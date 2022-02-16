import CLASS,random,CLASS_1


def add_snow_flakes():
    y = random.randint(1, 15) / 10
    #class_rect = CLASS.Snowflake(0, random.randint(0, 1049),y)
    class_rect = CLASS_1.Water(0, random.randint(0, 1049))
    class_rects.append(class_rect)


def del_snowflakes():
    for class_rect in class_rects:
        if class_rect.uhla_tha_screen()==True:
            class_rects.remove(class_rect)




def step():
    del_snowflakes()
    for class_rect1 in class_rects:
        class_rect1.dvigenie()





class_rects = []
