import pygame
from pygame import draw
class Snowflake:
    def __init__(self,y,x,speedy):
        self.y=y
        self.x=x
        self.speedy=speedy
        self.rect_snowflake=pygame.Rect(self.x,self.y,50,50)
        print('snowflaks was created')

    def draw_snowflakes(self,screen):
        draw.rect(screen,[123,123,123],self.rect_snowflake)


    def dvigenie(self):
        self.y+=self.speedy
        self.rect_snowflake.y=self.y

