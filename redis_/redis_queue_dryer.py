# Example of how to consume messages from a REDIS queue. This example is used in conjunction with the
# redis_queue_washer.py.
import redis

conn = redis.Redis()
print("Dryer is starting...")
while True:
    msg = conn.blpop('dishes')
    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
    print('Dried', val)
print('Dishes are dried')
