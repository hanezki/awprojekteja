import urllib.request
import requests
#contents = urllib.request.urlopen("http://34.125.89.188/health.html").read()
r = requests.get("http://34.125.89.188/health.html")
print(r)