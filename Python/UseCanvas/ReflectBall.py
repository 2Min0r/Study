# coding: utf-8
import tkinter as tk

balls = [
    {"x" : 400, "y" : 300, "dx" : 4, "dy": 3, "color" : "red"},
    {"x" : 200, "y" : 100, "dx" : 3, "dy": 2, "color" : "blue"},
    {"x" : 100, "y" : 200, "dx" : 4, "dy": 5, "color" : "yellow"},
    {"x" : 300, "y" : 150, "dx" : 4, "dy": 2, "color" : "pink"},
    {"x" : 150, "y" : 250, "dx" : 4, "dy": 3, "color" : "skyblue"},
]

def move():
    global balls

    for b in balls:
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill = "white", width = 0)

        b["x"] = b["x"] + b["dx"]
        b["y"] = b["y"] + b["dy"]

        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill = b["color"], width = 0)

        if b["x"] >= canvas.winfo_width() - 20 or b["x"] <= 20:
            b["dx"] = -b["dx"]
        if b["y"] >= canvas.winfo_height() - 20 or b["y"] <= 20:
            b["dy"] = -b["dy"]
            
    root.after(10, move)


root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()
