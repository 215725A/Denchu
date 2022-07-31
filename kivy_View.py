from ctypes.wintypes import SMALL_RECT
import datetime
from modulefinder import Module
from tokenize import String

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
#from kivy.uix.label import Label
from Model import Model
from Controller import Controller
from monster_kari import monster
from Status import Status
from selectImage import SelectImage


####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

#ウィンドウサイズの定義
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'resizable', 1)


class SelScreen(Screen): #モンスター選択画面のクラス
    color = ''
    def __init__(self, **kwargs):
        super(SelScreen, self).__init__(**kwargs)
        
    def pressRed(self):
        self.color = "赤色デンチュウ"
        
    def pressyellow(self):
        self.color = '黄色デンチュウ'
    
    def pressGreen(self):
        self.color = '緑色デンチュウ'
        
class DecScreen_red(Screen): #赤デンチュウ決定画面のクラス
    back = ''
    color = ''
    def __init__(self, controller, **kwargs):
        super(DecScreen_red, self).__init__(**kwargs)
        self.controller = controller
        
    def pressBack(self):
        self.back = '選び直す!'
        
    def pressSelect(self, color):
        self.color = '赤色デンチュウ' 
        self.controller.onPress(color)
        self.controller.onPress("保存する")

        
class DecScreen_yellow(Screen):#黄デンチュウ決定画面のクラス
    back = ''
    color = ''
    def __init__(self, controller, **kwargs):
        super(DecScreen_yellow, self).__init__(**kwargs)
        self.controller = controller
        
    def pressBack(self):
        self.back = '選び直す!'
        
    def pressSelect(self):
        self.color = '黄色デンチュウ'
        self.controller.onPress(self.color)
        self.controller.onPress("保存する")
        
class DecScreen_green(Screen): #緑色デンチュウ決定画面のクラス
    back = ''
    color = ''
    def __init__(self, controller, **kwargs):
        super(DecScreen_green, self).__init__(**kwargs)
        self.controller = controller

    def pressBack(self):
        self.back = '選び直す!'
        
    def pressSelect(self):
        self.color = '緑色デンチュウ'
        self.controller.onPress(self.color)
        self.controller.onPress("保存する")
        
class BatScreen(Screen): #戦闘画面のクラス
    def __init__(self, controller, **kwargs):
        super(BatScreen, self).__init__(**kwargs)
        self.controller = controller
    
    
        Image = StringProperty(SelectImage.image)
        den_HP = StringProperty(str(controller.model.player.monster))
        mon_HP = StringProperty(str(Status.monsterHP))
        denName = StringProperty(Status.denchuName)
        oppName = StringProperty(Status.monsterName)
        
class SkillScreen(Screen): #スキル選択画面のクラス
    BatScreen.Image = StringProperty(SelectImage.image)
    den_HP = StringProperty(str(Status.denchuHP))
    mon_HP = StringProperty(str(Status.monsterHP))
    denName = StringProperty(Status.denchuName)
    oppName = StringProperty(Status.monsterName)
    calc = 10
    damage = StringProperty(str(calc))
    #技１〜４を入れる変数
    First = '普通のパンチ'
    Third = '3'
    Fourth = '4'
    skill1 = StringProperty(First)
    skill2 = StringProperty('マジ殴り')
    skill3 = StringProperty(Third)
    skill4 = StringProperty(Fourth)
    #テキストを保存する変数
    skillText1 = StringProperty('技を選択してください。')
    skillText2 = StringProperty('')
    def __init__(self, controller, **kwargs):
        super(SkillScreen, self).__init__(**kwargs)
        self.controller = controller
    
    def pressSkill1(self): #技1を押すとそれに応じてテキストの内容を更新
        self.skillText1 = 'いけ！普通のパンチだ！'
        self.skillText2 = '相手モンスターに30ダメージ!'
        self.controller.onPress(self.First)
        
    def pressSkill2(self): #技2を押すとそれに応じてテキストの内容を更新
        self.skillText1 = 'いけ!マジ殴り'
        self.skillText2 = '相手モンスターに30ダメージ!'
        
    def pressSkill3(self): #技3を押すとそれに応じてテキストの内容を更新
        self.skillText1 = 'いけ!' + self.skill3 + 'だ！'
        self.skillText2 = '相手モンスターに'+self.damage+'ダメージ!'
        
    def pressSkill4(self): #技4を押すとそれに応じてテキストの内容を更新
        self.skillText1 = 'いけ!' + self.skill4 + 'だ！'
        self.skillText2 = '相手モンスターに'+self.damage+'ダメージ!'
         
class AitemScreen(Screen): #アイテムを選択する画面
    Image = StringProperty(SelectImage.image)
    den_HP = StringProperty(str(monster.denchuHP))
    mon_HP = StringProperty(str(monster.monsterHP))
    denName = StringProperty(monster.denchuName)
    oppName = StringProperty(monster.monsetrName)
    use_oden = ''
    use_Bat = ''
    #テキストを保存する変数
    aitemText1 = StringProperty()
    aitemText2 = StringProperty()
    def __init__(self, **kwargs):
        super(AitemScreen, self).__init__(**kwargs)
        self.aitemText1 = ''
        self.aitemText2 = '使用するアイテムを選択してください。'
    
    #押したボタンに応じてテキストの内容を更新するためのメソッド    
    def pressOden(self):
        self.aitemText1 = 'おでんを使用！'
        self.aitemText2 = 'デンチュウのHPが30回復!'
        self.use_oden = 'use'
        
    def pressBatt(self):
        self.aitemText1 = 'バッテリーを使用！'
        self.aitemText2 = '次のターンの攻撃力が上昇！'
        self.use_Bat = 'use'    

#逃げる選択画面    
class EscapeScreen(Screen):
    Image = StringProperty(SelectImage.image)
    den_HP = StringProperty(str(monster.denchuHP))
    mon_HP = StringProperty(str(monster.monsterHP))
    denName = StringProperty(monster.denchuName)
    oppName = StringProperty(monster.monsetrName)
    back = StringProperty()
    escape = StringProperty()
    def __init__(self, **kwargs):
        super(EscapeScreen, self).__init__(**kwargs)
        
    def pressBack(self):
        self.back = ('')
    def pressEscape(self):
        self.escape = ('')

#逃げるを実行したことにより敗北を通知する画面        
class EscDefeatScreen(Screen):
    Image = StringProperty(SelectImage.image)
    den_HP = StringProperty(str(monster.denchuHP))
    mon_HP = StringProperty(str(monster.monsterHP))
    denName = StringProperty(monster.denchuName)
    oppName = StringProperty(monster.monsetrName)
    escDefeatText = StringProperty('戦闘から離脱しました。')
    def __init__(self, **kwargs):
        super(EscDefeatScreen, self).__init__(**kwargs) 
        
    def pressButton(self):
        self.escDefeatText = '戦闘は終了しています。ウィンドウを閉じて再挑戦してください。'
        
class EnemyTurnScreen(Screen):
    selectSkill = StringProperty('技１')
    Image = StringProperty(SelectImage.image)
    den_HP = StringProperty(str(monster.denchuHP))
    mon_HP = StringProperty(str(monster.monsterHP))
    denName = StringProperty(monster.denchuName)
    oppName = StringProperty(monster.monsetrName)
    
    def __init__(self, **kwargs):
        super(EnemyTurnScreen, self).__init__(**kwargs)

    

#メインメソッドのようなもの        
class drawApp(App):
    def __init__(self, **kwargs):
        super(drawApp, self).__init__(**kwargs)
        self.title='DENCHU'
        view = SelScreen()
        model = Model(view)
        self.controller = Controller(model)
        
        

    def build(self):
        # Create the screen manager
        SM = ScreenManager()
        SM.add_widget(SelScreen(name='select'))
        SM.add_widget(DecScreen_red(self.controller, name='decision_red'))
        SM.add_widget(DecScreen_yellow(self.controller, name='decision_yellow'))
        SM.add_widget(DecScreen_green(self.controller, name='decision_green'))
        SM.add_widget(BatScreen(self.controller, name='battle'))
        SM.add_widget(SkillScreen(self.controller, name='skill'))
        SM.add_widget(AitemScreen(name='aitem'))
        SM.add_widget(EscapeScreen(name='escape'))
        SM.add_widget(EscDefeatScreen(name='esc_defeat'))
        SM.add_widget(EnemyTurnScreen(name='enemy_turn'))
        return SM
    
if __name__ == '__main__':
    drawApp().run()