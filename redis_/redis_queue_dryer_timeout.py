# This example shows how you can use other methods to terminate the processing of consuming messages from a REDIS queue.
# This exmaple works in conjunction with the redis_queue_washer.py example, and should be started first in a background
# process.

def dryer_timeout():
    import redis, os, time
    conn = redis.Redis()
    pid = os.getpid();
    timeout = 20 # 20 seconds
    print("Dryer process %s is starting" % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s dried %s' % (pid, val))
        time.sleep(0.1)
    print("Dryer process %s is done" % pid)

import multiprocessing
DRYERS=3
for num in range(DRYERS):
    p = multiprocessing.Process(target=dryer_timeout)
    p.start()
    