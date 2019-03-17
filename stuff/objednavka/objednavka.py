from faker import Faker
import random
import io
import string

fake = Faker()

objednavka = open("objednavka.txt", "a")
id = 7231815 + 1
for i in range(52000):
    datum_vytvorenia= fake.past_date(start_date= '-5y', tzinfo=None)
    datum_dokoncenia= fake.past_date(start_date= '-5y', tzinfo=None)
    if(datum_vytvorenia > datum_dokoncenia):
        temp = datum_vytvorenia
        datum_vytvorenia = datum_dokoncenia
        datum_dokoncenia = temp
    if(i%3 == 0):
        objednavka.write("{},{},0,{},{},{}\n".format(datum_vytvorenia, id, random.randrange(22512492), random.randrange(5,20000), datum_dokoncenia))
    else:
        objednavka.write("{},{},0,{},{},\n".format(datum_vytvorenia, id, random.randrange(22512492), random.randrange(5,20000)))
    id +=1
objednavka.close()
