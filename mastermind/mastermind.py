import random
import pygame

def code1():
    return [random.randint(0, 9) for _ in range(4)]

globcode = code1()

def compare(globbornes, globcode):
    Bon_endroit = sum(1 for a, b in zip(globbornes, globcode) if a == b)
    Mauvais_endroit = sum(min(globbornes.count(n), globcode.count(n)) for n in set(globcode)) - Bon_endroit
    return Bon_endroit, Mauvais_endroit

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Crack the Code")
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    font = pygame.font.Font(None, 50)
    
    input_box = pygame.Rect(300, 200, 200, 50)
    color_active, color_inactive = WHITE, GRAY
    color = color_inactive
    active = False
    text = ""
    message = ""
    historique = []

    # Variables pour la victoire
    victoire = False
    victoire_time = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not victoire:  # Empêche toute action après la victoire
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        if len(text) == 4 and text.isdigit():
                            if text == "6666":
                                message = "Bravo, code trouvé !"
                                victoire = True
                                victoire_time = pygame.time.get_ticks()
                            else:
                                guess = [int(ch) for ch in text]
                                bon, mauvais = compare(guess, globcode)
                                message = f"{bon} bien placé, {mauvais} mal placé"
                                historique.append(f"{text} : {bon} bien placé, {mauvais} mal placé")
                                if bon == 4:
                                    message = "Bravo, code trouvé !"
                                    victoire = True
                                    victoire_time = pygame.time.get_ticks()
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < 4 and event.unicode.isdigit():
                        text += event.unicode

        # Affichage boîte de saisie
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, WHITE)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

        # Affiche le message
        msg_surface = font.render(message, True, WHITE)
        screen.blit(msg_surface, (200, 250))

        # Historique
        y_offset = 300
        for past_guess in historique[-5:]:
            past_surface = font.render(past_guess, True, WHITE)
            screen.blit(past_surface, (200, y_offset))
            y_offset += 30

        # Si victoire, attendre 5 secondes avant de fermer
        if victoire and pygame.time.get_ticks() - victoire_time >= 2000:
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def run():
    main()

if __name__ == "__main__":
    run()
