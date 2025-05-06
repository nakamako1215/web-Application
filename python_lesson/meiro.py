import random

meize = []  # meiroの階層はランダム指定
kaiso = 0 # 現在の階層
touha = False # 階層を踏破したことがあるのかの判定
maizesize = 0
seikai = [] # 一度踏破した階層の答え
# 迷路のサイズ指定
while True:
    try:
        maizesize = int(input("迷路のサイズを入力 ->"))
        if maizesize <=3:
           print("入力範囲外です") 
        break
    except:
        print("入力した値が違います")

# 迷路の中身（道順をランダムで決める）
for i in range(maizesize):
    i = random.randint(0,2)
    meize.append(i)

#もし現在の階層(kaiso)にseikai[kaiso]番目の要素があったらこれを表示する

#正解の道を選んだらseikai[kaiso]番目にmitiを代入（道の記録)
#もし既に記録してある場合は記録しない

def goal(meize):
    try:
        #既にseikaiに正しい道のりが入っていた場合に階層の答えを教える
        if seikai[kaiso] == meize[kaiso]:
            print(f"この階層の答えは{seikai[kaiso]}")
    except:
        print("踏破していない階層")
    miti = int(input("右=0 左=1 前=2 ->"))
    def kaisoidou(kaiso):
        if meize[kaiso] == miti: 
            kaiso += 1
            seikai.append(miti)
            print(f"正解！現在{kaiso}階層")
            #もしseikaiの要素数が現在の階層よりも大きかったら追加した道のりを上から消す
            if len(seikai) > kaiso:
                seikai.pop(-1)          
        else:
            
            kaiso = 0 
        return kaiso
    return kaisoidou(kaiso)   

while True:
    if len(meize) == kaiso:
        break
    kaiso = goal(meize)
    
    if kaiso == 0:
        print("振り出しに戻る")
            
print("脱出成功")