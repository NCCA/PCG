from . Visualizer import Visualizer

__all__ = ['width','height',"put_pixel", "get_pixel", "update", "clear", "set_bg_color", "save", "main_loop"]

width = 400
height = 400
_canvas = Visualizer(width=width, height=height, bg="#000000")

def put_pixel(x, y, r, g, b):
    _canvas.put_pixel(x, y, r, g, b)

def get_pixel(x, y):
    return _canvas.get_pixel(x, y)

def update():
    _canvas.update()

def clear():
    _canvas.clear()

def set_bg_color(r, g, b):
    _canvas.set_bg_color(r, g, b)

def save(name):
    _canvas.save(name)

def main_loop():
    _canvas.main_loop()