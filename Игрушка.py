from tkinter import *
import time
import random

window = Tk()
window.title("Аркада")
window.resizable(False, False)
window.wm_attributes("-topmost", 1)

class ball():
    def __init__(self, canvas, color, platform):
        self.canvas = canvas
        self.color = color
        self.platform = platform
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        dir = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(dir)
        self.y = -1
    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rectangle)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[1] <= platform_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        if pos[0] <= 0:
            self.x = 1
        if pos[1] <= 0:
            self.y = 1
        if pos[2] >= 500:
            self.x = -1
        if pos[3] >= 500:
            self.y = -1
        if self.touch_platform(pos):
            self.y = -3

        
class platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.rectangle = self.canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
    def left(self, event):
        self.x -=2
    def right(self, event):
        self.x +=2
    def draw(self):
        self.canvas.move(self.rectangle, self.x, 0)
        pos = self.canvas.coords(self.rectangle)
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= 500:
            self.x = -1
        
        
        
canvas = Canvas(window, width=500, height=500)
canvas.pack()
pl = platform(canvas, "blue")
bl = ball(canvas, "red", pl)
while True:
    pl.draw()
    bl.draw()
    window.update()
    time.sleep(0.01)
window.mainloop()

