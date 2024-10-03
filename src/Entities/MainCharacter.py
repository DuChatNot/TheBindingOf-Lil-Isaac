import pygame as pg
import Utils.Constants as c
import Utils.Functions as f

class Character:

    def __init__(self, x, y, f_animation, b_animation, s_animation, i_animation):

        self.flip = False

        self.shape = pg.Rect(0, 0, c.CH_HEIGHT, c.CH_WIDTH) # -> ( coordenadas X, coordenadas Y, medidas X, medidas Y )
        self.shape.center = (x, y)

        # -- Animation Storage
        self.animation_dict = {0: f_animation, 1: b_animation, 2: s_animation, 3: i_animation}

        # -- Animation Loop
        self.frame_index = 0
        self.image = i_animation[0]

        # -- Time measure
        self.time_passed = pg.time.get_ticks() # En milisegundos



    def draw(self, screen):

        flipped_image = pg.transform.flip(self.image, self.flip, False) # Voltea al personaje
        if self.flip:
            screen.blit(flipped_image, self.shape)  # -> ( Que dibujar , En donde dibujar )
        else:
            screen.blit(self.image, self.shape)

        pg.draw.rect(screen, c.YELLOW_MANGO, self.shape, 1)

    def movement(self, delta_x, delta_y):

        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False