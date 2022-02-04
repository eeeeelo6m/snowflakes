import pygame
from pygame import draw,font
pygame.init()
f = font.match_font('centurygothic', True, False)
shirpht_1=font.Font(f,37)
class Snowflake:
    def __init__(self,y,x,speedy):
        self.y=y
        self.x=x
        self.speedy=speedy
        self.rect_snowflake=pygame.Rect(self.x,self.y,50,50)
        print('snowflaks was created')

    def draw_snowflakes(self,screen):
        draw.rect(screen,[123,123,123],self.rect_snowflake)

        shirpht_speed_snowflakes=shirpht_1.render(str(self.speedy),True,[210,120,89])
        screen.blit(shirpht_speed_snowflakes,[self.x,self.y])


    def dvigenie(self):
        self.y+=self.speedy
        self.rect_snowflake.y=self.y


    def uhla_tha_screen(self):
        if self.y>=650:
            return True


