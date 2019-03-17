from faker import Faker
import io
import string
import random

fake = Faker()
final = open("customers.txt", "a")
mena = open("mena.txt", "r")
priezviska = "priezviska.txt"
count1 = 0
count2 = 0

for i in range(4947):
   meno = mena.readline()
   meno.strip()
   with open(priezviska) as pv:
      priezvisko = pv.readline()
      while priezvisko:
         if i < 2500:
            for k in range(2):
                  final.write(random.choice(string.ascii_uppercase))
            for k in range(6):
                  final.write(random.choice(string.digits))
            datum = fake.date_between(start_date='-49y', end_date='-18y')
            final.write(",{},{},{},{}\n".format(str(count2), meno.strip(), datum, priezvisko.strip()))
            count2 +=1
         priezvisko = pv.readline()
final.close()
