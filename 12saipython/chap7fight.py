import tkinter
import random
import time

class FightManager:
    # コンストラクタ
    def __init__(self):
        self.dialog = tkinter.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)
        self.canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, 620, 434, fill="black")
        # ボタン作成
        self.fbutton = tkinter.Button(self.dialog, text="攻撃")
        self.fbutton.place(x=180, y=340)
        self.fbutton["command"] = self.click_fight
        self.rbutton = tkinter.Button(self.dialog, text="力をためる")
        self.rbutton.place(x=320, y=340)
        self.rbutton["command"] = self.click_reserve
        # 画像の読み込み
        self.images = [
            tkinter.PhotoImage(file="img6\chap7-monseter1.png"),
            tkinter.PhotoImage(file="img6\chap7-monster2.png")
        ]
        self.canvas.create_image(180, 160, image=self.images[0])
        # ラベルを配置
        self.label = tkinter.Label(self.dialog, text="ラベル",
            fg="white", bg="black", justify="left")
        self.label.place(x=360, y=10)
        # 非表示
        self.dialog.place_forget()
    # 戦闘開始
    def fight_start(self, map_data, x, y, brave):
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
        self.brave = brave
        # モンスターの画像を表示
        p = self.map_data[y][x]
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 620, 434, fill="black")
        self.canvas.create_image(180, 160, image=self.images[p-5])
        self.label["text"] = ""
        # モンスターのオブジェクトを作成
        if p == 5:
            self.monster = Monster1()
        elif p == 6:
            self.monster = Monster2()
        self.label["text"] = self.monster.name + "が現れた"
    # 攻撃ボタン
    def click_fight(self):
        self.fbutton["state"] = "disabled"
        self.rbutton["state"] = "disabled"
        self.do_turn(self.brave.get_atk())
    # 力をためるボタン
    def click_reserve(self):
        self.fbutton["state"] = "disabled"
        self.rbutton["state"] = "disabled"
        self.brave.reserve()
        self.do_turn(-1)
    # 戦闘処理
    def do_turn(self, brave_atk):
        # 主人公のターン
        monster_dfs = self.monster.get_dfs()
        if brave_atk < 0:
            labeltext = "勇者は力をためた"
        else:
            labeltext = "勇者は攻撃した"
            self.label["text"] = labeltext
            self.dialog.update()
            # 主人公の攻撃の結果表示
            time.sleep(2) #2秒待ち
            dmg = brave_atk - monster_dfs
            self.monster.culc_hp(brave_atk, monster_dfs)
            if dmg <= 0:
                labeltext = labeltext + "\n防がれた"
            else:
                labeltext = labeltext + "\n" + str(dmg) + \
                    "のダメージを与えた"
        # ラベル更新、残り体力表示
        self.label["text"] = labeltext
        self.dialog.update()
        time.sleep(2) #2秒待ち
        labeltext = labeltext + \
            "\nモンスターの残り体力は" + str(self.monster.hp)
        self.label["text"] = labeltext
        self.dialog.update()
        if self.monster.hp < 1:
            time.sleep(2) #2秒待ち
            self.fbutton["state"] = "normal"
            self.rbutton["state"] = "normal"
            self.fight_win()
            return
        # モンスターのターン
        time.sleep(2) #2秒待ち
        brave_dfs = self.brave.get_dfs()
        if random.random() < 0.2:
            labeltext = labeltext + "\n\nモンスターは力をためた"
            self.monster.reserve()
        else:
            labeltext = labeltext + "\n\nモンスターの攻撃"
            self.label["text"] = labeltext
            self.dialog.update()
            # モンスターの攻撃の結果表示
            time.sleep(2) #2秒待ち
            monster_atk = self.monster.get_atk()
            dmg = monster_atk - brave_dfs
            self.brave.culc_hp(monster_atk, brave_dfs)
            if dmg <= 0:
                labeltext = labeltext + "\n防いだ"
            else:
                labeltext = labeltext + "\n" + str(dmg) + \
                    "のダメージを受けた"
        # ラベル更新、残り体力表示
        self.label["text"] = labeltext
        self.dialog.update()
        time.sleep(2) #2秒待ち
        labeltext = labeltext + \
            "\n勇者の残り体力は" + str(self.brave.hp)
        self.label["text"] = labeltext
        self.dialog.update()
        if self.brave.hp < 1:
            time.sleep(2) #2秒待ち
            self.fight_lose()
        else:
            # ボタンを有効化して次のターンへ
            self.fbutton["state"] = "normal"
            self.rbutton["state"] = "normal"
    # 勝利
    def fight_win(self):
        self.map_data[self.brave_y][self.brave_x] = 0
        self.dialog.place_forget()
    # 敗北
    def fight_lose(self):
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="red")
        canvas.create_text(300, 200,
            fill="white", font=("MS ゴシック", 15),
            text="""勇者は負けてしまった。
最初からやり直してくれたまえ。""")

# キャラクターの親クラス
class Character:
    # コンストラクタ
    def __new__(cls):
        obj = super().__new__(cls)
        obj.rsv = 1
        return obj
    # 力をためる
    def reserve(self):
        self.rsv = self.rsv + 1
    # 攻撃力を求める
    def get_atk(self):
        r = self.rsv
        self.rsv = 1
        return random.randint(1, self.atk * r)
    # 防御力を求める
    def get_dfs(self):
        return random.randint(0, self.dfs)
    # 体力計算
    def culc_hp(self, atk, dfs):
        dmg = atk - dfs
        # ダメージなし
        if dmg < 1:
            return self.hp
        # 体力を減らす
        self.hp = self.hp - dmg
        if self.hp < 1:
            self.hp = 0
        return self.hp

# 勇者クラス
class Brave(Character):
    def __init__(self):
        self.name = "勇者ハル"
        self.hp = 30
        self.atk = 15
        self.dfs = 10
# モンスター1
class Monster1(Character):
    def __init__(self):
        self.name = "マコデビル"
        self.hp = 20
        self.atk = 15
        self.dfs = 5
# モンスター2
class Monster2(Character):
    def __init__(self):
        self.name = "リリースネーク"
        self.hp = 10
        self.atk = 8
        self.dfs = 5