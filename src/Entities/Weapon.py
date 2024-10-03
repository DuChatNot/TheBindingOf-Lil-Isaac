import pygame as pg

import Utils.Constants as c
import Utils.Functions as f

class Weapon():

    def __init__(self, weapon_img):
        self.weapon_img = weapon_img # Imagen PNG del arma
        self.angle = 0
        self.weapon = pg.transform.rotate(self.weapon_img, self.angle) # Rotar el arma en función al movimiento del personaje
        self.weapon_container = self.weapon.get_rect() # Encierra al arma en un rectangulo (hitbox)

    def update(self, character):
        self.weapon_container.center = character.shape.center
        self.weapon_container.x = self.weapon_container.x + character.shape.width/2


    def draw_weapon(self, surface):
        surface.blit(self.weapon, self.weapon_container)
        pg.draw.rect(surface, c.SEA_GREEN, self.weapon_container, 1) # Dibuja la hitbox del arma

