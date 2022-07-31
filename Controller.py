class Controller:
    def __init__(self, model):
        self.model = model
        

    def onPress(self,key):#ボタンが押された時の処理
        if key in "赤色デンチュウ" :
            self.model.setMonster("denchu_red") #モンスターの確定選択画面に移動する pass

        elif key in "緑色デンチュウ" :
            self.model.setMonster("denchu_green") #モンスターの確定選択画面に移動する pass

        elif key in "黄色デンチュウ" :
            self.model.setMonster("denchu_yellow") #モンスターの確定選択画面に移動する pass

        elif key in "赤色デンチュウに決めた！" : 
            self.model.setMonster("denchu_red") #赤色デンチュウのインスタンスを生成

        elif key in "緑色デンチュウに決めた！" :
            self.model.setMonster(denchu_green) #緑色デンチュウのインスタンを生成

        elif key in "黄色デンチュウに決めた！" :
            self.model.setMonster(denchu_yellow) #黄色デンチュウのインスタンスを生成

        elif key in "選び直す！" : 
            pass #デンチュウの選択画面に戻る pass
        
        elif key in "おでん" or key in "バッテリー":
            self.model.activateItem(key) #選んだデンチュウの体力を20回復する

        elif key in "戦う" :
            self.model.selectFight(key) #技選択画面に移動する pass

        elif key in "逃げる!" :
            pass #ゲームを終了し、敗北テキストが表示される pass

        elif key in "戻る" :
            pass #前の画面に戻る pass

        #elif key in "技1" or key in "技2" or key in "技3" or key in "技4":
            #self.model.selectFight(key) #モンスターの技リストから技１を使用する

        elif key in "保存する":
            self.model.writeStatus(self.model.player.monster, self.model.computer.monster)

        else :
            self.model.selectFight(key)