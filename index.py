import pygame
import random
import time

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hacker Terminal")

# Couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# Police
font = pygame.font.Font(pygame.font.match_font('courier'), 20)

# Mot de passe et tentatives
passwords = ["shadow", "access", "matrix", "glitch", "cyber", "neon"]
password = random.choice(passwords)
attempts = 5

time_limit = 90  # 1 min 30 sec
start_time = time.time()

# Historique des messages
terminal_lines = []
input_text = ""

# Messages de démarrage
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

def draw_terminal():
    screen.fill(BLACK)
    y_offset = 20
    for line in terminal_lines[-20:]:  # Afficher les 20 dernières lignes
        text_surface = font.render(line, True, GREEN)
        screen.blit(text_surface, (10, y_offset))
        y_offset += 25
    
    # Afficher le texte entré
    input_surface = font.render("> " + input_text, True, GREEN)
    screen.blit(input_surface, (10, HEIGHT - 40))
    
    # Afficher le minuteur
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, time_limit - elapsed_time)
    timer_surface = font.render(f"Temps restant : {remaining_time}s", True, DARK_GREEN)
    screen.blit(timer_surface, (WIDTH - 250, 10))
    
    pygame.display.flip()

def add_terminal_line(text):
    terminal_lines.append(text)

def boot_sequence():
    for msg in boot_messages:
        add_terminal_line(msg)
        draw_terminal()
        time.sleep(random.uniform(0.2, 0.5))
    add_terminal_line("")

# Lancer la séquence de démarrage
boot_sequence()

def show_hacked_window():
    hacked_screen = pygame.display.set_mode((500, 300))
    hacked_screen.fill(BLACK)
    hacked_font = pygame.font.Font(pygame.font.match_font('courier'), 30)
    hacked_text = hacked_font.render("Accès aux caméras obtenu !", True, GREEN)
    hacked_screen.blit(hacked_text, (50, 130))
    pygame.display.flip()
    time.sleep(3)

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
            response = "Accès autorisé ! Vous avez piraté le système ! 🔓"
            draw_terminal()
            show_hacked_window()
            pygame.quit()
            exit()
        else:
            attempts -= 1
            response = f"Accès refusé ! Tentatives restantes : {attempts}" if attempts > 0 else f"Échec du hack ! Le mot de passe était : {password}"
            if attempts == 0:
                pygame.quit()
                exit()
    else:
        response = "Commande invalide. Utilisez : hint, list, hack [mot]"
    
    add_terminal_line(response)

def main():
    global input_text
    running = True
    clock = pygame.time.Clock()
    
    while running:
        draw_terminal()
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            add_terminal_line("Temps écoulé ! Échec du hack !")
            pygame.quit()
            exit()
        
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