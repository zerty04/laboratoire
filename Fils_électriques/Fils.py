import pygame
import sys

# Liste des mini-jeux réussis
mini_jeux_reussis = []

symboles = (
        ["⚡", "🔋"],#chap 1
        ["🌞", "🔌"],
        ["🔥", "💥"],
        ["🧲", "🔄"],
        ["🔧", "⚙️"],

        ["🧪", "💥"],#chap 2
        ["🔥", "💥"],
        ["🪨", "💎"],
        ["💧", "☁️"],
        ["🌋", "🌱"],

        ["🧬", "🧫"],#chap 3
        ["💧", "🌱"],
        ["🧬", "🦕"],
        ["🌬", "👃"],
        ["🩸", "❤️"],

        ["📡", "📶"],#chap 4  
        ["🎧", "💨"],
        ["💡", "🌫"],
        ["🎵", "👂"],
        ["🔢", "🎼"]
)


carnet_professeur = {
    0: "Tout autour de moi, l'énergie danse, invisible, insaisissable... Mais j'ai compris ! Il faut savoir la capturer et la stocker !",
    1: "J’ai tendu une plaque sous le soleil, et voilà ! Un courant s’est formé, capturé dans mes circuits.",
    2: "L’étincelle jaillit, cherchant un chemin. Mais un mauvais contact, et c’est l’explosion !",
    3: "Les aimants dansent en rythme, créant un flux mystérieux. Serait-ce la clé du mouvement perpétuel ?",
    4: "Ma machine vibre, ronronne… chaque pièce s’imbrique, chaque rouage trouve sa place.",
    
    5: "Une simple goutte d’un acide inconnu, et ma roche se dissout instantanément. Quelle puissance !",
    6: "Un simple coup de feu sur cette poudre blanche... et BOUM ! Mes sourcils ont disparu.",
    7: "J'ai trouvé une roche terne, insignifiante. Je l'ai soumise à une pression titanesque... et en ai extrait une pure merveille !",
    8: "L'eau bout, puis disparaît en vapeur... mais en la capturant, elle se fige de nouveau en gouttelettes. Le cycle est éternel.",
    9: "Des cendres noires et fines après la combustion… et si elles contenaient la clé d’une nouvelle création ?",
    
    10: "L’ADN est un code, mais un code qui peut être altéré.",
    11: "Un simple contact avec l'eau, et ces graines se sont éveillées ! L'humidité est la clé du renouveau.",
    12: "Ces cellules se divisent encore et encore... Une créature en gestation, un miracle en devenir !",
    13: "L’air est invisible, et pourtant sans lui, tout s’éteint... La respiration, moteur du vivant.",
    14: "Le sang circule, porteur de chaleur et de vitalité. Sans lui, le corps devient froid et inerte...",
    
    15: "J'ai tendu une antenne vers le ciel... et j'ai capté des signaux étranges, venus d'ailleurs.",
    16: "Le son voyage dans l'air, mais sous l'eau, il se déplace différemment... plus vite, plus profondément.",
    17: "J'ai émis un signal lumineux dans le brouillard... et j'ai vu une ombre y répondre. Qui était-ce ?",
    18: "Une simple vibration, et l’air se met à chanter... Le son, une onde invisible, mais si puissante.",
    19: "J’ai superposé des fréquences, et un motif est apparu. La musique des nombres ?"
}

print(symboles[2], carnet_professeur[2])

def INDEX():
    try:
        symbole = int(input("index de symbole"))
        carnet = int(input("index du carnet"))
        if symbole == carnet:
            print("C'est tout bon")
        else:
            print("Pas bon")
    except ValueError:
        print("un entier")


pygame.init()

fenetre = pygame.display.set_mode((300,300))
pygame.display.set_caption("Mon Jeu")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                False

    fenetre.fill((255,255,255))
    pygame.display.flip

pygame.quit()