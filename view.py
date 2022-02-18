from pygame import font, display
screen = display.set_mode([1050, 650])
import model,modelview


f = font.match_font('centurygothic', True, False)
shirpht = font.Font(f, 50)

print(font.get_fonts())




def view():

    screen.fill([21, 232, 231])
    collichestvo = len(model.class_rects)
    shirpht_schet_snovflakes = shirpht.render(str(collichestvo), True, [46, 90, 192])
    for class_rect in model.class_rects:
        if modelview.regim=='test':
            class_rect.draw_snowflakes(screen)
        if modelview.regim=='game':
            class_rect.draw_cartinca_snowflake(screen)

    screen.blit(shirpht_schet_snovflakes, [0, 0])
    display.flip()
