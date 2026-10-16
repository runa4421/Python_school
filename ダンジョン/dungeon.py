import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("動かす")

CANVAS_SIZE = 800
FONT = ("Comic Sans MS", 20)
key = ""
x = CANVAS_SIZE//10
y = CANVAS_SIZE//8*7

cvs=tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white")

img = Image.open("magic_neko.png")
w = img.width
h = img.height
img = img.resize(( int(w * (150/w)), int(h * (150/w)) ))
img_tk = ImageTk.PhotoImage(img)


m=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [1, 1, 0, 0, 0, 0, 1, 0, 0], 
    [1, 0, 1, 1, 0, 1, 1, 1, 1], 
    [1, 0, 1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 0, 0, 1], 
    [1, 0, 1, 0, 1, 1, 0, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1], 
]


n=len(m)
walk=CANVAS_SIZE//n

def MAP():
    for y in range(n):
        for x in range(n):
            if m[y][x] == 1:
                cvs.create_rectangle(x*walk, y*walk, x*walk+walk, y*walk+walk, fill="gray")

def key_down(e):
    global key
    key = e.keysym
    move()

def move():
    global x, y
    cvs.delete("all")
    MAP()
    cvs.create_text(CANVAS_SIZE//2, CANVAS_SIZE//20, text="正しい道を進もう！", font=FONT, fill="purple")
    if key == "Up":
        y -= 5
    if key == "Down":
        y += 5
    if key == "Left":
        x -= 5
    if key == "Right":
        x += 5
    cvs.create_image(x, y, image=img_tk)
    
MAP()
cvs.create_image(x, y, image=img_tk)
cvs.create_text(CANVAS_SIZE//2, CANVAS_SIZE//15, text="まほうつかいネコと\nめいろダンジョン", font=FONT, fill="purple")

cvs.pack()
root.bind("<KeyPress>", key_down)
label=tk.Label(font=("Times New Roman", 80))
label.pack()
root.mainloop()