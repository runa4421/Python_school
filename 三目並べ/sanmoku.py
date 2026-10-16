import tkinter as tk
import random
import time
from PIL import Image, ImageTk

masu=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

CANVAS_SIZE=600
FONT=("Comic Sans MS", 60)
shirushi=0
kachi=0
n=len(masu)
photo_images = []
s=0


def start():
    global shirushi
    cvs.delete("all")
    if s==0:
        root.title("三匹並べ")
        cvs.create_text(
            CANVAS_SIZE//2, CANVAS_SIZE//3, 
            text="３ひきならべ", font=FONT, fill="orange"
        )
        cvs.create_rectangle(
            CANVAS_SIZE//9*2, CANVAS_SIZE//2, CANVAS_SIZE//9*7, CANVAS_SIZE//7*5, 
            fill="thistle1", outline="plum", width=15
            )
        cvs.create_text(
            CANVAS_SIZE//2, CANVAS_SIZE//5*3, 
            text="はじめる", font=FONT, fill="purple"
        )
    if s==1:
        masume()
    if s==2:
        time.sleep(0.5)
        cvs.delete("all")
        cvs.create_text(
            CANVAS_SIZE//2, CANVAS_SIZE//3, 
            text="しゅうりょう！", font=FONT, fill="orange"
        )
        if kachi == 1:
            cvs.create_text(
                CANVAS_SIZE//2, CANVAS_SIZE//5*3, 
                text="あなたの勝ち！", 
                font=FONT, fill="#f66"
            )
        if kachi == 2:
            cvs.create_text(
                CANVAS_SIZE//2, CANVAS_SIZE//5*3, 
                text="コンピュータ\nの勝ち！", 
                font=FONT, fill="#f66"
            )
        if kachi == 0 and shirushi == 9:
            cvs.create_text(
                CANVAS_SIZE//2, CANVAS_SIZE//5*3, 
                text="ひきわけ><", font=FONT, fill="navy"
            )
        shirushi = 9


def masume():
    global photo_images
    cvs.delete("all")
    photo_images.clear()
    for i in range(1, n):
        a=CANVAS_SIZE//3*i
        cvs.create_line(
            a, 0, a-10, CANVAS_SIZE//3, a+10, CANVAS_SIZE//3*2, a, CANVAS_SIZE,
            fill = "plum", width = 8, smooth = True
        )
        cvs.create_line(
            0, a, CANVAS_SIZE//3, a-10, CANVAS_SIZE//3*2, a+10, CANVAS_SIZE, a, 
            fill = "plum", width = 8, smooth = True
        )

    for y in range(n):
        for x in range(n):
            images = ["1.png", "1.png", "2.png"]
            img = Image.open(images[masu[y][x]])
            w = img.width
            h = img.height
            img = img.resize(( int(w * (200/w)), int(h * (200/w)) ))
            img_tk = ImageTk.PhotoImage(img)
            photo_images.append(img_tk)
            X = x*CANVAS_SIZE//3+100
            Y = y*CANVAS_SIZE//3+110
            if masu[y][x] == 1:
                cvs.create_image(X, Y, image=img_tk)
            if masu[y][x] == 2:
                cvs.create_image(X, Y, image=img_tk)

    if shirushi == 0:
        cvs.create_text(
            CANVAS_SIZE//2, CANVAS_SIZE//2, 
            text = "スタート！", fill = "navy", font = FONT
        )
    cvs.update()


def click(e):
    global kachi, shirushi, s
    if s == 0:
        if (CANVAS_SIZE//9*2 <= e.x <= CANVAS_SIZE//9*7) and (CANVAS_SIZE//2 <= e.y <= CANVAS_SIZE//7*5):
            s = 1
            start()
        return
    if shirushi == 9:
        replay()
        return
    if shirushi == 1 or shirushi == 3 or shirushi == 5 or shirushi == 7:
        return
    mx = int(e.x/(CANVAS_SIZE//3))
    my = int(e.y/(CANVAS_SIZE//3))
    if mx > 2:  mx = 2
    if my > 2:  my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi += 1
        masume()
        time.sleep(0.5)
        kachi = hantei()
        syouhai()
        if kachi ==1 or shirushi == 9:
            start()
            return
        if shirushi<9:
            computer()
            masume()
            kachi = hantei()
            syouhai()
            start()


def computer():
    global shirushi
    for y in range(n):
        for x in range(n):
            if masu[y][x] == 0:
                masu[y][x] = 2
                t = hantei()
                if t == 2:
                    shirushi += 1
                    return
                masu[y][x] = 0
    for y in range(n):
        for x in range(n):
            if masu[y][x] == 0:
                masu[y][x] = 1
                t = hantei()
                if t == 1:
                    masu[y][x] = 2
                    shirushi += 1
                    return
                masu[y][x] = 0
    while True:
        x=random.randint(0,2)
        y=random.randint(0,2)
        if masu[y][x]==0:
            masu[y][x] = 2
            shirushi += 1
            break


def hantei():
    for i in range(1,n):
        if masu[0][0]==i and masu[1][0]==i and masu[2][0]==i:
            return i
        if masu[0][1]==i and masu[1][1]==i and masu[2][1]==i:
            return i
        if masu[0][2]==i and masu[1][2]==i and masu[2][2]==i:
            return i

        if masu[0][0]==i and masu[0][1]==i and masu[0][2]==i:
            return i
        if masu[1][0]==i and masu[1][1]==i and masu[1][2]==i:
            return i
        if masu[2][0]==i and masu[2][1]==i and masu[2][2]==i:
            return i

        if masu[0][0]==i and masu[1][1]==i and masu[2][2]==i:
            return i
        if masu[0][2]==i and masu[1][1]==i and masu[2][0]==i:
            return i
    return 0


def syouhai():
    global s
    if kachi == 1:
        root.title("あなたの猫が三匹揃いました")
        s = 2
    if kachi == 2:
        root.title("コンピュータの猫が三匹揃いました")
        s = 2
    if kachi == 0 and shirushi == 9:
        root.title("引き分けです")
        s = 2


def replay():
    global shirushi, s
    shirushi = 0
    for y in range(n):
        for x in range(n):
            masu[y][x] = 0
    s=0
    start()


root=tk.Tk()
root.resizable(False, False)
root.bind("<Button>", click)

cvs=tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="ivory")

cvs.pack()
start()
root.mainloop()