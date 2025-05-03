#1～10の数字をランダムに出していく相手に2～11の数時で勝負するプログラムを作成する
#ルール1：一度出した数字は出せない
#ルール2：ラウンド数と勝利数、敗北数、残りの手札、試合結果を毎回表示する
#ルール3：手札が無くなるまで繰り返し、最終の勝敗を表示する
#ルール4手札にないものを入力したらそのラウンドの最初に戻るようにする

import random

cpu = [1,2,3,4,5,6,7,8,9,10]

player = [2,3,4,5,6,7,8,9,10,11]
kakunin = []
turn = 0
win = 0
lose =0

while True:
    turn += 1
    print(f"round{turn}")
    
    print(f"自分の手札{player}")
    print(f"相手の手札{cpu}\n")
    
    while True:
        try:
            playercont = int(input("2～11を入力 ->"))
            if not 2 <= playercont <=112 :
                print("手札の範囲外です。もう一度入力")
            elif playercont not in player:
                print("その数字は既に利用しています。もう一度入力")
            else:
                break
        except:
            print("入力した値が違います。数字で入力してください")
        
        
    cpucont = random.choice(cpu)
    
    print(f"playerの手札'{playercont}',cpuの手札'{cpucont}'")
    if playercont > cpucont:
        print("playerの勝利\n")
        win += 1
    else:
        print("playerの敗北\n")
        lose

    player.remove(playercont)
    cpu.remove(cpucont)
    
    if player == []:
        break
    
if win > lose:
    print("最終結果：playerの勝利")
    
elif win < lose:
    print("最終結果playerの敗北")

else:
    print("最終結果：引き分け")