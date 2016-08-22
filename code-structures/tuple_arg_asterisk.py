# When you specify an asterisk in the parameter list, it transforms the parameters into a tuple.
# Common idiom is to call the parameter *args

def capture_list(*args):
    print("Elements:", args)

capture_list()

capture_list("H", 334, 9973, "YT", 498.23, True)