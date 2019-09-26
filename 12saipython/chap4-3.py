import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("仲間を選ぶ")
root.minsize(640, 480)
root.option_add("*font", ("メイリオ", 14))

# 画像読み込み
king_img = tkinter.PhotoImage(file = 'img4/chap4-2-1.png')
monsterA_img = tkinter.PhotoImage(file = 'img4/chap4-2-2.png')
monsterB_img = tkinter.PhotoImage(file = 'img4/chap4-2-3.png')

# キャンバス作成
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(110, 220, image=king_img, tag="illust")
canvas.create_image(320, 220, image=monsterA_img, tag="illust")
canvas.create_image(530, 220, image=monsterB_img, tag="illust")

# ラベル配置
sysText = tkinter.Label(text="だれを仲間にしますか？\
    （1:王様、2:魔物A、3:魔物B）")
sysText.place(x=100, y=20)

# 入力ボックス配置
entry= tkinter.Entry(width=12)
entry.place(x=200, y=350)

# ボタン配置
button = tkinter.Button(text="決定")
button.place(x=380, y=350)

# ボタンクリックイベント関数
def btn_click():
    val = float(entry.get())
    if val == 1:
        res_text = tkinter.Label(text="王様が仲間になりました。")
        res_text.place(x=200, y=60)
        canvas.delete("illust")
        canvas.create_image(320, 220, image=king_img,
        tag="illust")
    elif val == 2:
        res_text = tkinter.Label(text="魔物Aが仲間になりました。")
        res_text.place(x=200, y=60)
        canvas.delete("illust")
        canvas.create_image(320, 220, image=monsterA_img,
        tag="illust")
    elif val == 3:
        res_text = tkinter.Label(text="魔物Bが仲間になりました。")
        res_text.place(x=200, y=60)
        canvas.delete("illust")
        canvas.create_image(320, 220, image=monsterB_img,
            tag="illust")
    else:
        res_text = tkinter.Label(text="誰も仲間になりませんでした。")
        res_text.place(x=160, y=60)
        canvas.delete("illust")
    button["state"] = "disabled"
    entry["state"] = "disabled"

# ボタンクリックイベントと関数の関連付け
button["command"] = btn_click

root.mainloop()