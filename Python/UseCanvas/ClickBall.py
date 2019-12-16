# coding: utf-8
import tkinter as tk

x = 300
y = 200

def click(event):
    global x, y
    
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0)

    x = event.x
    y = event.y
    
    canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill = "red", width = 0)


root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

canvas.bind("<Button-1>", click)

root.mainloop()
