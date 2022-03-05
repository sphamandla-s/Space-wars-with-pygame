import math

def collude(enemy_x, bullet_x, enemy_y, bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x,2)) + (math.pow(enemy_y - bullet_y,2)))
    if distance < 27:
        return True
    return False