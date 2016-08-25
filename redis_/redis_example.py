import redis

conn = redis.Redis()

print(conn.keys('*'))

conn.set('secret', 'ni! We are the knights of Ni!')

print(conn.get('secret'))
print(conn.getrange('secret', -14, -1))

# Set multiple keys with mset()
conn.mset({'dice': 5, 'corners': 12})

print(conn.mget(['dice', 'corners']))

conn.delete('corners')
print(conn.get('corners'))

conn.incr('dice')
conn.incr('dice', 3)
print(conn.get('dice'))

# lpush will insert the string at the beginning of the list
conn.lpush('zoo', 'tiger')
conn.lpush('zoo', 'lion', 'leopard')
print(conn.lrange('zoo', 0, 2))



