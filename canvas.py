#!/usr/bin/env python

from ncca.Canvas import *
from random import randint

count = 0
for _ in range(1000000) :
    x=randint(0,width)
    y=randint(0,height)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    put_pixel(x,y,r,g,b)
    count += 1
    if count % 1000 == 0 :
       update()

main_loop()