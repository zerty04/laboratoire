import random
def code1():
    code =[]
    for i in range(4):
        code.append(random.randint(0,9))
    return code 
globcode = code1()
print(globcode)

def devine():
    bornes = {}
    for i in range(4):
        bornes[i]= int(input("selectionner un chiffre"))
    return bornes
globbornes = devine()
print (globbornes)


def compare():
    for i in range(3):
        Bon_endroit = 0
        Mauvais_endroit = 0
        if globbornes[i] == globcode[i]:
            Bon_endroit = Bon_endroit + 1
        elif globbornes[i] in globcode:
            Mauvais_endroit = Mauvais_endroit + 1
    print(Bon_endroit,'chiffres placés au bon endroit et',Mauvais_endroit,'chiffres placés au mauvais endroit')
    return
compare()