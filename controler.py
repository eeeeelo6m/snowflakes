import pygame,model
from pygame import event
pygame.init()
TIMER_SNOWFLAKE=pygame.event.custom_type()
pygame.time.set_timer(TIMER_SNOWFLAKE,2000)

def control():
    e=event.get()
    for r in e:
        if r.type==pygame.QUIT:
            exit()
        if r.type==TIMER_SNOWFLAKE:
            model.add_snow_flakes()
