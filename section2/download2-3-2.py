import urllib.request as ur
import urllib.parse as up

API = "https://api.ipify.org"

values = {
    'format' : 'json'
}

params = up.urlencode(values)

url = API + "?" + params
data = ur.urlopen(url).read()
text = data.decode("utf-8")
print(text)
