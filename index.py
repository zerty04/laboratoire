# ===============================
# HACKER TERMINAL - PYGAME EDITION
# ===============================

import pygame
import random
import time

# ===============================
# CONFIGURATION DU MOT DE PASSE
# ===============================
passwords = ["shadow", "access", "matrix", "glitch", "cyber", "neon"]
password = random.choice(passwords)
attempts = 3  # Nombre de tentatives

# ===============================
# INITIALISATION
# ===============================
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hacker Terminal")

# ===============================
# COULEURS & POLICE
# ===============================
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(pygame.font.match_font('courier'), 20)

# ===============================
# CHARGEMENT IMAGE
# ===============================
camera_image = pygame.image.load("camera.png")
camera_image = pygame.transform.scale(camera_image, (WIDTH, HEIGHT))

# ===============================
# VARIABLES GLOBALES
# ===============================
input_text = ""
terminal_lines = []
start_time = time.time()
time_limit = 90  # secondes

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

# ===============================
# FONCTIONS VISUELLES
# ===============================
def draw_terminal():
    screen.fill(BLACK)
    y_offset = 20

    for line in terminal_lines[-20:]:
        surface = font.render(line, True, GREEN)
        screen.blit(surface, (10, y_offset))
        y_offset += 25

    input_surface = font.render("> " + input_text, True, GREEN)
    screen.blit(input_surface, (10, HEIGHT - 40))

    remaining_time = max(0, time_limit - int(time.time() - start_time))
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

def hacking_animation():
    screen.fill(BLACK)
    for i in range(10):
        txt = font.render("HACKING...", True, GREEN if i % 2 == 0 else DARK_GREEN)
        screen.blit(txt, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(0.3)

    screen.fill(BLACK)
    success = font.render("ACCÈS AUX CAMÉRAS OBTENU", True, GREEN)
    screen.blit(success, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)
    show_camera_feed()

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
        guess = command.split(" ", 1)[1]
        if guess == password:
            add_terminal_line("Accès autorisé ! Vous avez piraté le système ! 🔓")
            draw_terminal()
            hacking_animation()
        else:
            attempts -= 1
            response = f"Accès refusé ! Tentatives restantes : {attempts}"
            if attempts == 0:
                add_terminal_line(f"Échec du hack ! Le mot de passe était : {password}")
                draw_terminal()
                time.sleep(3)
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
    clock = pygame.time.Clock()
    running = True

    boot_sequence()

    while running:
        draw_terminal()

        if time.time() - start_time >= time_limit:
            add_terminal_line("Temps écoulé ! Échec du hack !")
            draw_terminal()
            time.sleep(3)
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

# ===============================
# POINT D’ENTRÉE DU JEU
# ===============================
def run():
    main()

if __name__ == "__main__":
    run()
