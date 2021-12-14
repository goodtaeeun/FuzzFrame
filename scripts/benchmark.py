from triage import *


BINUTILS_TARGETS = [
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGo", "original"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGo", "original"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGo", "original"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGo", "original"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGo", "original"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGo", "original"),

    # ini/par/eva/min = 1.0/0.8/0.9/0.1 (back to original)
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "9fa81a5"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "9fa81a5"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "9fa81a5"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "9fa81a5"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "9fa81a5"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "9fa81a5"),

    # ini/par/eva/min = 1.0/0.8/0.9/0.2
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "e6d9cf2"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "e6d9cf2"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "e6d9cf2"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "e6d9cf2"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "e6d9cf2"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "e6d9cf2"),

    # ini/par/eva/min = 1.0/0.8/0.95/0.1
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "860498e"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "860498e"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "860498e"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "860498e"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "860498e"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "860498e"),

    # ini/par/eva/min = 1.0/0.8/0.8/0.1
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "e8e547f"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "e8e547f"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "e8e547f"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "e8e547f"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "e8e547f"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "e8e547f"),

    # ini/par/eva/min = 1.0/0.95/0.9/0.1
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "9f61798"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "9f61798"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "9f61798"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "9f61798"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "9f61798"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "9f61798"),

    # ini/par/eva/min = 1.0/0.9/0.9/0.1
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "8a60761"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "8a60761"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "8a60761"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "8a60761"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "8a60761"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "8a60761"),

    # ini/par/eva/min = 0.8/0.8/0.9/0.1
    ("cxxfilt-2016-4487", "stdin", check_cxxfilt_2016_4487, "AFLGOPT", "71c0cdb"),
    ("cxxfilt-2016-4489", "stdin", check_cxxfilt_2016_4489, "AFLGOPT", "71c0cdb"),
    ("cxxfilt-2016-4490", "stdin", check_cxxfilt_2016_4490, "AFLGOPT", "71c0cdb"),
    ("cxxfilt-2016-4491", "stdin", check_cxxfilt_2016_4491, "AFLGOPT", "71c0cdb"),
    ("cxxfilt-2016-4492", "stdin", check_cxxfilt_2016_4492, "AFLGOPT", "71c0cdb"),
    ("cxxfilt-2016-6131", "stdin", check_cxxfilt_2016_6131, "AFLGOPT", "71c0cdb"),


]


ALL_TARGETS = BINUTILS_TARGETS


def generate_worklist(iteration):
    
    targ_list = BINUTILS_TARGETS

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
