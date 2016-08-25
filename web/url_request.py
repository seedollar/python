import urllib.request as ur

url = 'http://www.joelonsoftware.com/articles/LeakyAbstractions.html'
url_image = 'http://thisiswhyyourecute.com/wp-content/uploads/2013/03/amazing_photos_of_animals_caught_in_the_act_640_35-560x391.jpg'
conn = ur.urlopen(url)
print(conn.status)
print(conn.getheader('Content-Type'))

conn2 = ur.urlopen(url_image)
print(conn2.status)
print(conn2.getheader('Content-Type'))

for key, value in conn2.getheaders():
    print(key + ":", value)
