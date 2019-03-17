import io
import random

vlastnictvo= open("vlastnictvo1.txt","a")
for i in range(22512508,22512630):
    vlastnictvo.write(str(i))
    vlastnictvo.write(",0,{}\n".format(str(i)))
vlastnictvo.close()
