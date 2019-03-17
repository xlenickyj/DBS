import random

materialista = open("material_oprava.txt","a")
id=14465759

for i in range(7231816,7283816):
    for l in range(random.randrange(3)):
        materialista.write("{},{},{}\n".format(str(i), str(random.randrange(2100580)), str(id)))
        id +=1
materialista.close()
