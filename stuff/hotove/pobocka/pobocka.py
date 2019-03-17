from faker import Faker
import io
import random

final = open("pobocka.txt", "a")
street = open("streets.txt", "r")
fake_data= Faker()
ulica = "washington-dc.osm.streets.txt"
count= 0
for i in range(44):
   line= street.readline()
   with open(ulica) as name:
      namo = name.readline()
      while namo:
           city = fake_data.city()
           state = fake_data.state()
           final.write("{},{} {},{},{} {},{},{}\n".format(str(count),namo.strip('\n'), line.strip('\n'), random.randrange(0,2713103), random.randrange(100,999), random.randrange(100,999), city, state))
           count += 1
           namo = name.readline()
