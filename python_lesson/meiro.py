
meize = [0,1,2]  # meiroの迷路のサイズ
kaiso = 0 # 現在の階層



def goal(meize):
    miti = int(input("右=0 左=1 前=2 ->"))
    def kaisoidou(kaiso):
        if meize[kaiso] == miti:
            kaiso += 1
            print(f"正解！現在{kaiso}階層")
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