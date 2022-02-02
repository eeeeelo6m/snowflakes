import pygame,time,CLASS,random,controler,model
from pygame import display,draw,font
pygame.init()

f = font.match_font('segoefluenticons', True, False)
shirpht = font.Font(f, 20)
shirpht = shirpht.render('123', True, [46, 90, 192])





screen = display.set_mode([1050, 650])
screen.fill([21, 232, 231])


while 1==1:

    time.sleep(1/100)

    controler.control()
    model.step()
    screen.fill([21, 232, 231])
    for class_rect in model.class_rects:
        class_rect.draw_snowflakes(screen)


    pygame.event.get()
    screen.blit(shirpht,[0,0])
    display.flip()
