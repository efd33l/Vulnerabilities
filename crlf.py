import sys
import urllib
import urllib.error
import urllib.request

host = "10.251.0.83:7777?a=1 HTTP/1.1\r\nX-injected: header\r\nTEST: 123"
url = "http://" + host + ":8080/test/?test=a"

try:
    info = urllib.request.urlopen(url).info()
    print(info)
except urllib.error.URLError as e:
    print(e)
