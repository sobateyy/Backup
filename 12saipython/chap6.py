
import tkinter

# マップの描画
def draw_map():
    
    for y in range(0, MAX_HEIGHT):
        for x in range(0, MAX_WIDTH):
            p = map_data[y][x]
            canvas.create_image(x*62+31, y*62+31, image=images[p])

    # 主人公表示
    canvas.create_image(brave_x*62+31, brave_y*62+31,
        image=images[4], tag="brave")

# 移動先のチェック
def check_move(x, y):
    global brave_x, brave_y, flag_key
    if x>=0 and x<MAX_WIDTH and y>=0 and y<MAX_HEIGHT:
        p = map_data[y][x]
        if p == 1:
            return
        elif p == 3:
            flag_key = True
            map_data[y][x] = 0
            canvas.delete("all")
            draw_map()
        elif p == 2:
            if flag_key == True:
                ending()
            else:
                return
        brave_x = x
        brave_y = y
        canvas.coords("brave", brave_x*62+31, brave_y*62+31)
# 上ボタンが押された
def click_button_up():
    check_move(brave_x, brave_y-1)
# 下ボタンが押された
def click_button_down():
    check_move(brave_x, brave_y+1)
# 左ボタンが押された
def click_button_left():
    check_move(brave_x-1, brave_y)
# 右ボタンが押された
def click_button_right():
    check_move(brave_x+1, brave_y)

# エンディング表示
def ending():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 620, 434, fill="black")
    canvas.create_text(300, 200,
        fill="white", font=("MS ゴシック", 15),
        text="""ゴールおめでとう。

だが、君の戦いはまだ始まったばかりだ。

　　　　　　　　　　　　　　　      ……つづく？""")
    # ボタンを無効化
    button_up["state"] = "disabled"
    button_down["state"] = "disabled"
    button_left["state"] = "disabled"
    button_right["state"] = "disabled"

# ウィンドウ作成
root = tkinter.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])
# キャンバス作成
canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")
# ボタン配置
button_up = tkinter.Button(text="↑")
button_up.place(x=720, y=150)
button_up["command"] = click_button_up
button_down = tkinter.Button(text="↓")
button_down.place(x=720, y=210)
button_down["command"] = click_button_down
button_left = tkinter.Button(text="←")
button_left.place(x=660, y=180)
button_left["command"] = click_button_left
button_right = tkinter.Button(text="→")
button_right.place(x=780, y=180)
button_right["command"] = click_button_right

# 画像データを読み込み
images = [tkinter.PhotoImage(file="img6/chap6-mapfield.png"),
          tkinter.PhotoImage(file="img6/chap6-mapwall.png"),
          tkinter.PhotoImage(file="img6/chap6-mapgoal.png"),
          tkinter.PhotoImage(file="img6/chap6-mapkey.png"),
          tkinter.PhotoImage(file="img6/chap6-mapman.png")]

# マップデータ
MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 2, 0, 0, 1, 3, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# 主人公の位置
brave_x = 1
brave_y = 0
# 鍵取得フラグ
flag_key = False

draw_map()
root.mainloop()