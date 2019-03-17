import random
import string

cm = open("cena.txt", "a")
material = open("material.txt", "a")
for i in range(2100776):
        material.write("{},".format(str(i)))
        for j in range(10):
            material.write("{}".format(random.choice(string.ascii_uppercase + string.digits)))
        material.write(",{}\n".format(random.randrange(1,24)))
