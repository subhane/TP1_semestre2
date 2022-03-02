import random

def randomNumber():
    randomNum = ''
    for i in range(4):
        k = random.randrange(0, 9)
        randomNum += str(k)
    return randomNum

number = randomNumber()
print(number)
Star = 0
Hammer = 0

L=[]
for i in number:
    L.append(int(i))

while True:
    userNumber = input("Veuillez choisir un nombre : ")
    position = input("Veuillez choisir une position : ")
    if number[int(position)-1] == userNumber:
        Star += 1
        L[int(position)-1] = 0
        print(L)
    else:
        Hammer += 1
    print("Etoile : " + str(Star) + " et Marteaux : " + str(Hammer))
    if L == [0, 0, 0, 0]:
        print("vous avez trouvé le numéro magique !")
        break



