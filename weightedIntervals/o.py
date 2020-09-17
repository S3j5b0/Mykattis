
import random
file1 = open("MyFile.txt","w")

randstartish = 0
randstopish = 5

roundcount = 0
file1.write("20000 \n")
for i in range(0,20000):
    randstarting = randstartish + random.randint(0,5) + roundcount
    randstopping = randstarting + random.randint(0, 3) 
    #generating values 
    start = randstarting
    stop = randstopping
    value = (stop - start) + random.randint(0,2)

    file1.write(str(start) + " " + str(stop) + " " + str(value) + "\n")
    roundcount = roundcount + 1


l = [None] * 5

