from faker import Faker
import io
import random

fake = Faker()

final = open("servis.txt", "a")
firma = "firstname.txt"
pripona = "lastname.txt"
count = 0
with open(firma) as prve:
   first = prve.readline()
   while first:
       with open(pripona) as druhe:
            suffix = druhe.readline()
            first = prve.readline()
            while suffix:
                 datum = fake.date(pattern="%Y-%m-%d", end_datetime=None)
                 final.write("{},{} {},".format(str(count),first.strip(), suffix.strip()))
                 dic = random.randrange(1000000000,9999999999)
                 ico = random.randrange(10000000,99999999)
                 final.write("{},{},{},SK{}\n".format(datum,ico,dic,dic))
                 count += 1
                 suffix = druhe.readline()
