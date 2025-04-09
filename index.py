# ===============================
# HACKER TERMINAL - PYGAME EDITION
# ===============================

import pygame
import random
import time

# INITIALISATION DE PYGAME
pygame.init()


# PARAMÈTRES DE LA FENÊTRE
WIDTH, HEIGHT = 1024, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hacker Terminal")


# COULEURS UTILISÉES
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
WHITE = (255, 255, 255)


# POLICE 
font = pygame.font.Font(pygame.font.match_font('courier'), 20)

# ===============================
# CONFIGURATION DU MOT DE PASSE
# ===============================
passwords = ["shadow", "access", "matrix", "glitch", "cyber", "neon"]
password = random.choice(passwords)
attempts = 3  # Nombre de tentatives restantes


# TIMER GLOBAL
time_limit = 90  # 1min30
start_time = time.time()


# VARIABLES 
terminal_lines = []  # Historique des lignes dans le terminal
input_text = ""      # Texte actuellement tapé par l'utilisateur

# ===============================
# CHARGEMENT DE L’IMAGE "CAMÉRA"
# ===============================
camera_image = pygame.image.load("camera.png")
camera_image = pygame.transform.scale(camera_image, (WIDTH, HEIGHT))


# MESSAGES DE DÉMARRAGE (FAKE BOOT SEQUENCE)
boot_messages = [
    "Initializing system...",
    "Loading kernel modules...",
    "Connecting to secure server...",
    "Decrypting classified data...",
    "Accessing restricted files...",
    "Running security protocols...",
    "No intrusions detected.",
    "System ready. Awaiting command...",
]


# FONCTION : AFFICHAGE DU TERMINAL
def draw_terminal():
    screen.fill(BLACK)
    y_offset = 20
    
    # Affiche les dernières lignes (20 max)
    for line in terminal_lines[-20:]:
        text_surface = font.render(line, True, GREEN)
        screen.blit(text_surface, (10, y_offset))
        y_offset += 25
    
    # Affiche l'entrée utilisateur
    input_surface = font.render("> " + input_text, True, GREEN)
    screen.blit(input_surface, (10, HEIGHT - 40))
    
    # Affiche le chrono
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, time_limit - elapsed_time)
    timer_surface = font.render(f"Temps restant : {remaining_time}s", True, DARK_GREEN)
    screen.blit(timer_surface, (WIDTH - 250, 10))
    
    pygame.display.flip()

# ===============================
# AJOUTER UNE LIGNE DANS LE TERMINAL
# ===============================
def add_terminal_line(text):
    terminal_lines.append(text)


# FAKE BOOT SEQUENCE AVANT JEU
def boot_sequence():
    for msg in boot_messages:
        add_terminal_line(msg)
        draw_terminal()
        time.sleep(random.uniform(0.2, 0.5))
    add_terminal_line("")

# Lancer la séquence de démarrage au début
boot_sequence()

# ===============================
# ANIMATION DE "HACK EN COURS..."
# ===============================
def hacking_animation():
    screen.fill(BLACK)
    for i in range(10):
        text_surface = font.render("HACKING...", True, GREEN if i % 2 == 0 else DARK_GREEN)
        screen.blit(text_surface, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(0.3)
    
    # Message de réussite
    screen.fill(BLACK)
    text_surface = font.render("ACCÈS AUX CAMÉRAS OBTENU", True, GREEN)
    screen.blit(text_surface, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)
    show_camera_feed()

# ===============================
# AFFICHAGE DE L'IMAGE "CAMÉRA"
# ===============================
def show_camera_feed():
    screen.blit(camera_image, (0, 0))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    exit()

# ===============================
# COMMANDES UTILISATEUR
# ===============================
def process_command(command):
    global attempts, input_text
    command = command.strip().lower()
    add_terminal_line("> " + command)
    
    if command == "hint":
        response = f"Le mot de passe commence par '{password[0]}' et contient {len(password)} lettres."
    
    elif command == "list":
        response = "Mots possibles : " + ", ".join(passwords)
    
    elif command.startswith("hack "):
        attempt = command.split(" ", 1)[1]
        if attempt == password:
            add_terminal_line("Accès autorisé ! Vous avez piraté le système ! 🔓")
            draw_terminal()
            hacking_animation()
        else:
            attempts -= 1
            response = f"Accès refusé ! Tentatives restantes : {attempts}" if attempts > 0 else f"Échec du hack ! Le mot de passe était : {password}"
            if attempts == 0:
                pygame.quit()
                exit()
    
    else:
        response = "Commande invalide. Utilisez : hint, list, hack [mot]"
    
    add_terminal_line(response)

# ===============================
# FONCTION PRINCIPALE DU JEU
# ===============================
def main():
    global input_text
    running = True
    clock = pygame.time.Clock()
    
    while running:
        draw_terminal()
        
        # Chrono terminé ?
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            add_terminal_line("Temps écoulé ! Échec du hack !")
            pygame.quit()
            exit()
        
        # Gestion des événements clavier
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process_command(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        clock.tick(30)
    
    pygame.quit()
main()