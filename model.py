import CLASS,random,CLASS_1,pygame



def add_snow_flakes():
    y = random.randint(1, 15) / 10
    class_rect = CLASS.Snowflake(random.randint(0, 1049),0,y)

    class_rects.append(class_rect)


def del_snowflakes():
    for class_rect in class_rects:
        if class_rect.uhla_tha_screen()==True:
            class_rects.remove(class_rect)


def stop(x,y):
    for class_rect1 in class_rects:
        if class_rect1.rect_snowflake.collidepoint(x,y) and type(class_rect1)==CLASS.Snowflake:

            class_rects.remove(class_rect1)
            class_rect = CLASS_1.Water(class_rect1.x,class_rect1.y)
            class_rects.append(class_rect)


def zahvat(x,y):
    for class_rect1 in class_rects:
        if class_rect1.rect_snowflake.collidepoint(x,y) and type(class_rect1) is CLASS.Snowflake:
            class_rect1.sostoynie='perenos'


def peredviganie_snowflake():
    pass



def step():
    del_snowflakes()
    for class_rect1 in class_rects:
        class_rect1.dvigenie()





class_rects = []
