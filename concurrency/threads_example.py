import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Threading %s says %s" % (threading.current_thread(), what))
    
if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        thread = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        thread.start()