# This example illustrates how we can implement a publish-subscribe pattern using REDIS.
import redis, random

conn = redis.Redis()
cats = ['siamese', 'persian', 'maine coon', 'ginger', 'blue']
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']

for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print("Publish %s wears a %s" % (cat,hat))
    conn.publish(cat, hat)



