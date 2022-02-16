import pygame, help,CLASS
from pygame import draw, font

pygame.init()

f = font.match_font('centurygothic', True, False)
shirpht_1 = font.Font(f, 37)
water_cartinca = pygame.image.load("picture/WATER.png")
water_cartinca = help.izmeni_kartinku(water_cartinca, 50, 50, [230, 218, 0], 100)


class Water(CLASS.Snowflake):
    def __init__(self, y, x):
        CLASS.Snowflake.__init__(self,y,x,2)
        self.a=5

    def draw_cartinca_snowflake(self, screen):
        screen.blit(water_cartinca, [self.rect_snowflake.x, self.rect_snowflake.y])

