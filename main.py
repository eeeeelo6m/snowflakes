import pygame,time,view,controler,model

pygame.init()




while 1==1:

    time.sleep(1/100)

    controler.control()
    model.step()
    view.view()



