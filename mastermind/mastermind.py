import random
def code1():
    code =[]
    for i in range(4):
        code.append(random.randint(0,9))
    return code 
globcode = [code1()]
print(globcode)

def devine():
    bornes = {}
    for i in range(4):
        bornes[i]= int(input("selectionner un chiffre"))
    return bornes
globbornes = devine()
print (globbornes)


def compare():
    for i in range(4):
        if globbornes[i] == globcode[i]:
            print("lol")