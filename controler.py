import pygame,model,modelview
from pygame import event
pygame.init()
TIMER_SNOWFLAKE=pygame.event.custom_type()
pygame.time.set_timer(TIMER_SNOWFLAKE,2000)
TIMER_SNOWFLAKE_MORGANIE=pygame.event.custom_type()

def control():
    e=event.get()
    for r in e:
        if r.type==pygame.QUIT:
            exit()
        if r.type==TIMER_SNOWFLAKE:
            model.add_snow_flakes()
        if r.type==pygame.KEYDOWN and r.key==pygame.K_SPACE:
            modelview.regim='game' if modelview.regim=='test' else 'test'


        if r.type == pygame.MOUSEBUTTONDOWN and r.button == pygame.BUTTON_LEFT:
            model.stop(r.pos[0],r.pos[1])
            model.pocupka(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEBUTTONDOWN and r.button == pygame.BUTTON_RIGHT:
            model.zahvat(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEMOTION:
            model.peredviganie_snowflake(r.pos[0],r.pos[1])









