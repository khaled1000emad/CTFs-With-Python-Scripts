import requests
from bs4 import BeautifulSoup, Comment

url = "http://natas1.natas.labs.overthewire.org"
r = requests.get(url, auth=('natas1','gtVrDuiDfck831PqWsLEZy5gyDz1clto'))
soup = BeautifulSoup(r.text, 'html.parser')

comments = soup.find_all(text=lambda text:isinstance(text, Comment))
print(comments[1])
