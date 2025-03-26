import random
def code1():
    code =[]
    for i in range(4):
        code.append(random.randint(0,9))
    return code 
globcode = code1()
print(globcode)



def obtenir_chiffres():
        liste_chiffres = []
        while len(liste_chiffres) < 4:
            try:
                chiffre = int(input("Entrez un chiffre entre 0 et 9 : "))
                if 0 <= chiffre <= 9:
                    liste_chiffres.append(chiffre)
                else:
                    print("Veuillez entrer un chiffre valide entre 0 et 9.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre entre 0 et 9.")
        return liste_chiffres

def compare():
        Bon_endroit = 0
        Mauvais_endroit = 0
        for elem1,elem2 in zip(globbornes,globcode):
            if elem1 == elem2:
                Bon_endroit = Bon_endroit + 1

        for element in globcode:
            if element in globbornes:
                Mauvais_endroit = Mauvais_endroit + 1
        Mauvais_endroit = Mauvais_endroit - Bon_endroit
        print(Bon_endroit,'chiffres placés au bon endroit et',Mauvais_endroit,'chiffres placés au mauvais endroit')
        return Bon_endroit




Historique = []
crack = False 
while crack == False:
    
    globbornes = obtenir_chiffres()
    Historique.append(globbornes)
    for element in Historique:
        print(element)

    
    if compare() == 4:
        crack = True
print("Bravo, vous avez trouver le code !!!")