#!/usr/bin/env python

from ncca import Visualizer
import random
width = 400
height = 400
canvas=Visualizer.Visualizer(width=width, height=height, bg="#000000")

# dr
def draw_circle(x,y,radius,r,g,b) :
    # draw a circle at x,y with radius r
    for x1 in range(x-radius,x+radius) :
        for y1 in range(y-radius,y+radius) :
            if (x1-x)**2+(y1-y)**2<radius**2 :
                canvas.put_pixel(x1,y1,r,g,b)



ball_x=width//2
ball_y=height//2

for _ in range(0,10000) :
    canvas.clear()
    # update the ball position and velocity
    ball_x+=1
    ball_y+=1
    if ball_x>width :
        ball_x=0
    if ball_y>height :
        ball_y=0
    print(f"ball_x={ball_x},ball_y={ball_y}")
    draw_circle(ball_x,ball_y,10,255,0,0)
    canvas.update()
    


canvas.save("circle.png")
canvas.main_loop()
