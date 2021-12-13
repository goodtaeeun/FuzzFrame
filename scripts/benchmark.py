from triage import *


BINUTILS_TARGETS = [
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGo", "original"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGo", "original"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGo", "original"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGo", "original"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGo", "original"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGo", "original"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", ),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),

    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT"),



]


ALL_TARGETS = BINUTILS_TARGETS


def generate_worklist(benchmark, iteration):
    if benchmark == "all":
        targ_list = ALL_TARGETS
    elif benchmark == "binutils":
        targ_list = BINUTILS_TARGETS
    else:
        print("Unsupported benchmark: %s" % benchmark)
        exit(1)

    worklist = []
    for (targ_name, input_src, _, tool, version) in targ_list:
        for i in range(iteration):
            iter_id = "iter-%d" % i
            worklist.append((targ_name, iter_id, input_src, tool, version))
    return worklist


def check_targeted_crash(targ, replay_buf):
    for (targ_name, _, crash_checker) in ALL_TARGETS:
        if targ_name == targ:
            return crash_checker(replay_buf)
    print("Unknown target: %s" % targ)
    exit(1)
