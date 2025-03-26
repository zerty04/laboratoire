import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title('Demo Tkinter')
window.geometry('600x400')

#Affichage d'un texte grace à la classe 'Label'
texte = 'UwU\n :3'
lbl = tkinter.Label(window, text = texte, fg='white', bg='magenta', font = ("Times", "24", "bold italic"), justify = 'left')
lbl.pack(fill = "both", expand = True)

# Un bouton qui affiche "...clic!!!"
def clic ():
    lbl.config(text = "😺")
tkinter.Button(window, text = "CLIC", command = lambda:clic()).pack()

# Sous conteneur pour la zone de saisie
frm = tkinter.Frame(window)
frm.pack(side = 'bottom')

frm_lbl = tkinter.Label(frm, text = "Giga Chad :").pack(side = 'left')
frm_fld = tkinter.Entry(frm)
frm_fld.pack(side = 'left')

def maj(msg):
    lbl.config(text = msg)
frm_btn = tkinter.Button(frm, text = 'Changer', command = lambda: maj( frm_fld.get()))
frm_btn.pack()

menu_bar = tkinter.Menu(window)
window.config(menu = menu_bar)
# menu "Action"
menu_action = tkinter.Menu(menu_bar, tearoff = False)
menu_action.add_command(label = 'Miaou', command = lambda:clic())
menu_action.add_command(label = 'Ciao', command = lambda:window.quit())
menu_bar.add_cascade(label = "Action", menu = menu_action)
# Menu 'test'
menu_test = tkinter.Menu(menu_bar, tearoff = True)
menu_test.add_command(label = 'prout', command = lambda:maj("🫃"))
menu_bar.add_cascade(label ='test', menu = menu_test)

# affichage d'une boite de dialogue "modale"
def end_or_not():
    ok = tkinter.messagebox.askokcancel('---CONFIRMATION---','Spanish ?')
    if ok == True:
        window.quit()
    else:
        lbl.config(text = 'T PD')
menu_test.add_command(label = 'english or spanish ?', command = end_or_not)

def new_window():
    win_2 = tkinter.Tk()
    win_2.title("Nouvelle fenetre")
    win_2.geometry("300x200")
    tkinter.Label(win_2, text = '^^').pack(expand = True)
menu_test.add_command(label ='Nouvelle fenetre', command = lambda:new_window())

window.mainloop()