import random
def code1():
    code =[]
    for i in range(4):
        code.append(random.randint(0,9))
    return code 
globcode = code1()
print(globcode)

def devine():
    bornes = []
    for i in range(4):
        bornes.append(int(input("selectionner un chiffre")))
    return bornes
globbornes = devine()
print (globbornes)

def compare():
    Bon_endroit = 0
    Mauvais_endroit = 0
    for elem1,elem2 in zip(globbornes,globcode):
        if elem1 == elem2:
            Bon_endroit = Bon_endroit + 1
    
    for i in range (4):
        if globbornes[i] in globcode:
            Mauvais_endroit = Mauvais_endroit + 1
    Mauvais_endroit = Mauvais_endroit - Bon_endroit
    print(Bon_endroit,'chiffres placés au bon endroit et',Mauvais_endroit,'chiffres placés au mauvais endroit')
    return
compare()