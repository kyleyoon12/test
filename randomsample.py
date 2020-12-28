import random

hanguls = list("가나다라마바사아자차카타파하")

with open("naming.txt","w")as file:
    for i in range(10):
        name = random.choice(hanguls)
        height = random.randrange(140,180)
        weight = random.randrange(40,60)

        file.write("{},{},{}\n".format(name,height,weight))
