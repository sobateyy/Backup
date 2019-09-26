import tkinter
# ウィンドウ作成
root = tkinter.Tk()
root.title("王様をいっぱい表示")
root.minsize(1600, 480)
# キャンバス配置
canvas = tkinter.Canvas(root,width=1600,height=480)
canvas.pack()
img = tkinter.PhotoImage(file = "img4/chap4-1-1.png")
# 座標用変数
x = 100
y = 180
# 繰り返し処理
while True:
    canvas.create_image(x, y, image=img)
    x = x + 200
    y = y + 50
    if x >= 1600 or y >= 480:
        break
root.mainloop()