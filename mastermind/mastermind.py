
import random
import pygame

# Génère un code secret aléatoire de 4 chiffres entre 0 et 9
def code1():
    return [random.randint(0, 9) for _ in range(4)]

# Code secret global
globcode = code1()

# Compare une tentative (globbornes) avec le code secret (globcode)
# Retourne le nombre de chiffres bien placés et mal placés
def compare(globbornes, globcode):
    Bon_endroit = sum(1 for a, b in zip(globbornes, globcode) if a == b) # Chiffres bien placés
    Mauvais_endroit = sum(min(globbornes.count(n), globcode.count(n)) for n in set(globcode)) - Bon_endroit # Chiffres mal placés
    return Bon_endroit, Mauvais_endroit

# Fonction principale du jeu
def main():
    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # Crée une fenêtre de 800x600 pixels
    pygame.display.set_caption("Crack the Code") # Définit le titre de la fenêtre
    
    # Définition des couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    font = pygame.font.Font(None, 50) # Police pour le texte
    
    # Définition de la boîte de saisie
    input_box = pygame.Rect(300, 200, 200, 50)  # Rectangle pour la saisie
    color_active, color_inactive = WHITE, GRAY # Couleurs pour la boîte active/inactive
    color = color_inactive # Couleur initiale
    active = False # Indique si la boîte est active
    text = "" # Texte saisi par l'utilisateur
    message = "" # Message affiché après une tentative
    historique = [] # Historique des tentatives
    
    running = True # Boucle principale du jeu
    while running:
        screen.fill(BLACK)  # Remplit l'écran avec la couleur noire
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique
                # Active la boîte si le clic est à l'intérieur
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN and active: # Si une touche est pressée et la boîte active
                if event.key == pygame.K_RETURN: # Si l'utilisateur appuie sur Entrée
                    if len(text) == 4 and text.isdigit(): # Vérifie que l'entrée est un nombre à 4 chiffres
                        guess = [int(ch) for ch in text] # Convertit le texte en liste d'entiers
                        bon, mauvais = compare(guess, globcode)  # Compare la tentative avec le code secret
                        message = f"{bon} bien placé, {mauvais} mal placé" # Message de résultat
                        message1 = f"{text} : {bon} bien placé, {mauvais} mal placé" # Ajoute à l'historique
                        historique.append(message1)
                        if bon == 4: # Si tous les chiffres sont bien placés
                            message = "Bravo, code trouvé !" # Message de victoire
                    text = ""  # Réinitialise le texte
                elif event.key == pygame.K_BACKSPACE: # Si l'utilisateur appuie sur Retour arrière
                    text = text[:-1] # Supprime le dernier caractère
                else:
                    if len(text) < 4 and event.unicode.isdigit(): # Limite à 4 chiffres et accepte uniquement des nombres
                        text += event.unicode # Ajoute le caractère saisi
        
        # Dessine la boîte de saisie
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, WHITE) # Rend le texte saisi
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10)) # Affiche le texte dans la boîte
        
        # Affiche le message de résultat
        msg_surface = font.render(message, True, WHITE)
        screen.blit(msg_surface, (200, 250))
        
         # Affiche les 5 dernières tentatives
        y_offset = 300
        for past_guess in historique[-5:]:
            past_surface = font.render(past_guess, True, WHITE)
            screen.blit(past_surface, (200, y_offset))
            y_offset += 30
        
        # Met à jour l'affichage
        pygame.display.flip()
    
    # Quitte Pygame
    pygame.quit()

# Point d'entrée du programme
if __name__ == "__main__":
    main()
