import pygame
from player import player_1
from enemy import enemy
from bullet import ship_bullet

pygame.init()
screen = pygame.display.set_mode((1350, 680))
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Wars")
font = pygame.font.Font("freesansbold.ttf", 32)

bullet_y = 675
bullet_x = 0
bullet_change_x = 0
bullet_change_y = 3
bullet_state = 'ready'
bullet_value = 10
score_value = 0


def play(x,y):
    player_Img = pygame.image.load("space-ship1.png")
    screen.blit(player_Img, (x,y))


def alien(x, y):
    enemy_img = pygame.image.load("alien.png")
    screen.blit(enemy_img, (x,y))


def bullet(x,y):
    global bullet_state
    bullet_img = pygame.image.load("bullet.png")
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 16,y + 10))
    screen.blit(bullet_img, (x - 16,y + 10))


def show_score(x,y):
    score = font.render('SCORE: ' + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


def bullet_left():
    score = font.render('BULLET: ' + str(bullet_value), True, (255,255,255))
    screen.blit(score, (1150,10))


def game_over():
    game_over_font = pygame.font.Font("freesansbold.ttf", 66)
    over = game_over_font.render('GAME OVER :(', True, (200,55,25))
    screen.blit(over, (450,250))



def run_space_wars(screen, change_position_x):
    global bullet_value
    global bullet_y 
    global bullet_x
    global bullet_state
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_position_x = -1.5
                if event.key == pygame.K_RIGHT:
                    change_position_x = 1.5
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready' and bullet_value >= 0:
                        bullet_x = player_x
                        bullet(bullet_x, bullet_y)
                        bullet_value -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_position_x = 0

        player_x =  player_1.player_movement(change_position_x)
        alien_x, alien_y = enemy.enemy_movement()
        
        if alien_y > 200 or bullet_value < 0:
            game_over()
            alien_x += 2000

        if bullet_y <=0:
            bullet_y = 570
            bullet_state = 'ready'


        if bullet_state == 'fire':
            bullet(bullet_x, bullet_y)
            bullet_y -= bullet_change_y
        

        if ship_bullet.collude(alien_x,bullet_x,alien_y,bullet_y):
            global score_value
            bullet_y = 675
            score_value += 1
            bullet_value += 1
            bullet_state = 'ready'
            enemy.enemy_hited()


        play(player_x,570)
        alien(alien_x,alien_y)
        show_score(10,10)
        bullet_left()
        pygame.display.update()



player_change_position_x = player_1.change_x()
run_space_wars(screen, player_change_position_x,)