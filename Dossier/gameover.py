import pygame
import time
import sys
import subprocess

def afficher_gameover(screen):
    pygame.font.init()
    font_big = pygame.font.Font(None, 80)  # Police grande pour "Game Over"
    font_small = pygame.font.Font(None, 40)  # Police plus petite pour le compte à rebours

    # Couleur de fond et texte
    screen.fill((0, 0, 0))  # Fond noir
    message = font_big.render("Game Over", True, (255, 0, 0))  # "Game Over" en rouge
    sous_texte = font_small.render("Nouvelle partie dans 5 secondes...", True, (255, 255, 255))  # Texte de compte à rebours en blanc

    # Positionner les éléments au centre
    screen.blit(message, message.get_rect(center=(400, 250)))
    screen.blit(sous_texte, sous_texte.get_rect(center=(400, 350)))
    pygame.display.flip()

    # Compte à rebours de 5 secondes
    countdown = 5  # Compte à rebours de 5 secondes
    start_ticks = pygame.time.get_ticks()  # Récupérer le temps de départ

    while countdown > 0:
        # Calculer le temps écoulé
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Temps écoulé en secondes

        # Si une seconde est passée, mettre à jour le compte à rebours
        if seconds >= 1:
            countdown -= 1
            start_ticks = pygame.time.get_ticks()  # Redémarrer le chronomètre

        # Afficher le temps restant
        countdown_text = font_small.render(f"Recommence dans {countdown}s", True, (255, 255, 255))
        screen.fill((0, 0, 0))  # Remplir l'écran de noir à chaque itération
        screen.blit(message, message.get_rect(center=(400, 250)))  # Ré-afficher "Game Over"
        screen.blit(countdown_text, (350, 450))  # Afficher le texte du compte à rebours
        pygame.display.update()  # Mettre à jour l'affichage

        # Gérer les événements (permettre de quitter proprement)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # À la fin du compte à rebours, rediriger vers le menu
    rediriger_vers_menu()

def rediriger_vers_menu():
    pygame.quit()  # Fermer pygame proprement
    time.sleep(1)  # Petite pause pour s'assurer que pygame se ferme avant de lancer un nouveau processus
    subprocess.call(['python3', 'menu.py'])  # Lancer le script menu.py
    sys.exit()  # Quitter l'actuel script pour que le menu s'affiche proprement
