#!/usr/bin/env python

from ncca import Visualizer
import random
width = 400
height = 400
canvas=Visualizer.Visualizer(width=width, height=height, bg="#000000")

# first seed some pixels with red
for x in range(0,width) :
    # x=random.randint(1,width-1)
    # y=random.randint(1,height-1)
    canvas.put_pixel(x,height//2,255,0,0)


# now we will do a random walk
x=random.randint(1,width-1)
y=random.randint(1,height-1)

def has_seed(x,y) -> bool :
    choices=[-1,0,1]
    for xr in choices :
        for yr in choices :
            
            if canvas.get_pixel(x+xr,y+yr)==(255,0,0) :
                return True
    return False

# now we will do a random walk
for _ in range(0,55000000) :
    if has_seed(x,y) :
        # change the pixel to black then reset the random walk
        canvas.put_pixel(x,y,255,0,0)
        x=random.randint(1,width-1)
        y=random.randint(1,height-1)
        #print(f"found seed {x},{y}")
        #canvas.update()

    else :
        x_diff=random.randint(-1,1)
        y_diff=random.randint(-1,1)
        x+=x_diff
        y+=y_diff
        if x<0 or x>width :
            x=random.randint(1,width-1)
        if y<0 or y>height :
            y=random.randint(1,height-1)


canvas.save("dla.png")
print("saved dla.png")
canvas.main_loop()
