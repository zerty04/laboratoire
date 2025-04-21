import pygame
import sys


symboles = (
    ["🧪", "🪨"],
    ["🔥", "💥"],
    ["🪨", "💎"],
    ["💧", "☁️"],
    ["🌋", "🌱"]

)

assoc_symboles = {
    'bouton1': "🌋",
    'bouton2': "🪨",
    'bouton3': "🧪",
    'bouton4': "🔥",
    'bouton5': "💧",
    'bouton6': "🪨",
    'bouton7': "☁️",
    'bouton8': "🌱",
    'bouton9': "💥",
    'bouton10': "💎",
}

connexions = [] 
connexions_fils = []

bouton_selectionne = None

onglet_actif = "Fils"  # Par défaut, on commence sur l'onglet Fils
rect_onglet_fils = pygame.Rect(3, 5, 75, 30)      # zone cliquable pour revenir à "Fils"
rect_onglet_carnet = pygame.Rect(730, 10, 45, 20)  # rectangle du bouton "Carnet"
   
texte_carnet = [
    "Une simple goutte d’un acide inconnu, et ma roche se dissout instantanément.",
    "Quelle puissance ! Un simple coup de feu sur cette poudre blanche... et BOUM !",
    "Mes sourcils ont disparu.",
    "J'ai trouvé une roche terne, insignifiante. Je l'ai soumise à une pression",
    "titanesque... et en ai extraitune pure merveille !",
    "L'eau bout, puis disparaît en vapeur... mais en la capturant elle se fige",
    "de nouveau en gouttelettes.",
    "Le cycle est éternel.",
    "Des cendres noires et fines après la combustion… et si elles contenaient la",
    "clé d’une nouvelle création ?"
]

pygame.init()

fenetre = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Fils électriques")

bouton1 = pygame.Rect(40, 80, 50, 50) 
bouton2 = pygame.Rect(40, 159, 50, 50)
bouton3 = pygame.Rect(40, 245, 50, 50)
bouton4 = pygame.Rect(40, 325, 50, 50)
bouton5 = pygame.Rect(40, 410, 50, 50)

bouton6 = pygame.Rect(700, 80, 50, 50)
bouton7 = pygame.Rect(700, 159, 50, 50)
bouton8 = pygame.Rect(700, 245, 50, 50)
bouton9 = pygame.Rect(700, 325, 50, 50)
bouton10 = pygame.Rect(700, 410, 50, 50)


boutons_gauche = [bouton1, bouton2, bouton3, bouton4, bouton5]
boutons_droite = [bouton6, bouton7, bouton8, bouton9, bouton10]


# Images
image_bouton1 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/volcan.jpg')
image_bouton1 = pygame.transform.scale(image_bouton1, (50, 50))
image_bouton2 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/pierre.jpg')
image_bouton2 = pygame.transform.scale(image_bouton2, (50, 50))
image_bouton3 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/tube_a_essai.jpg')
image_bouton3 = pygame.transform.scale(image_bouton3, (50, 50))
image_bouton4 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/feu.jpg')
image_bouton4 = pygame.transform.scale(image_bouton4, (50, 50))
image_bouton5 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/eau.jpg')
image_bouton5 = pygame.transform.scale(image_bouton5, (50, 50))


image_bouton6 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/pierre.jpg')
image_bouton6 = pygame.transform.scale(image_bouton6, (50, 50))
image_bouton7 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/nuage.jpg')
image_bouton7 = pygame.transform.scale(image_bouton7, (50, 50))
image_bouton8 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/plante.jpg')
image_bouton8 = pygame.transform.scale(image_bouton8, (50, 50))
image_bouton9 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/explosion.jpg')
image_bouton9 = pygame.transform.scale(image_bouton9, (50, 50))
image_bouton10 = pygame.image.load('C:/Documents/ISEP/Projet Info S2/diamant.jpg')
image_bouton10 = pygame.transform.scale(image_bouton10, (50, 50))





explosion_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/explosion_finale.jpg') 
explosion_image = pygame.transform.scale(explosion_image, (100, 100))
explosion_visible = False
explosion_timer = 0  # Temps jusqu’à ce que l’explosion disparaisse


bouton_verification = pygame.Rect(350, 50, 80, 40) 
bouton_onglet = pygame.Rect(120, 5, 100, 30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si on clique sur la croix (X)
            running = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_onglet_fils.collidepoint(event.pos):
                onglet_actif = "Fils"
            elif rect_onglet_carnet.collidepoint(event.pos):
                onglet_actif = "Carnet"

            pos = event.pos

            if onglet_actif in "Fils":
                # Vérifier si clic sur un bouton de gauche
                for b in boutons_gauche:
                    if b.collidepoint(pos):
                        bouton_selectionne = b  # Sélectionner bouton gauche
                        break
                else:  # Si pas de bouton gauche, on vérifie bouton droite
                    for b in boutons_droite:
                        if b.collidepoint(pos) and bouton_selectionne:
                            nouvelle_connexion = (bouton_selectionne, b)
                            if nouvelle_connexion in connexions or (b, bouton_selectionne) in connexions:
                                print("Connexion déjà effectuée !")
                            else:
                                connexions.append((bouton_selectionne, b))  # Connexion 
                                bouton_selectionne = None 
                                break

                # Vérification du bouton de vérification
                if bouton_verification.collidepoint(pos):
                    print("Vérification des connexions...")
                    explosion_visible = False
                    connexions_correctes = 0
                    connexion_incorrecte = False
                    for gauche, droite in connexions:
                        sym_gauche = assoc_symboles.get(f'bouton{boutons_gauche.index(gauche) + 1}')
                        sym_droite = assoc_symboles.get(f'bouton{boutons_droite.index(droite) + 6}')
                        if [sym_gauche, sym_droite] in symboles or [sym_droite, sym_gauche] in symboles:
                            print(f"✅ {sym_gauche} connecté à {sym_droite} — Correct")
                            connexions_correctes += 1
                        else:
                            print(f"❌ {sym_gauche} connecté à {sym_droite} — Incorrect")
                            connexion_incorrecte = True
                            explosion_visible = True
                            explosion_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/explosion_finale.jpg') 
                            explosion_image = pygame.transform.scale(explosion_image, (250, 250))
                            fenetre.blit(explosion_image, (0, 150))
                            explosion_timer = pygame.time.get_ticks() + 2000
                    connexions.clear()  # Réinitialiser les connexions après vérification   
                    bouton_selectionne = None  # Réinitialiser la sélection après vérification
                    print(connexions_correctes)

                    if connexions_correctes == 5 and connexion_incorrecte == False:
                        print("🎉 Toutes les connexions sont correctes ! Fin du jeu.")
                        pygame.quit()
                        sys.exit()

    
                        
    # Remplir l'écran
    fenetre.fill((255, 255, 255))

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

    for b1, b2 in connexions: # Dessiner les fils entre les boutons connectés
        x1, y1 = b1.center
        x2, y2 = b2.center
        pygame.draw.line(fenetre, (0, 0, 255), (x1, y1), (x2, y2), 3)

    #Dessiner le bouton de vérification
    pygame.draw.rect(fenetre, (0, 100, 0), bouton_verification) # couleur
    font = pygame.font.Font(None, 24)
    texte_verif = font.render("Vérifier", True, (255, 255, 255)) 
    fenetre.blit(texte_verif, (bouton_verification.x + 10, bouton_verification.y + 10)) 


    # Dessin de la barre d'onglets
    pygame.draw.rect(fenetre, (220, 220, 220), (0, 0, 800, 40))  # barre grise du haut

    font_titre = pygame.font.Font(None, 32)

    # Onglet Fils
    couleur_fils = (100, 100, 100) if onglet_actif == "Fils" else (220, 220, 220)
    pygame.draw.rect(fenetre, couleur_fils, rect_onglet_fils, border_radius=8)
    texte_fils = font_titre.render("Fils", True, (0, 0, 0))
    fenetre.blit(texte_fils, (rect_onglet_fils.x + 15, rect_onglet_fils.y + 5))

    # Onglet Carnet
    couleur_carnet = (100, 100, 100) if onglet_actif == "Carnet" else (220, 220, 220)
    pygame.draw.rect(fenetre, couleur_carnet, rect_onglet_carnet, border_radius=8)
    ma_police = pygame.font.Font(None, 16) #police de la page secrete
    texte_carnet_onglet = ma_police.render("Secret", True, (0, 0, 0))
    fenetre.blit(texte_carnet_onglet, (rect_onglet_carnet.x + 5, rect_onglet_carnet.y + 5))

    for b1, b2 in connexions_fils:
            x1, y1 = b1.center
            x2, y2 = b2.center
            pygame.draw.line(fenetre, (0, 0, 255), (x1, y1), (x2, y2), 3)

        # Affichage de la page du carnet si l'onglet actif est Carnet
    if onglet_actif == "Carnet":
        pygame.draw.rect(fenetre, (240, 240, 250), (0, 40, 800, 460))  # Fond de la page
        texte_page = font_titre.render("On dirait que vous avez trouvé le carnet du professeur...", True, (0, 0, 0)) 
        fenetre.blit(texte_page, (100, 65)) 
        font_carnet = pygame.font.Font(None, 28)  # Police du texte du carnet
        y_offset = 150  # Position verticale de départ
        for ligne in texte_carnet:
            rendu = font_carnet.render(ligne, True, (20, 20, 60))  # Création du texte
            fenetre.blit(rendu, (30, y_offset))  # Affichage du texte
            y_offset += 32  # Espacement entre chaque ligne de texte

        # Cacher l’explosion après 2 secondes
    if explosion_visible and pygame.time.get_ticks() > explosion_timer:
        explosion_visible = False

        # Afficher l’explosion si active
    if explosion_visible:
        fenetre.blit(explosion_image, (250, 150))

        # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
