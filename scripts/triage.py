
def warn(msg, buf, dump=True):
    print("[Warning]: %s" % msg)
    if dump:
        print("Check the following replay log:")
        print(buf)


# Helper function for for-all check.
def check_all_exist(buf, checklist):
    for str_to_check in checklist:
        if str_to_check not in buf:
            return False
    return True


# Helper function for if-any check.
def check_any_exist(buf, checklist):
    for str_to_check in checklist:
        if str_to_check in buf:
            return True
    return False


def check_cxxfilt_2016_4487(buf):
    if "register_Btype" in buf:
        if "cplus-dem.c:4319" in buf:
            return True
        else:
            warn("Unexpected crash point in register_Btype()", buf)
            return False
    else:
        return False


def check_cxxfilt_2016_4489(buf):
    return check_all_exist(buf, ["cplus-dem.c:3007"])


def check_cxxfilt_2016_4490(buf):
    if "d_unqualified_name" in buf:
        if "cp-demangle.c:1596" in buf:
            return True
        else:
            warn("Unexpected crash point in d_unqualified_name()", buf)
            return False
    else:
        return False


def check_cxxfilt_2016_4491(buf):
    return check_all_exist(buf, ["stack-overflow", "d_print_comp"])


def check_cxxfilt_2016_4492(buf):
    if "do_type" in buf and "register_Btype" not in buf and "stack-overflow" not in buf:
        if check_any_exist(buf, ["cplus-dem.c:3606", "cplus-dem.c:3781"]):
            return True
        else:
            if "demangle_template" in buf:
                warn("do-type() + demangle_tempate() in the trace", buf, False)
            else:
                warn("Unexpected crash point in do_type()", buf)
            return False
    else:
        return False


def check_cxxfilt_2016_6131(buf):
    return check_all_exist(buf, ["stack-overflow", "do_type"])
