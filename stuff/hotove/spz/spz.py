from faker import Faker
import io
import string
import random

fake = Faker()

file1 = open("final.txt", "a")
file2 = open("final1.txt", "a")
file3 = open("final2.txt", "a")
file4 = open("final3.txt", "a")
file5 = open("final4.txt", "a")

count = 0
for i in range(4502543):
    for j in range(17):
        file1.write(random.choice(string.ascii_uppercase + string.digits))
        file2.write(random.choice(string.ascii_uppercase + string.digits))
        file3.write(random.choice(string.ascii_uppercase + string.digits))
        file4.write(random.choice(string.ascii_uppercase + string.digits))
        file5.write(random.choice(string.ascii_uppercase + string.digits))
    file1.write(",")
    file3.write(",")
    file2.write(",")
    file4.write(",")
    file5.write(",")
    for k in range(2):
         file1.write(random.choice(string.ascii_uppercase))
         file2.write(random.choice(string.ascii_uppercase))
         file3.write(random.choice(string.ascii_uppercase))
         file4.write(random.choice(string.ascii_uppercase))
         file5.write(random.choice(string.ascii_uppercase))
    for m in range(3):
         file1.write(random.choice(string.digits))
         file2.write(random.choice(string.digits))
         file3.write(random.choice(string.digits))
         file4.write(random.choice(string.digits))
         file5.write(random.choice(string.digits)) 
    for l in range(2):
         file1.write(random.choice(string.ascii_uppercase))
         file2.write(random.choice(string.ascii_uppercase))
         file3.write(random.choice(string.ascii_uppercase))
         file4.write(random.choice(string.ascii_uppercase))
         file5.write(random.choice(string.ascii_uppercase))

    datum = fake.past_date(start_date="-25y", tzinfo=None)
    file1.write(",{},{},{},{}\n".format(str(random.randrange(700,60000)),str(random.randrange(150)), count, datum))
    datum = fake.past_date(start_date="-25y", tzinfo=None)
    file2.write(",{},{},{},{}\n".format(str(random.randrange(700,30000)),str(random.randrange(150)), count + 1, datum))
    datum = fake.past_date(start_date="-25y", tzinfo=None)
    file3.write(",{},{},{},{}\n".format(str(random.randrange(700,550000)),str(random.randrange(150)), count + 2, datum))  
    datum = fake.past_date(start_date="-25y", tzinfo=None)
    file4.write(",{},{},{},{}\n".format(str(random.randrange(700,40000)),str(random.randrange(150)), count + 3, datum))
    datum = fake.past_date(start_date="-25y", tzinfo=None)
    file5.write(",{},{},{},{}\n".format(str(random.randrange(700,100000)),str(random.randrange(150)), count + 4, datum))
    count += 5
