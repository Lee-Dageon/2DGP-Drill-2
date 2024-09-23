import math
from pico2d import *

open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')

A = (100, 100)
B = (700, 100)
C = (400, 400)


center_x, center_y = 400, 300
radius = 200  

def move_to(p1, p2):
    x, y = p1
    target_x, target_y = p2
    
    while x != target_x or y != target_y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        
        if x < target_x:
            x += 2
        elif x > target_x:
            x -= 2
        if y < target_y:
            y += 2
        elif y > target_y:
            y -= 2
        
        delay(0.001)

def move_in_circle():
    angle = 0
    while angle < 2 * math.pi:
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        character.draw_now(x, y)
        
        angle += 0.05
        
        delay(0.001)

while True:

    move_to(A, B)
    move_to(B, C)
    move_to(C, A)
    

    move_in_circle()

close_canvas()
