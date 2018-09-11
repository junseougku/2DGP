import os
import math
from pico2d import *
os.chdir("C:\\Users\\inodata\\Documents\\blaster\\2d\\2DGP\\Drills\\Drill-03")

open_canvas()

character = load_image('character.png')
character.draw_now(400,90)
grass = load_image('grass.png')
grass.draw_now(400,30)

radis = 0
rad = 0

x = 400
y = 90


while(True):
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x=x+2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+2
        delay(0.01)

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.01)

    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        delay(0.01)

    while(radis<180):    
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+x,300+y)
        x = math.cos(math.radians(rad))*220
        y = math.sin(math.radians(rad))*220
        rad=rad+2
        radis=radis+1
        delay(0.01)
        
close_canvas()
