# Shows the use of the globals() and locals() functions
global_var1 = "global1"
global_var2 = 8683.45
def local_func():
    var1 = "test"
    var2 = 494.2
    print("LOCALS:",locals())

local_func()

print('GLOBALS', globals())
