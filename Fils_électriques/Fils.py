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

assoc_symboles = {
    'bouton1': "⚡",
    'bouton2': "🔧",
    'bouton3': "🌞",
    'bouton4': "🔥",
    'bouton5': "🧲",
    'bouton6': "💥",
    'bouton7': "🔌",
    'bouton8': "⚙️",
    'bouton9': "🔄",
    'bouton10': "🔋"
}

connexions = [] 
bouton_selectionne = None


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

pygame.init()

fenetre = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Fils électriques")

bouton1 = pygame.Rect(40, 30, 50, 50) 
bouton2 = pygame.Rect(40, 100, 50, 50)
bouton3 = pygame.Rect(40, 172, 50, 50)
bouton4 = pygame.Rect(40, 246, 50, 50)
bouton5 = pygame.Rect(40, 320, 50, 50)

bouton6 = pygame.Rect(500, 30, 50, 50)
bouton7 = pygame.Rect(500, 100, 50, 50)
bouton8 = pygame.Rect(500, 172, 50, 50)
bouton9 = pygame.Rect(500, 246, 50, 50)
bouton10 = pygame.Rect(500, 320, 50, 50)

boutons_gauche = [bouton1, bouton2, bouton3, bouton4, bouton5]
boutons_droite = [bouton6, bouton7, bouton8, bouton9, bouton10]

# Images
image_bouton1 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/electricite.jpg')
image_bouton1 = pygame.transform.scale(image_bouton1, (50, 50))
image_bouton2 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/cle_a_molette.jpg')
image_bouton2 = pygame.transform.scale(image_bouton2, (50, 50))
image_bouton3 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/soleil.jpg')
image_bouton3 = pygame.transform.scale(image_bouton3, (50, 50))
image_bouton4 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/feu.jpg')
image_bouton4 = pygame.transform.scale(image_bouton4, (50, 50))
image_bouton5 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/aimant.jpg')
image_bouton5 = pygame.transform.scale(image_bouton5, (50, 50))
image_bouton6 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/explosion.jpg')
image_bouton6 = pygame.transform.scale(image_bouton6, (50, 50))
image_bouton7 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/prise.jpg') # prise
image_bouton7 = pygame.transform.scale(image_bouton7, (50, 50))
image_bouton8 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/Rouage.jpg')
image_bouton8 = pygame.transform.scale(image_bouton8, (50, 50))
image_bouton9 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/reverse.jpg')
image_bouton9 = pygame.transform.scale(image_bouton9, (50, 50))
image_bouton10 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/batterie.jpg') #batterie
image_bouton10 = pygame.transform.scale(image_bouton10, (50, 50))

bouton_verification = pygame.Rect(250, 10, 100, 40) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si on clique sur la croix (X)
            running = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            # Vérifier si clic sur un bouton de gauche
            for b in boutons_gauche:
                if b.collidepoint(pos):
                    bouton_selectionne = b  # Sélectionner bouton gauche
                    break
            else:  # Si pas de bouton gauche, on vérifie bouton droite
                for b in boutons_droite:
                    if b.collidepoint(pos) and bouton_selectionne:
                        connexions.append((bouton_selectionne, b))  # Connexion 
                        bouton_selectionne = None 
                        break

            # Vérification du bouton de vérification
            if bouton_verification.collidepoint(pos):
                print("Vérification des connexions...")
                for gauche, droite in connexions:
                    sym_gauche = assoc_symboles.get(f'bouton{boutons_gauche.index(gauche) + 1}')
                    sym_droite = assoc_symboles.get(f'bouton{boutons_droite.index(droite) + 6}')
                    if [sym_gauche, sym_droite] in symboles or [sym_droite, sym_gauche] in symboles:
                        print(f"✅ {sym_gauche} connecté à {sym_droite} — Correct")
                    else:
                        print(f"❌ {sym_gauche} connecté à {sym_droite} — Incorrect")
                        explosion_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/explosion_finale.jpg') 
                        explosion_image = pygame.transform.scale(explosion_image, (100, 100))
                        fenetre.blit(explosion_image, (250, 150))

    
    # Remplir l'écran
    fenetre.fill((255, 255, 255))
    
    # Dessiner les boutons
    pygame.draw.rect(fenetre, (0, 0, 0), bouton1)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton2)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton3)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton4)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton5)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton6)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton7)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton8)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton9)
    pygame.draw.rect(fenetre, (0, 0, 0), bouton10)
    
    for b1, b2 in connexions: # Dessiner les fils entre les boutons connectés
        x1, y1 = b1.center
        x2, y2 = b2.center
        pygame.draw.line(fenetre, (0, 0, 255), (x1, y1), (x2, y2), 3)

    # Dessiner le bouton de vérification
    pygame.draw.rect(fenetre, (0, 100, 0), bouton_verification) # couleur
    font = pygame.font.Font(None, 24)
    texte_verif = font.render("Vérifier", True, (255, 255, 255))
    fenetre.blit(texte_verif, (bouton_verification.x + 10, bouton_verification.y + 10))

    # Afficher les images sur les boutons
    fenetre.blit(image_bouton1, bouton1)
    fenetre.blit(image_bouton2, bouton2)
    fenetre.blit(image_bouton3, bouton3)
    fenetre.blit(image_bouton4, bouton4)
    fenetre.blit(image_bouton5, bouton5)
    fenetre.blit(image_bouton6, bouton6)
    fenetre.blit(image_bouton7, bouton7)
    fenetre.blit(image_bouton8, bouton8)
    fenetre.blit(image_bouton9, bouton9)
    fenetre.blit(image_bouton10, bouton10)

    # Mettre à jour l'affichage
    pygame.display.flip()


    # Dessiner une barre de titre en haut
    pygame.draw.rect(fenetre, (220, 220, 220), (0, 0, 600, 40))  # barre grise

    # Afficher le titre du jeu
    font_titre = pygame.font.Font(None, 32)
    texte_titre = font_titre.render("yo", True, (0, 0, 0))
    fenetre.blit(texte_titre, (10, 10))

    # Dessiner un onglet à côté du titre
    pygame.draw.rect(fenetre, (180, 180, 180), (120, 5, 100, 30), border_radius=8)
    texte_onglet = font_titre.render("Onglet", True, (0, 0, 0))
    fenetre.blit(texte_onglet, (130, 10))



pygame.quit()