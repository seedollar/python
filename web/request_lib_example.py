# Illustrates the use of the "request" library to make http requests

import requests

url = 'http://www.joelonsoftware.com/articles/LeakyAbstractions.html'

resp = requests.get(url)
print(resp)
print(resp.text)
