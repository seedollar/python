import memcache

db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
print(db.get('marco'))


