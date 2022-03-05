import random
from bullet import ship_bullet

alien_x = random.randrange(0,1290)
alien_y = random.randrange(0, 100)
enemy_change_x = 1
enemy_change_y = 30


def enemy_movement():
    global alien_x, alien_y
    global enemy_change_x
    global enemy_change_y

    alien_x += enemy_change_x

    if alien_x <= 0:
        enemy_change_x = 1
        alien_y += enemy_change_y
    elif alien_x >= 1290:
        enemy_change_x = -1
        alien_y += enemy_change_y
    return alien_x, alien_y


def enemy_hited():
    global alien_x
    global alien_y
    alien_x = random.randrange(0,860)
    alien_y = random.randrange(0, 100)