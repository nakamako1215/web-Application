
"""
# 麻雀の点数を出力(面前のみ)
print("麻雀の点数計算を行います。")
# 東場何本場か、南場何本場か
while True:
    try:
        ba = int(input("東場なら1、南場なら2を入力")) 
        if not 0< ba <=2:
            print("入力した値が違います。もう一度入力")
        else:
            break
    except ValueError as e:
        print("指示通り入力してください")

while True:
    try:                
        honba = int(input("親の継続回数を入力0～3"))
        if not 0 < honba <=3:
            print("入力した値が違います。もう一度入力")
        else:
            break
    except ValueError as e:
        print("指示通り入力してください")
# ステップ1：親の上がりか、子の上がりか
while True:
    try:                
        player = int(input("親の場合は1、子の場合は2を入力"))
        if not 0 < player <=2:
            print("入力した値が違います。もう一度入力")
        else:
            break
    except ValueError as e:
        print("指示通り入力してください")

# ステップ2：ロンかツモか
while True:
    try:                
        agari = int(input("ロンの場合1、ツモの場合2を入力"))
        if not 0 < agari <=2:
            print("入力した値が違います。もう一度入力")
        else:
            break
    except ValueError as e:
        print("指示通り入力してください")
        
# ステップ3：ツモの場合、一発、海底、嶺上開花か
while True:
    try:                
        if agari == 2:
            print("一発の場合1、海底の場合2、嶺上解放の場合は3を入力")
            tumori = int(input("->"))
            if not 0 < tumori <=3:
                print("入力した値が違います。もう一度入力")    
            else:
                break
    except ValueError as e:
        print("指示通り入力してください")
"""
list1 = list("1536723東北東")
print(list1)
print(sorted(list1))
ihan = [
    "門前清自摸和",
    "立直",
    "一発",
    "白",
    "発",
    "中",
    "場風牌",
    "自風牌",
    "平和",
    "一盃口",
    "タンヤオ",
    "嶺上開花",
    "槍槓",
    "海底摸月",
    "河底撈魚"
]

ryanhan = [
    "三色同順",
    "一気通貫",
    "チャンタ",
    "七対子",
    "対々和",
    "三暗刻",
    "三色同刻",
    "三槓子",
    "ダブル立直",
    "混老頭",
    "小三元"
]

sanhan = [
    "二盃口",
    "純チャン",
    "混一色"
]

rohan = [
    "清一色"
]

yakuman = [
    "清老頭",
    "国士無双",
    "四暗刻",
    "四槓子",
    "九蓮宝燈",
    "緑一色",
    "字一色",
    "天和",
    "地和"
]


# 追加要素、手配入力、（13牌）
"""
souzu = [1,2,3,4,5,6,7,8,9]
manzu = [1,2,3,4,5,6,7,8,9]
pinzu = [1,2,3,4,5,6,7,8,9]
kazehai = ["東","西","南","北"]
yakuhai = ["白","發","中"]
"""
