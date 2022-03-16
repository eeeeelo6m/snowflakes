import CLASS, random, CLASS_1, pygame


def add_snow_flakes():
    y = random.randint(1, 15) / 10
    class_rect = CLASS.Snowflake(random.randint(0, 1049), 0, y)
    class_rects.append(class_rect)
    return class_rect


def add_water(x,y):
    class_rect = CLASS_1.Water(x,y)
    class_rects.append(class_rect)
    return class_rect

def del_snowflakes():
    for class_rect in class_rects:
        if class_rect.uhla_tha_screen() == True:
            class_rects.remove(class_rect)


def stop(x, y):
    for class_rect1 in class_rects:
        if class_rect1.rect_snowflake.collidepoint(x, y) and type(class_rect1) == CLASS.Snowflake:
            class_rects.remove(class_rect1)
            class_rect = CLASS_1.Water(class_rect1.x, class_rect1.y)
            class_rects.append(class_rect)



def zahvat(x, y):
    global perenos
    if perenos == True:
        perenos = False
        for class_rect_1 in class_rects:
            class_rect_1.sostoynie = 'dvigenie'
    elif perenos == False:
        for class_rect1 in class_rects:
            if class_rect1.rect_snowflake.collidepoint(x, y) and type(class_rect1) is CLASS.Snowflake:
                class_rect1.sostoynie = 'perenos'
                perenos = True
                break


def peredviganie_snowflake(x, y):
    for class_rect1 in class_rects:
        if class_rect1.sostoynie == 'perenos':
            class_rect1.perenos(x, y)



def pocupka(x,y):
    global perenos
    if slot_snowflake.rect_snowflake.collidepoint(x, y):
        a=add_snow_flakes()
        a.sostoynie='perenos'
        a.perenos(x,y)
        perenos=True
    if slot_water.rect_snowflake.collidepoint(x, y):
        b=add_water(x,y)
        b.sostoynie='perenos'
        b.perenos(x,y)
        perenos=True



def step():
    del_snowflakes()
    for class_rect1 in class_rects:
        class_rect1.dvigenie()



perenos = False
class_rects = []
rect_magazin=pygame.Rect([1050-130,0],[130,70])
slot_snowflake=CLASS.Snowflake(rect_magazin.x+10, 10, 0)
slot_water=CLASS_1.Water(rect_magazin.x+70, 10)

