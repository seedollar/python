# Use the "global" keyword so specify that you want to access the global scoped variable with the same name and modify it

global_var = "global"

def print_global_var():
    global global_var # You have told Python you want to use the global namespace
    global_var = "changed global"
    print(global_var)

print_global_var()
