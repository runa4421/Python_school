import random

japanese=["雨","猫","砂糖","たぬき","教師","アルパカ","冷蔵庫"]
english=["ame","neko","satou","tanuki","kyousi","arupaka","reizouko"]

n=len(japanese)
right=0

def result():
    global right
    print("----------終了！----------")
    print("獲得点数：", right, "点 ／16 点")
    if right == 0:
        print("もっと練習しよう")
    if 1 <= right <= 5:
        print("もう少し頑張ろう！")
    if 6 <= right <= 9:
        print("君ならもっとできる！")
    if 10 <= right <= 15:
        print("惜しい！あと少しだ！")
    if right == 16:
        print("素晴らしい！君はタイピングマスターだ！")


print("----------タイピングゲームスタート！----------")
r = random.sample(range(0, n), n)
for i in range(n):
    a = r[i]
    print("この単語を打て！")
    t=input(japanese[a])
    if t == english[a]:
        print("正解！(^^)v")
        if a ==0 or a == 1:
            right += 1
            print("＋１点")
        if a == 2 or a == 3:
            right += 2
            print("＋２点")
        if a == 4 or a == 5:
            right += 3
            print("＋３点")
        if a == 6:
            right += 4
            print("＋４点")
    else:
        print("不正解(><)")
result()