import pygame as pg
import Utils.Constants as c

# --- Image Load ---
def il(route):
    return pg.image.load(route).convert_alpha()

# --- Scale Image
def scale(image, scale):

    w = image.get_width()
    h = image.get_height()

    scaled = pg.transform.scale(image, (w * scale, h * scale))
    return scaled

# --- Loop, Scale & Store animations
def create_animations(direction):
    animation = []
    for i in range(1,5):
        img = il(f'/mnt/c/Users/Andrei/OneDrive/Desktop/Py-Dev/GameDevelopment/FirstProject/src/Assets/Images/Characters/Main/{direction}-{i}.png')
        s_img = scale(img, c.M_SCALE)
        animation.append(s_img)
    
    return animation

# --- Select, Loop and Show animation

def loop_selected_animation(character, selection):

        cooldown = 100
        selected_animation = character.animation_dict[selection]

        character.image = selected_animation[character.frame_index]

        if pg.time.get_ticks() - character.time_passed >= cooldown:
            character.frame_index += 1
            character.time_passed = pg.time.get_ticks()

        if character.frame_index == len(selected_animation):
            character.frame_index = 0

def select_animation(direction = 'idle'):
    
    if direction == 'forward':
        return 0
    elif direction == 'backwards':
        return 1
    elif direction == 'sides':
        return 2
    elif direction == 'idle':
        return 3
    else:
        return 3
    
# --- Flip Img

def flip(img, axis = 'x'):

    if axis == 'x':
        return pg.transform.flip(img, True, False)
    elif axis == 'y':
        return pg.transform.flip(img, False, True)
    else:
        return