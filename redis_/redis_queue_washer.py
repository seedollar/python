# This example shows how you can push messages to a REDIS queue, and see how they are consumed.
# This example works in conjunction with the redis_queue_dryer.py file which should be started first.
import redis

conn = redis.Redis()
print('Washer is starting...')
dishes = ['salad', 'bread', 'dessert', 'entree']

for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
print('Washer is done')
