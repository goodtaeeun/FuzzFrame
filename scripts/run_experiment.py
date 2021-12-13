import sys, os, subprocess, time, csv
from benchmark import generate_worklist

BASE_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
IMAGE_NAME = "aflgopt"
MAX_INSTANCE_NUM = 50
SUPPORTED_TOOLS = ["AFLGo", "AFLGOPT"]


def run_cmd(cmd_str):
    print("[*] Executing: %s" % cmd_str)
    cmd_args = cmd_str.split()
    try:
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        return str(output)
    except Exception as e:
        print(e)
        exit(1)


def run_cmd_in_docker(tool, target, version, iter_id, cmd_str, is_detached):
    container = "%s-%s-%s-%s" % (tool, target, version, iter_id)
    print("[*] Executing '%s' in container %s" % (cmd_str, container))
    exec_flag = "-d" if is_detached else ""
    cmd_prefix = "docker exec %s %s /bin/bash -c" % (exec_flag, container)
    cmd_args = cmd_prefix.split()
    cmd_args += [cmd_str]
    try:
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        return str(output)
    except Exception as e:
        print(e)
        exit(1)


def check_cpu_count():
    n_str = 60
    try:
        if int(n_str) < MAX_INSTANCE_NUM:
            print("Not enough CPU cores, please decrease MAX_INSTANCE_NUM")
            exit(1)
    except Exception as e:
        print(e)
        print("Failed to count the number of CPU cores, abort")
        exit(1)


def decide_outdir():
    i = 0
    while True:
        i += 1
        outdir = os.path.join(BASE_DIR, "output", "%d" % (i))
        if not os.path.exists(outdir):
            return outdir


def fetch_works(worklist):
    works = []
    for i in range(MAX_INSTANCE_NUM):
        if len(worklist) <= 0:
            break
        works.append(worklist.pop(0))
    return works


def spawn_containers(works):
    for i in range(len(works)):
        target, iter_id, _, tool, version = works[i]
        cmd = "docker run --tmpfs /box:exec --rm -m=8g --cpuset-cpus=%d -it -d --name %s-%s-%s-%s %s" \
                % (i, tool, target, version, iter_id, IMAGE_NAME)
        run_cmd(cmd)


def run_fuzzing(works, timelimit):
    for (target, iter_id, input_src, tool, version) in works:
        if tool == "AFLGOPT":
            cmd = "/fuzzer/build_AFLGOPT.sh %s" % (version)
            run_cmd_in_docker(tool, target, version, iter_id, cmd, True)

        cmd = "/tool-script/run_%s.sh %s %s %d" % \
                (tool, target, input_src, timelimit)
        run_cmd_in_docker(tool, target, version, iter_id, cmd, True)


def wait_finish(works, timelimit):
    time.sleep(timelimit)
    total_count = len(works)
    elapsed_min = 0
    while True:
        time.sleep(60)
        elapsed_min += 1
        print("Waited for %d min" % elapsed_min)
        finished_count = 0
        for (target, iter_id, _, tool, version) in works:
            stat_str = run_cmd_in_docker(tool, target, version, iter_id, "cat /STATUS", False)
            if "FINISHED" in stat_str:
                finished_count += 1
            else:
                print("%s-%s-%s-%s not finished" % (tool, target, version, iter_id))
        if finished_count == total_count:
            print("All works finished!")
            break


def store_outputs(works, outdir):
    for (target, iter_id, _, tool, version) in works:
        container = "%s-%s-%s-%s" % (tool, target, version, iter_id)
        cmd = "docker cp %s:/output %s/%s" % (container, outdir, container)
        run_cmd(cmd)


def cleanup_containers(works):
    for (target, iter_id, _, tool, version) in works:
        cmd = "docker kill %s-%s-%s-%s" % (tool, target, version, iter_id)
        run_cmd(cmd)


def main():
    if len(sys.argv) != 3:
        print("Usage: %s <timelimit> <iter#>" % sys.argv[0])
        exit(1)

    timelimit = int(sys.argv[1])
    iteration = int(sys.argv[2])


    worklist = generate_worklist(iteration)
    outdir = decide_outdir()
    os.makedirs(outdir)
    while len(worklist) > 0:
        works = fetch_works(worklist)
        spawn_containers(works)
        run_fuzzing(works, timelimit)
        wait_finish(works, timelimit)
        store_outputs(works, outdir)
        cleanup_containers(works)


if __name__ == "__main__":
    main()
