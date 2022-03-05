x = 675

def change_x():
    change_x = 0
    return change_x 


def player_movement(change):
    global x
    x += change
    if x <= 0:
        x = 0
    elif x >= 1290:
        x = 1290
    return x

