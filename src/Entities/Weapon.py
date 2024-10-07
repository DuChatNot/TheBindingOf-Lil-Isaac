import pygame as pg

import Utils.Constants as c
import Utils.Functions as f
import math as m

class Weapon():

    def __init__(self, weapon_img):
        self.weapon_img = weapon_img # Imagen PNG del arma
        self.angle = 0
        self.weapon = pg.transform.rotate(self.weapon_img, self.angle) # Rotar el arma en función al movimiento del personaje
        self.weapon_container = self.weapon.get_rect() # Encierra al arma en un rectangulo (hitbox)

    def update(self, character):
        self.weapon_container.center = character.shape.center
        if character.flip:
            self.weapon_container.x = self.weapon_container.x - character.shape.width/2
            self.rotate_weapon(True)
        else:
            self.weapon_container.x = self.weapon_container.x + character.shape.width/2
            self.rotate_weapon(False)
        
        # Movimiento de arma (Mouse)

        mouse_pos = pg.mouse.get_pos() # Devuelve una lista en formato [x , y]
        delta_x = mouse_pos[0] - self.weapon_container.centerx
        delta_y = - (mouse_pos[1] - self.weapon_container.centery)
        delta_angle = m.degrees(m.atan2(delta_y, delta_x))
        
        '''
        if(-1 > delta_angle and self.angle > -37):
            self.angle = delta_angle
        '''
        


    def draw_weapon(self, surface):
        self.weapon = pg.transform.rotate(self.weapon, self.angle)
        surface.blit(self.weapon, self.weapon_container)
        pg.draw.rect(surface, c.SEA_GREEN, self.weapon_container, 1) # Dibuja la hitbox del arma

    def rotate_weapon(self, rotation):
        if rotation:
            f_weapon = f.flip(self.weapon_img)
            self.weapon = pg.transform.rotate(f_weapon, self.angle + 90)
        else:
            f_weapon = f.flip(self.weapon_img, 'n')
            self.weapon = pg.transform.rotate(f_weapon, self.angle -90)

