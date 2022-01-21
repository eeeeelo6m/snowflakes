import CLASS,random


def add_snow_flakes():
    global class_rect,y
    class_rect = CLASS.Snowflake(y, random.randint(0, 500))
    y=0



def step():
    global y
    class_rect.x+=0
    y+=1
    class_rect.obect_snowflake.y=y



y=0
class_rect = CLASS.Snowflake(y, random.randint(0, 500))
