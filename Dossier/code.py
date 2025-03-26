import pygame
import random

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jetpack Joyride - Pièces et Obstacles Stylisés")

player_image = pygame.image.load("Dossier/player.png")  
fireball_image = pygame.image.load("Dossier/fireball.png")  
piece_image = pygame.image.load("Dossier/piece.png") 
obstacle_violet_image = pygame.image.load("Dossier/obstacle_violet.png") 
background_image = pygame.image.load("Dossier/background.jpg") 

player_image = pygame.transform.scale(player_image, (80, 120))
fireball_image = pygame.transform.scale(fireball_image, (60, 60))
piece_image = pygame.transform.scale(piece_image, (40, 40))  
obstacle_violet_image = pygame.transform.scale(obstacle_violet_image, (70, 70))
background_image = pygame.transform.scale(background_image, (largeur_fenetre, hauteur_fenetre))


BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
OR = (255, 223, 0)
BLEU = (0, 0, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)
VIOLET = (128, 0, 128)

clock = pygame.time.Clock()

player_width = 50
player_height = 50
player_x = 100
player_y = hauteur_fenetre // 2
player_velocity = 5
is_flying = False

piece_radius = 15
pieces = []
                
obstacle_violet_width = 50
obstacle_violet_height = 50
obstacle_violet_velocity = 5
obstacles_violets = []

fireballs = []
fireball_velocity = 7

def dessiner_joueur(x, y):
    fenetre.blit(player_image, (x, y))

def dessiner_piece(piece):
    fenetre.blit(piece_image, piece)

def dessiner_obstacle_violet(obstacle):
    fenetre.blit(obstacle_violet_image, obstacle)

def dessiner_boule_de_feu(fireball):
    fenetre.blit(fireball_image, fireball)

def generer_piece():
    x = random.randint(200, largeur_fenetre - 100)
    y = random.randint(50, hauteur_fenetre - 50)
    return pygame.Rect(x, y, 30, 30)

def generer_obstacle_violet():
    x = largeur_fenetre
    y = random.randint(50, hauteur_fenetre - obstacle_violet_height)
    return pygame.Rect(x, y, obstacle_violet_width, obstacle_violet_height)

def generer_boule_de_feu():
    x = largeur_fenetre
    y = random.randint(50, hauteur_fenetre - 30)  
    return pygame.Rect(x, y, 30, 30)

def verifier_collision_cercle_rectangle(cercle, rectangle):
    cercle_center = pygame.math.Vector2(cercle.center)
    rectangle_center = pygame.math.Vector2(rectangle.center)
    
    distance = cercle_center.distance_to(rectangle_center)
    if distance <= (cercle.width / 2 + player_width / 2):
        return True
    return False

def deplacer_pieces_vers_joueur():
    global pieces
    for piece in pieces:
        piece_center = pygame.math.Vector2(piece.center)
        player_center = pygame.math.Vector2(player_x + player_width / 2, player_y + player_height / 2)
        
        direction = player_center - piece_center
        direction = direction.normalize() * 2  
        
        piece.centerx += direction.x
        piece.centery += direction.y

def boucle_principale():
    global player_y, is_flying, obstacles_violets, pieces, fireballs
    
    game_over = False
    score = 0
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_flying = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    is_flying = False

        if is_flying:
            player_y -= player_velocity
        else:
            player_y += player_velocity
        
        if player_y < 0:
            player_y = 0
        if player_y > hauteur_fenetre - player_height:
            player_y = hauteur_fenetre - player_height
        
        if random.random() < 0.02:
            pieces.append(generer_piece())
        
        if random.random() < 0.02:
            obstacles_violets.append(generer_obstacle_violet())
        
        if random.random() < 0.02:
            fireballs.append(generer_boule_de_feu())
        
        obstacles_violets = [obstacle.move(-obstacle_violet_velocity, 0) for obstacle in obstacles_violets]
        
        fireballs = [fireball.move(-fireball_velocity, 0) for fireball in fireballs]
        
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for obstacle in obstacles_violets:
            if player_rect.colliderect(obstacle):
                game_over = True
        
        for fireball in fireballs:
            if player_rect.colliderect(fireball):
                game_over = True
        
        pieces_cueillies = []
        for piece in pieces:
            if verifier_collision_cercle_rectangle(piece, player_rect):
                pieces_cueillies.append(piece)
                score += 10  
        
        pieces = [piece for piece in pieces if piece not in pieces_cueillies]
        
        obstacles_violets = [obstacle for obstacle in obstacles_violets if obstacle.x + obstacle_violet_width > 0]
        fireballs = [fireball for fireball in fireballs if fireball.x + 30 > 0]
        
        deplacer_pieces_vers_joueur()
        
        fenetre.blit(background_image, (0, 0))  
        dessiner_joueur(player_x, player_y)
        
        for obstacle in obstacles_violets:
            dessiner_obstacle_violet(obstacle)
        
        for fireball in fireballs:
            dessiner_boule_de_feu(fireball)
        
        for piece in pieces:
            dessiner_piece(piece)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, NOIR)
        fenetre.blit(score_text, (10, 10))
        
        pygame.display.update()
        
        clock.tick(60)

    pygame.quit()

boucle_principale()
  