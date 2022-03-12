import pygame, help, time
from pygame import draw, font

pygame.init()

f = font.match_font('centurygothic', True, False)
shirpht_1 = font.Font(f, 37)
snowflake_cartinca = pygame.image.load("picture/SNOWFLAKE.png")
snowflake_cartinca = help.izmeni_kartinku(snowflake_cartinca, 50, 50, [255, 255, 255], 100)
snowflake_fioletovay_cartinca = pygame.image.load("picture/snowflake_fioletovay.png")
snowflake_fioletovay_cartinca = help.izmeni_kartinku(snowflake_fioletovay_cartinca, 50, 50, [255, 255, 255], 100)


class Snowflake:
    def __init__(self, x, y, speedy):
        self.y = y
        self.x = x
        self.speedy = speedy
        self.sostoynie_snowflake = 'dvigenie'
        self.color = 'blue'
        self.rect_snowflake = pygame.Rect(self.x, self.y, 50, 50)
        self.izmenenie = time.time()
        print('snowflaks was created')

    def draw_snowflakes(self, screen):
        draw.rect(screen, [123, 123, 123], self.rect_snowflake)
        shirpht_speed_snowflakes = shirpht_1.render(str(self.speedy), True, [210, 120, 89])
        screen.blit(shirpht_speed_snowflakes, [self.x, self.y])

    def dvigenie(self):
        if self.sostoynie_snowflake == 'dvigenie':
            self.y += self.speedy
            self.rect_snowflake.y = self.y

    def uhla_tha_screen(self):
        if self.y >= 650:
            return True

    def draw_cartinca_snowflake(self, screen):
        if self.color == 'blue':
            screen.blit(snowflake_cartinca, [self.rect_snowflake.x, self.rect_snowflake.y])
        if self.color == 'fioletoviy':
            screen.blit(snowflake_fioletovay_cartinca, [self.rect_snowflake.x, self.rect_snowflake.y])
        if self.sostoynie_snowflake == 'perenos':
            self.mercanie()

    def mercanie(self):
        if self.izmenenie + self.speedy <= time.time() and self.color == 'fioletoviy':
            self.izmenenie += self.speedy
            self.color = 'blue'
        if self.izmenenie + self.speedy <= time.time() and self.color == 'blue':
            self.izmenenie += self.speedy
            self.color = 'fioletoviy'

    def perenos(self, x, y):
        self.x = x
        self.y = y
        self.rect_snowflake.x = self.x
        self.rect_snowflake.y = self.y



    @property
    def sostoynie(self):
        return self.sostoynie_snowflake

    @sostoynie.setter
    def sostoynie(self, value):
        self.sostoynie_snowflake=value
        self.color = 'blue'