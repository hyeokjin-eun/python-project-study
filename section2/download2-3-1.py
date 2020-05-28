import urllib.request as dw
from urllib.parse import urlparse

url = "http://www.encar.com/"

mem = dw.urlopen(url)

print(type(mem))
print("geturl :",mem.geturl())
print("status :",mem.status)
print("headers :",mem.getheaders())
print("info :",mem.info(),"\n")
print("getcode :",mem.getcode())
print("read :",mem.read(10).decode('utf-8'))
print(urlparse('http://www.encar.co.kr?test=test').query)
