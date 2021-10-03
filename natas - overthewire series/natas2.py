import requests
url = "http://natas2.natas.labs.overthewire.org/files/users.txt"
r = requests.get(url, auth=('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'))
password = r.text[78:110]
print("the password for natas 3 is "+password)
