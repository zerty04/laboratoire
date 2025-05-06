import pygame
import sys
import subprocess

# Initialisation
pygame.init()
pygame.mixer.init()

# Paramètres écran
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini-Jeux - Menu Principal")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
HOVER_COLOR = (100, 100, 255)

# Polices
FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 24)

# Charger une image de fond
background = pygame.image.load("background.jpg")  # Mets ton image dans le dossier
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Bouton classe
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = DARK_GRAY
        self.hovered = False

    def draw(self, screen):
        pygame.draw.rect(screen, HOVER_COLOR if self.hovered else self.color, self.rect, border_radius=10)
        text_surf = FONT.render(self.text, True, WHITE)
        screen.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
                                self.rect.y + (self.rect.height - text_surf.get_height()) // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.callback()

# État du menu
show_rules = False

# Fonctions des boutons
def start_game():
    print("Lancement du jeu...")
    pygame.quit()  # Fermer la fenêtre du menu
    try:
        # Remplacer par ton script de jeu (par exemple, main.py)
        subprocess.run(["python", "main.py"], check=True)
        print("✅ Script lancé avec succès !")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du lancement du script : {e}")

def show_rules_screen():
    global show_rules
    show_rules = True

def quit_game():
    pygame.quit()
    sys.exit()

def back_to_menu():
    global show_rules
    show_rules = False

# Création des boutons
buttons = [
    Button("Start", WIDTH // 2 - 100, 200, 200, 60, start_game),
    Button("Rules", WIDTH // 2 - 100, 300, 200, 60, show_rules_screen),
    Button("Quit", WIDTH // 2 - 100, 400, 200, 60, quit_game)
]

back_button = Button("Back", 20, 20, 100, 50, back_to_menu)

# Texte des règles
rules_text = [
    "Bienvenue dans le projet Mini-Jeux !",
    "Voici quelques règles générales :",
    "- Utilise la souris ou le clavier selon le jeu.",
    "- Chaque mini-jeu a ses propres instructions.",
    "- Amuse-toi et essaie de battre les meilleurs scores !"
]

# Boucle principale
def main_menu():
    clock = pygame.time.Clock()
    while True:
        SCREEN.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if show_rules:
                back_button.handle_event(event)
            else:
                for button in buttons:
                    button.handle_event(event)

        if show_rules:
            SCREEN.fill((20, 20, 20))  # Écran de règles
            y_offset = 100
            for line in rules_text:
                rule_surf = SMALL_FONT.render(line, True, WHITE)
                SCREEN.blit(rule_surf, ((WIDTH - rule_surf.get_width()) // 2, y_offset))
                y_offset += 40
            back_button.draw(SCREEN)
        else:
            for button in buttons:
                button.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_menu()
