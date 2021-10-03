import requests
from bs4 import BeautifulSoup
import base64
# Crafting the payload
url = 'http://natas8.natas.labs.overthewire.org'
encodedSecret = "3d3d516343746d4d6d6c315669563362"
decode_from_hex = bytes.fromhex(encodedSecret).decode()
reversed = decode_from_hex[::-1]
final_secret = base64.b64decode(reversed).decode()
# Sending the data
data={'secret':'oubWYf2kBq', 'submit':'Submit+Query'}
r = requests.post(url, auth=('natas8','DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'), data=data)


# Scraping the passowrdd
soup=BeautifulSoup(r.text, 'html.parser')
tag = soup.find('div', attrs={'id':'content'})
password = tag.text.strip()[16:75]
print(password)
