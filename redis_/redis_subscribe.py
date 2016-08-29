# Example of publish-subscribe. Used in conjunction with the redis_publish.py file.
import redis

conn = redis.Redis()

topics = ['blue', 'ginger']
sub = conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print("Subscribe: %s wears a %s" % (cat, hat))
        