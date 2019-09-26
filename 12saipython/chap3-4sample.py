string  = input("求めたい分を入力してください：")
minutes = float(string)
hours   = round(minutes / 60, 2)
def minutes_to_hours():
    output = string + "分は" + str(hours) + "時間です"
    print(output)
minutes_to_hours()