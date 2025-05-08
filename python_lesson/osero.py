
#〇×ゲーム
#必要な要素

#盤面を作る
class Banmen:
    def __init__(self):
        self.banmen = [['','',''],  #[0][0],[0][1],[0][2]
                       ['','',''],  #[1][0],[1][1],[1][2]
                       ['','','']]  #[2][0],[2][1],[2][2]
#盤面に〇と×を付ける(盤面を更新する)
    def update(self,p1_0,p1_1,p2_0,p2_1):
        self.banmen[p1_0][p1_1] = '〇'
        self.banmen[p2_0][p2_1] = '✕'
#どこに〇と×を付けるのか、出力を受け取る。
class nyuryoku:
    def __init__(self):
        while True:
            try:
                #ここでの条件。リストの範囲を超える数値を書かせない。
                #書いた場合はもう一度書かせる。文字列も同様に
                #既に〇か×がある場合ももう一度書かせる。
                self.p1_0 = int(input(f"player1の数値を入力(行(横))\n"))
                self.p1_1 = int(input(f"player1の数値を入力(縦(列))\n"))
                if self.banmen[self.p1_0][self.p1_1] == '〇' or self.banmen[self.p2_0][self.p2_1] == '✕':
                    print('既に書かれています。もう一度書き直してください')
                self.p2_0 = int(input(f"player2の数値を入力((行(横))\n"))
                self.p2_1 = int(input(f"player2の数値を入力(縦(列))\n"))
                if self.banmen[self.p2_0][self.p2_1] == '✕' or self.banmen[self.p2_0][self.p2_1] == '〇':
                    print('既に書かれています。もう一度書き直してください')
            

#縦横斜めに３つ〇もしくはxを付けたら勝利と出力、やられたらxと出力、

#最大9回この工程をくりかえす


if __name__== "__main__":
    x = Banmen()
    while True:
        
        
        for row in x.banmen:
            print(row)
        
        y = nyuryoku()
        x.update(y.p1_0,y.p1_1,y.p2_0,y.p2_1)