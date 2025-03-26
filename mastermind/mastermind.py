import random
import tkinter 
import tkinter.messagebox

window = tkinter.Tk()
window.title('Demo Tkinter')
window.geometry('600x400')

texte = 'UwU\n :3'
lbl = tkinter.Label(window, text = texte, fg='white', bg='magenta', font = ("Times", "24", "bold italic"), justify = 'left')
lbl.pack(fill = "both", expand = True)

frm = tkinter.Frame(window)
frm.pack(side = 'bottom')

frm_lbl = tkinter.Label(frm, text = "code :").pack(side = 'left')
frm_fld = tkinter.Entry(frm)
frm_fld.pack(side = 'left')

def maj(msg):
    obtenir_chiffres()
    lbl.config(text = msg)
frm_btn = tkinter.Button(frm, text = 'Changer', command = lambda: maj( frm_fld.get()))
frm_btn.pack()

menu_bar = tkinter.Menu(window)
window.config(menu = menu_bar)

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
                chiffre = int("Entrez un code à 4 chiffres: ")
                if 0 <= chiffre <= 9999:
                    liste_chiffres.append(chiffre)
                else:
                    print("Veuillez entrer un code valide à 4 chiffres.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un code à quatres chiffres.")
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

window.mainloop()