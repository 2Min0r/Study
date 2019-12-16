# coding: utf-8
import tkinter as tk

class Ball:
    def __init__ (self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        
    def move(self, canvas):
        self.erase(canvas)
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.draw(canvas)

        if self.x >= canvas.winfo_width() or self.x <= 0:
            self.dx = -self.dx
        if self.y >= canvas.winfo_height() or self.y <= 0:
            self.dy = -self.dy

    def erase(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)

    def draw(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)

class Rectangle(Ball):    
    def erase(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)

    def draw(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)

class Triangle(Ball):    
    def erase(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill = "white", width = 0)

    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill = self.color, width = 0)




balls = [
    Ball(400, 200, 2, 2, "pink"),
    Ball(300, 400, 2, 2, "purple"),
    Ball(200, 250, 2, 2, "yellowgreen"),
    Rectangle(250, 300, 2, 2, "red"),
    Triangle(150, 150, 2, 2, "yellow")
    ]
    

def loop():
    for b in balls:
        b.move(canvas)

    root.after(10,loop)

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(root, width = 800, height = 600, bg = "white")
canvas.place(x = 0, y = 0)

root.after(10, loop)

root.mainloop()
