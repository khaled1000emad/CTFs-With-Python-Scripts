The challenge link: https://www.zixem.altervista.org/SQLi/login_lvl5.php
This challenege required a password which was easily found (hashed) in the source code

![image](https://user-images.githubusercontent.com/58134995/135036541-a5e70f56-2366-4e54-b957-b604c4dd2ada.png)



Nice so when we login we found this message: 

![image](https://user-images.githubusercontent.com/58134995/135036632-041195bd-014d-4ba5-a38e-111450a06eb5.png)

So we now know that our password is consisted of only numbers [ it also passed as a get parameter ], so i wrote the python script and i waited for ~ 3min and:

![image](https://user-images.githubusercontent.com/58134995/135036817-b45e6dfe-d895-4957-8731-db8f2965c8d9.png)

When i tried this password :
![image](https://user-images.githubusercontent.com/58134995/135036920-3ee6ac28-6e7f-4404-ace1-ff805f279c8f.png)

No i didn't
