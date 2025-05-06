#1～10の数字をランダムに出していく相手に2～11の数時で勝負するプログラムを作成する
#ルール1：一度出した数字は出せない
#ルール2：ラウンド数と勝利数、敗北数、残りの手札、試合結果を毎回表示する
#ルール3：手札が無くなるまで繰り返し、最終の勝敗を表示する
#ルール4手札にないものを入力したらそのラウンドの最初に戻るようにする

#npcに法則性を追加する
#追加ルール１：npcが手札状況で絶対に勝てる数値がある場合、絶対に勝てる最小数値を出す。
#追加ルール２：逆にnpcが絶対に負ける数字があるとき、一番低い数値を出す

import random

cpu = [1,2,3,4,5,6,7,8,9,10] # npcの手札
player = [2,3,4,5,6,7,8,9,10,11] # playerの手札
turn = 0
win = 0
lose =0
i = 0

while True:
    turn += 1
    print(f"round{turn}")
    print(f"勝利数{win}")
    print(f"敗北数{lose}")
    print(f"自分の手札{player}")
    print(f"相手の手札{cpu}\n")
    
    while True:
        try:
            playercont = int(input("2～11を入力 ->"))
            if not 2 <= playercont <=11 :
                print("手札の範囲外です。もう一度入力")
            elif playercont not in player:
                print("その数字は既に利用しています。もう一度入力")
            else:
                break
        except:
            print("入力した値が違います。数字で入力してください")
        
        
    #cpucont = random.choice(cpu) # cpuリストの中からランダムで選ぶ
    #新機能の追加、もし、playercontの数値よりも大きいものがあったら
    #その数値の一つ上のリストの中身を表示する。
    #もしその数値がなかったら、リストの一番下から出力する
    for i in range(len(player)):
        if playercont < cpu[i]:
            cpucont = cpu[i]
            break
        elif playercont > cpu[i]:
            cpucont = cpu[0]
        
    print(f"playerの手札'{playercont}',cpuの手札'{cpucont}'")
    if playercont > cpucont:
        print("playerの勝利\n")
        win += 1
    elif playercont < cpucont:
        print("playerの敗北\n")
        lose +=1
    else:
        print("引き分け")

    player.remove(playercont)
    cpu.remove(cpucont)
    
    if player == []:
        break
    
if win > lose:
    print("最終結果：playerの勝利")
    
elif win < lose:
    print("最終結果：playerの敗北")

else:
    print("最終結果：引き分け")