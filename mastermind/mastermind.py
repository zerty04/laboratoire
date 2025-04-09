
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
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Crack the Code")
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    font = pygame.font.Font(None, 50)
    
    input_box = pygame.Rect(200, 150, 200, 50)
    color_active, color_inactive = WHITE, GRAY
    color = color_inactive
    active = False
    text = ""
    message = ""
    historique = []
    
    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    if len(text) == 4 and text.isdigit():
                        guess = [int(ch) for ch in text]
                        historique.append(text)
                        bon, mauvais = compare(guess, globcode)
                        message = f"{bon} bien placé, {mauvais} mal placé"
                        if bon == 4:
                            message = "Bravo, code trouvé !"
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if len(text) < 4 and event.unicode.isdigit():
                        text += event.unicode
        
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, WHITE)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
        
        msg_surface = font.render(message, True, WHITE)
        screen.blit(msg_surface, (200, 250))
        
        y_offset = 300
        for past_guess in historique[-5:]:
            past_surface = font.render(past_guess, True, WHITE)
            screen.blit(past_surface, (200, y_offset))
            y_offset += 30
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
