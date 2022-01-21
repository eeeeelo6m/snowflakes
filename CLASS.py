import pygame
from pygame import draw
class Snowflake:
    def __init__(self,y,x):
        self.y=y
        self.x=x
        self.obect_snowflake=pygame.Rect(self.x,self.y,50,50)
        print('snowflaks was created')

    def draw_snowflakes(self,screen):
        draw.rect(screen,[123,123,123],self.obect_snowflake)