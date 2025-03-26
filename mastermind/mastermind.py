import random
def code1():
    code =[]
    for i in range(4):
        code.append(random.randint(0,9))
    return code 
globcode = code1()
print(globcode)

crack = False 
while crack == False:
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
        chiffre = set()
        for elem1,elem2 in zip(globbornes,globcode):
            chiffre.add(elem1)
            if elem1 == elem2:
                Bon_endroit = Bon_endroit + 1
        
        for i in range (4):
            if globbornes[i] in chiffre:
                Mauvais_endroit = Mauvais_endroit + 1
                chiffre.remove(globbornes[i])
        Mauvais_endroit = Mauvais_endroit - Bon_endroit
        print(Bon_endroit,'chiffres placés au bon endroit et',Mauvais_endroit,'chiffres placés au mauvais endroit')
        return Bon_endroit
    if compare() == 4:
        crack = True