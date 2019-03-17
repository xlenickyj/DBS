from faker import Faker
import io
import random
fake = Faker()

file = open("employees.txt","a")
mena = open("mena.txt", "r")
priezviska = "priezviska.txt"
count1 = 2113273
for i in range(572):
   meno = mena.readline()
   meno.strip()
   with open(priezviska) as pv:
      priezvisko = pv.readline()
      while priezvisko:
         priezvisko = pv.readline()     
         file.write("{} {},".format(meno.strip(),priezvisko.strip()))
         file.write("{}, ".format(str(fake.date())))
         file.write("{},".format(str(count1)))
         file.write("{},{}\n".format(str(random.randrange(1743977)), str(random.randint(500,2000))))
         count1 +=1
