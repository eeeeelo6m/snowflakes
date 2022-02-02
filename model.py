import CLASS,random


def add_snow_flakes():
    y = random.randint(1, 15) / 10
    class_rect = CLASS.Snowflake(0, random.randint(0, 1049),y)
    class_rects.append(class_rect)




def step():
    for class_rect1 in class_rects:
        class_rect1.dvigenie()





class_rects = []
