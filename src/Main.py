import pygame as pg, sys
from pygame.locals import *

import Utils.Constants as c
import Utils.Functions as f

from Entities.MainCharacter import Character
from Entities.Weapon import Weapon

# --- Game Launch ---
pg.init()

# --- Screen ---
SCREEN = pg.display.set_mode((c.WIDTH, c.HEIGHT)) # Crea una ventana con la resolución especificada

    # --- Settings
CLOCK = pg.time.Clock()


# --- Window ---
pg.display.set_caption("The Binding of lil' Isaac") # Nombre en la ventana
# --- Main Character --- #

f_animation = f.create_animations('Forward')
b_animation = f.create_animations('Backwards')
s_animation = f.create_animations('Sides')
i_animation = f.create_animations('Idle')

mainChar = Character(50, 50, f_animation, b_animation, s_animation, i_animation)
    # --- Vars

left_movement = False
right_movement = False
up_movement = False
down_movement = False

# --- Weaponry --- #
weapon_img = f.il('./Assets/Images/Weapons/TBoI_Weapon.png')
s_weapon = f.scale(weapon_img, c.WEAPON_SCALE)
weapon = Weapon(s_weapon) 

# --- Development --- #
animation_selection = f.select_animation()

# --- Gameplay ---
while True:
    #Background:
    SCREEN.fill(c.GRAY)

    #Draw Main Character
    mainChar.draw(SCREEN)

    #Draw Weapon
    weapon.update(mainChar)
    weapon.draw_weapon(SCREEN)

    #Testing

    # -- --

    CLOCK.tick(c.FPS)

    delta_x = 0
    delta_y = 0

    f.loop_selected_animation(mainChar, animation_selection)

    if left_movement == True:
        delta_x -= c.M_SPEED
    if right_movement == True:
        delta_x += c.M_SPEED
    if up_movement == True:
        delta_y -= c.M_SPEED
    if down_movement == True:
        delta_y += c.M_SPEED

    mainChar.movement(delta_x, delta_y)

    for e in pg.event.get():

        if e.type == QUIT:
            pg.quit()
            sys.exit()

        if e.type == pg.KEYDOWN:

            if e.key == pg.K_a:
                left_movement = True
                animation_selection = f.select_animation('sides')
                mainChar.flip = True

            if e.key == pg.K_w:
                up_movement = True
                animation_selection = f.select_animation('backwards')
            
            if e.key == pg.K_d:
                right_movement = True
                animation_selection = f.select_animation('sides')
                mainChar.flip = False

            if e.key == pg.K_s:
                down_movement = True
                animation_selection = f.select_animation('forward')

        if e.type == pg.KEYUP:

            if e.key == pg.K_a:
                left_movement = False
                
            if e.key == pg.K_w:
                up_movement = False

            if e.key == pg.K_d:
                right_movement = False

            if e.key == pg.K_s:
                down_movement = False

        if down_movement == False and up_movement == False and left_movement == False and right_movement == False:
            animation_selection = f.select_animation('idle')

    pg.display.update()