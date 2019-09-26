import tkinter
# ウィンドウ作成
root = tkinter.Tk()
root.title("王様をいっぱい表示")
root.minsize(1600, 800)
# キャンバス配置
canvas = tkinter.Canvas(root,width=1600,height=800)
canvas.pack()
img = tkinter.PhotoImage(file = "img4/chap4-1-1.png")
# 繰り返し処理
for i in range(7):
    canvas.create_image(100 + i * 200, 180 + i * 50, image=img)
root.mainloop()