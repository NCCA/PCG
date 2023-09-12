#!/usr/bin/env python

from ncca import Visualizer
from random import randint

canvas=Visualizer.Visualizer(width=100, height=100, bg="#000000")

for _ in range(0,100000) :
    x=randint(0,100)
    y=randint(0,100)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    canvas.put_pixel(x,y,r,g,b)
canvas.save("test.png")

canvas.main_loop()

