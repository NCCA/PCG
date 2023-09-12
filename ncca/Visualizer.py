from tkinter import Tk, Canvas, PhotoImage, mainloop



class Visualizer :
    

    def __init__(self, width : int =100, height : int =100, bg : str="#FFFFFFFF") -> None:
        window = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(window, width=width, height=height, bg="#FFFFFF")
        self.canvas.pack()
        self.img = PhotoImage(width=width, height=height)
        self.canvas.create_image((width//2, height//2), image=self.img, state="normal")

    def put_pixel(self, x: int, y: int, r : int,g : int ,b : int) -> None:
        try :
            self.img.put(f'#{r:02x}{g:02x}{b:02x}', (x, y)) 
        except :
            pass
    def get_pixel(self, x: int, y: int) -> tuple:
        try :
            return self.img.get(x,y)
        except :
            return (0,0,0)
        
    def update(self) -> None:
        self.canvas.update()
        self.canvas.update_idletasks()

    def clear(self) -> None:
        self.img.blank()

    def set_bg_color(self, r : int,g : int ,b : int) -> None:
        self.canvas.config(bg=f'#{r:02x}{g:02x}{b:02x}')

    def save(self,name : str) -> None:
        self.img.write(name, format="png")

    def main_loop(self) -> None:
        mainloop()