lista=[]
import random
x=random.randrange(1,60)
print(x)

if x in lista:
    print("Sim,está na lista")

else:
    print("Não está")
 
    lista.append(x)
    print(lista)

while len(lista) < 6:
    x=random.randrange(1,60)
    print(x)

    if x in lista:
        print("Sim,está na lista")

    else:
        print("Não está")

        lista.append(x)
        print(lista)


