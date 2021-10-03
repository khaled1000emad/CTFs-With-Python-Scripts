import requests
from bs4 import BeautifulSoup, Comment
url = "http://natas0.natas.labs.overthewire.org"

r = requests.post(url, auth=('natas0','natas0'))
soup = BeautifulSoup(r.text, 'html.parser')
comments = soup.find_all(text=lambda text:isinstance(text, Comment))
print(comments[1])
