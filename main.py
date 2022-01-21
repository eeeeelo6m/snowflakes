import pygame,time,CLASS,random,controler,model
from pygame import display,draw
pygame.init()




screen = display.set_mode([1050, 650])
screen.fill([21, 232, 231])


while 1==1:
    time.sleep(1/100)
    controler.control()
    model.step()
    screen.fill([21, 232, 231])
    model.class_rect.draw_snowflakes(screen)


    pygame.event.get()

    display.flip()
