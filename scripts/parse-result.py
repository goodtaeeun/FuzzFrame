import sys, os
from benchmark import check_targeted_crash

REPLAY_LOG_FILE = "replay_log.txt"
FUZZ_LOG_FILE = "fuzzer_stats"
REPLAY_ITEM_SIG = "Replaying crash - "
FOUND_TIME_SIG = "found at "


def median(int_list):
    sorted_list = list(int_list)
    sorted_list.sort()
    n = len(sorted_list)
    if n % 2 == 0: # Even number
        i = n/2 - 1
    else: # Odd number
        i = n/2
    j = n/2
    return (sorted_list[int(i)] + sorted_list[int(j)]) / 2


def get_experiment_info(outdir):
    targ_list = []
    max_iter_id = 0
    for d in os.listdir(outdir):
        if d.endswith("-iter-0"):
            targ = d[:-len("-iter-0")]
            targ_list.append(targ)
        iter_id = int(d.split("-")[-1])
        if iter_id > max_iter_id:
            max_iter_id = iter_id
    iter_cnt = max_iter_id + 1
    return (targ_list, iter_cnt)


def parse_tte(targ, targ_dir):
    log_file = os.path.join(targ_dir, REPLAY_LOG_FILE)
    f = open(log_file, "r")
    buf = f.read()
    f.close()
    while REPLAY_ITEM_SIG in buf:
        # Proceed to the next item.
        start_idx = buf.find(REPLAY_ITEM_SIG)
        buf = buf[start_idx + len(REPLAY_ITEM_SIG):]
        # Identify the end of this replay.
        if REPLAY_ITEM_SIG in buf:
            end_idx = buf.find(REPLAY_ITEM_SIG)
        else: # In case this is the last replay item.
            end_idx = len(buf)
        replay_buf = buf[:end_idx]
        if check_targeted_crash(targ, replay_buf):
            found_time = int(replay_buf.split(FOUND_TIME_SIG)[1].split()[0])
            return found_time
    # If not found, approximate as the timeout (24 hour in our case). This is
    # okay as long as we report the median value.
    return 86400


def parse_stat(targ, targ_dir):
    log_file = os.path.join(targ_dir, FUZZ_LOG_FILE)
    f = open(log_file, "r")
    buf = f.read()
    f.close()
    execs = int(buf.split("execs_done")[1].split(": ")[1].split()[0])
    paths_total = int(buf.split("paths_total")[1].split(": ")[1].split()[0])
    paths_favored = int(buf.split("paths_favored")[1].split(": ")[1].split()[0])
    bitmap_cvg = float(buf.split("bitmap_cvg")[1].split(": ")[1].split("%")[0])
    path_ratio = float(paths_total) / float(execs)
    edge_ratio = float(paths_favored) / float(execs)
    return (execs, path_ratio, edge_ratio, bitmap_cvg)


def analyze_targ_result(outdir, targ, iter_cnt):
    tte_list = []
    execs_list = []
    path_ratio_list = []
    edge_ratio_list = []
    bitmap_cvg_list = []
    for iter_id in range(iter_cnt):
        targ_dir = os.path.join(outdir, "%s-iter-%d" % (targ, iter_id))
        tte = parse_tte(targ, targ_dir)
        tte_list.append(tte)
        (execs, path_ratio, edge_ratio, bitmap_cvg) = parse_stat(targ, targ_dir)
        execs_list.append(execs)
        path_ratio_list.append(path_ratio)
        edge_ratio_list.append(edge_ratio)
        bitmap_cvg_list.append(bitmap_cvg)
    print("(Result of %s)" % targ)
    print("Time-to-error: %s (median = %d)" % (tte_list, median(tte_list)))
    min_execs = min(execs_list)
    max_execs = max(execs_list)
    avg_execs = sum(execs_list) / len(execs_list)
    print("Execs: %d - %d (avg = %d)" % (min_execs, max_execs, avg_execs))
    min_path_ratio = min(path_ratio_list) * 100.0
    max_path_ratio = max(path_ratio_list) * 100.0
    print("Path ratio: %.4f - %.4f" % (min_path_ratio, max_path_ratio))
    min_edge_ratio = min(edge_ratio_list) * 100.0
    max_edge_ratio = max(edge_ratio_list) * 100.0
    print("Edge ratio: %.4f - %.4f" % (min_edge_ratio, max_edge_ratio))
    min_bitmap_cvg = min(bitmap_cvg_list)
    max_bitmap_cvg = max(bitmap_cvg_list)
    print("Bitmap coverage: %.2f - %.2f" % (min_bitmap_cvg, max_bitmap_cvg))
    print("------------------------------------------------------------------")


def main():
    if len(sys.argv) != 2:
        print("Usage: %s <output dir>" % sys.argv[0])
        exit(1)
    outdir = sys.argv[1]
    targ_list, iter_cnt = get_experiment_info(outdir)
    targ_list.sort()
    for targ in targ_list:
        analyze_targ_result(outdir, targ, iter_cnt)


if __name__ == "__main__":
    main()
