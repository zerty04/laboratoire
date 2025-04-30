import pygame
import sys
from time import sleep


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

connexions = [] #la lliste qui va contenir les paires de boutons

bouton_selectionne = None

onglet_actif = "Fils"  # on commence sur longlet Fils
rect_onglet_fils = pygame.Rect(3, 5, 75, 30)      #zone cliquable pour revenir à "Fils"
rect_onglet_carnet = pygame.Rect(730, 10, 45, 20)  #rectangle du bouton "Carnet" (qui est caché)
   
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

GameOver_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/GameOver.jpg')
GameOver_image = pygame.transform.scale(GameOver_image, (800, 600))
GameOver_visible = False

mission_passed_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/mission_passed.jpg') 
mission_passed_image = pygame.transform.scale(mission_passed_image, (600, 600))
mission_passed_visible = False

timer = 0 

bouton_verification = pygame.Rect(250, 50, 80, 40) 
bouton_reinitialiser = pygame.Rect(350, 50, 110, 40)
bouton_indice = pygame.Rect(480, 50, 60, 40)
bouton_OK = pygame.Rect(380, 320, 60, 40)


afficher_bouton_indice = True
afficher_indice = False

bouton_onglet = pygame.Rect(120, 5, 100, 30)


afficher_bouton_OK = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # on ferme la fenetre si on clique sur la croix 
            running = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_onglet_fils.collidepoint(event.pos):
                onglet_actif = "Fils"
            elif rect_onglet_carnet.collidepoint(event.pos):
                onglet_actif = "Carnet"

            pos = event.pos

            if onglet_actif in "Fils":
                for b in boutons_gauche: # Vérifier si clic sur un bouton de gauche
                    if b.collidepoint(pos):
                        bouton_selectionne = b  # Sélectionne un bouton de gauche
                        break
                else:  # Si pas de bouton gauche, on vérifie bouton droite
                    for b in boutons_droite:
                        if b.collidepoint(pos) and bouton_selectionne:
                            nouvelle_connexion = (bouton_selectionne, b)
                            if nouvelle_connexion in connexions or (b, bouton_selectionne) in connexions:
                                print("Connexion déjà effectuée !")
                            else:
                                connexions.append((bouton_selectionne, b))  #on ajoute la paire de bouton a la liste de connexion
                                bouton_selectionne = None 
                                break

                # Vérification du bouton de vérification
                if bouton_reinitialiser.collidepoint(pos):
                    print("Réinitialisation des connexions...")
                    connexions.clear()
                elif bouton_indice.collidepoint(pos): #on affiche un message d'indice au cas ou le joueur est nul
                    afficher_bouton_indice = False
                    afficher_indice = True
                elif bouton_OK.collidepoint(pos): #on cache le bouton ok ET le message (expliqué plus bas)
                    afficher_bouton_OK = False
                elif bouton_verification.collidepoint(pos):
                    print("Vérification des connexions...")
                    explosion_visible = False
                    mission_passed = False
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
                            explosion_image = pygame.transform.scale(explosion_image, (500, 500))
                            fenetre.blit(explosion_image, (150, -20))
                            timer = pygame.time.get_ticks() + 2000
                            pygame.display.flip()
                            sleep(3)
                            GameOver_visible = True
                            GameOver_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/GameOver.jpg')
                            GameOver_image = pygame.transform.scale(GameOver_image, (800, 600))
                            fenetre.blit(GameOver_image, (0, -50))
                            timer = pygame.time.get_ticks() + 2000
                            pygame.display.flip()
                            sleep(4)
                            pygame.quit()
                            sys.exit()

                    connexions.clear() 
                    bouton_selectionne = None  

                    if connexions_correctes == 5 and connexion_incorrecte == False:
                        mission_passed_visible = True
                        print("🎉 Toutes les connexions sont correctes ! Fin du jeu.")
                        mission_passed_image = pygame.image.load('C:/Documents/ISEP/Projet Info S2/mission_passed.jpg') 
                        mission_passed_image = pygame.transform.scale(mission_passed_image, (800, 600))
                        fenetre.blit(mission_passed_image, (0, 0)) 
                        timer = pygame.time.get_ticks() + 2000
                        pygame.display.flip()
                        sleep(3)
                        pygame.quit()
                        sys.exit()

    
                        
    # Remplir tout l'écran
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

    for b1, b2 in connexions: # Dessiner les fils
        x1, y1 = b1.center
        x2, y2 = b2.center
        pygame.draw.line(fenetre, (0, 0, 255), (x1, y1), (x2, y2), 3)

    #bouton de vérification
    pygame.draw.rect(fenetre, (0, 100, 0), bouton_verification) # couleur
    font = pygame.font.Font(None, 24)
    texte_verif = font.render("Vérifier", True, (255, 255, 255)) 
    fenetre.blit(texte_verif, (bouton_verification.x + 10, bouton_verification.y + 10)) 

    #bouton de vreinitialisation
    pygame.draw.rect(fenetre, (100, 0, 0), bouton_reinitialiser)
    texte_reinit = font.render("Réinitialiser", True, (255, 255, 255))
    fenetre.blit(texte_reinit, (bouton_reinitialiser.x + 5, bouton_reinitialiser.y + 10))

    #bouton indice
    pygame.draw.rect(fenetre, (200, 200, 0), bouton_indice)
    texte_indice = font.render("Indice", True, (255, 255, 255))
    fenetre.blit(texte_indice, (bouton_indice.x + 5, bouton_indice.y + 10))
    
    
    if afficher_indice:
        font = pygame.font.Font(None, 18)
        texte_surface = font.render("Essayez de détacher vos", True, (0, 0, 0)) 
        fenetre.blit(texte_surface, (560, 50))
        texte_surface = font.render("yeux de ces symboles", True, (0, 0, 0)) 
        fenetre.blit(texte_surface, (560, 65)) 
        

    pygame.draw.rect(fenetre, (220, 220, 220), (0, 0, 800, 40))  # barre grise du haut
    font = pygame.font.Font(None, 27)
    texte_surface = font.render("Reconnectez les fils", True, (0, 0, 0)) 
    fenetre.blit(texte_surface, (120, 12))

    
    if afficher_bouton_OK: # en gros ici on supprime le bouton ok et le texte si on clique dessus par le afficher bouton ok = True
        pygame.draw.rect(fenetre, (0, 180, 0), bouton_OK)
        texte_OK = font.render("OK !", True, (255, 255, 255))
        fenetre.blit(texte_OK, (bouton_OK.x + 12, bouton_OK.y + 12))

        font = pygame.font.Font(None, 27)
        texte_surface = font.render("Le cablage des fils a été saboté !", True, (0, 0, 0)) 
        fenetre.blit(texte_surface, (250, 250))
        font = pygame.font.Font(None, 27)
        texte_surface = font.render("Reconnectez-les pour ouvrir la porte !", True, (0, 0, 0)) 
        fenetre.blit(texte_surface, (230, 280))


    font_titre = pygame.font.Font(None, 32)

    # Onglet Fils
    couleur_fils = (100, 100, 100) if onglet_actif == "Fils" else (220, 220, 220)
    pygame.draw.rect(fenetre, couleur_fils, rect_onglet_fils, border_radius=8)
    texte_fils = font_titre.render("Fils", True, (0, 0, 0))
    fenetre.blit(texte_fils, (rect_onglet_fils.x + 15, rect_onglet_fils.y + 5))

    # Onglet du Carnet
    couleur_carnet = (100, 100, 100) if onglet_actif == "Carnet" else (220, 220, 220)
    pygame.draw.rect(fenetre, couleur_carnet, rect_onglet_carnet, border_radius=8)
    ma_police = pygame.font.SysFont('Georgia', 10)
    texte_carnet_onglet = ma_police.render("S e c r e t", True, (0, 0, 0))
    fenetre.blit(texte_carnet_onglet, (rect_onglet_carnet.x + 5, rect_onglet_carnet.y + 5))

    for b1, b2 in connexions:
            x1, y1 = b1.center
            x2, y2 = b2.center
            pygame.draw.line(fenetre, (0, 0, 255), (x1, y1), (x2, y2), 3)

    if onglet_actif == "Carnet":
        pygame.draw.rect(fenetre, (240, 240, 250), (0, 40, 800, 460))  # Fond de la page
        texte_page = font_titre.render("On dirait que vous avez trouvé le carnet du professeur...", True, (0, 0, 0)) 
        fenetre.blit(texte_page, (100, 65)) 
        font_carnet = pygame.font.Font(None, 28)
        y_offset = 150 
        for ligne in texte_carnet:
            rendu = font_carnet.render(ligne, True, (20, 20, 60))
            fenetre.blit(rendu, (30, y_offset))
            y_offset += 32  #interligne 

        # Cacher l’explosion après 2 secondes
    if explosion_visible and pygame.time.get_ticks() > timer:
        explosion_visible = False

        # on affiche lexplosion si elle est True
    if explosion_visible:
        fenetre.blit(explosion_image, (250, 150))

        # met a jour l'affichage à linfini
    pygame.display.flip()

pygame.quit()