import random
from select import select
from sys import platlibdir
from tokenize import String

# トレーナークラス
# 敵トレーナーとプレイヤーの親クラス
class Trainer:
    def __init__(self):             #コンストラクタ
        self.trainerName = ""       #名前の初期化

# 敵クラス
# トレーナークラスの子クラス
# 名前, モンスターを持っている
# 戦うことだけできる
class Opponent(Trainer):
    def __init__(self):             #コンストラクタ
        super().__init__()          #親クラス(Trainerクラス)を継承
        self.trainerName = "コンピュータ"      #トレーナー名はコンピュータで固定する
        self.entities = ["robot", "enemy", "boss"]      #モンスターはこの一覧から選ぶ
        self.monster = Monster(None)
        self.num = random.randint(0,2)

    #敵が持つモンスターを選択するメソッド
    def selectMonster(self):
        self.monster = Monster(self.entities[self.num])    #モンスター一覧からランダムで選ぶ
        self.monster.color = self.monster.setColor(self.monster.monsterName)    #選んだモンスターの属性を決める
        self.monster.skills = self.monster.setSkills(self.monster.color)        #モンスターが持つ技を設定する
    
    # モンスターを戦わせるメソッド
    def fight(self, executer:None, target:None):
        executer.useSkill(executer, target, random.choice(self.monster.skills)) #技を使う


# プレイヤー(ユーザが操作する)クラス
# トレーナークラスの子クラス
# 名前, モンスター, アイテムを持っている
# 戦う, アイテムを使用する, 逃げることができる
class Player(Trainer):
    def __init__(self):             #コンストラクタの生成
        super().__init__()
        self.trainerName = "プレイヤー"     #名前はプレイヤーで固定する
        self.items = Item()         #アイテムを設定する
        self.monster = Monster(None)
    
    # モンスターを選択するメソッド
    def selectMonster(self, key):
        self.monster = Monster(key)         #受け取ったモンスターの名前のモンスターを選ぶ
        self.monster.color = self.monster.setColor(self.monster.monsterName)    #選んだモンスターの名前から属性を設定する
        self.monster.skills = self.monster.setSkills(self.monster.color)        #選んだモンスターの属性からモンスターの技を設定する

    # モンスターを戦わせるメソッド
    def fight(self, executer, target, selectCommand):
        executer.useSkill(executer, target, selectCommand)  # 選択した技を使用する

    # アイテムを使用するメソッド
    def useItem(self, selectItem):
        self.items.skillActivation(selectItem, self.monster)    # 選択したアイテムを使用する

    # 逃げる時のメソッド
    def escape():
        pass

#アイテムクラス
class Item:
    def __init__(self):
        self.itemNames = ["おでん", "バッテリー"]
        self.healAmount = 30
        self.addAmount = 5

    def skillActivation(self, selectItem, target):
        if selectItem == "おでん":
            target.heal(self.healAmount)
            self.itemNames[0] = "---"
        elif selectItem == "バッテリー":
            target.addPower(self.addAmount)
            self.itemNames[1] = "---"


class Monster:
    def __init__(self, name):
        self.monsterName = name
        self.color = ""
        self.hp = 100
        self.maxHP = self.hp
        self.power = 12
        self.speed = 10
        self.items = [0,1]
        self.dead = False
        self.skills = []
        self.damage = 0
    
    def setColor(self, name):
        if name == "denchu_red" or name == "boss":
            self.color = "RED"
        elif name == "denchu_green" or name == "robot":
            self.color = "GREEN"
        elif name == "denchu_yellow" or name == "enemy":
            self.color = "YELLOW"

    def setSkills(self, color):
        self.skill1 = SpeSkill("普通のパンチ", "WHITE", 1, 1)
        self.skill2 = SpeSkill("マジ殴り", "WHITE", 1.3, 0.8)
        self.skill3 = SpeSkill("", "", 0, 0)
        self.skill4 = SpeSkill("", "", 0, 0)
        if color == "RED":
            self.skill3 = SpeSkill("きゅうれんぽうとう", "RED", 1.2, 0.9)
            self.skill4 = SpeSkill("ヨガファイヤー", "RED", 1.5, 0.7)
            # self.skills = [self.skill1, self.skill2, self.skill3, self.skill4]
        elif color == "GREEN":
            self.skill3 = SpeSkill("リューイーソー", "GREEN", 1.2, 0.9)
            self.skill4 = SpeSkill("サンフラワー", "GREEN", 1.5, 0.7)
            # self.skills = [self.skill1, self.skill2, self.skill3, self.skill4]
        elif color == "YELLOW":
            self.skill3 = SpeSkill("チートイ", "YELLOW", 1.2, 0.9)
            self.skill4 = SpeSkill("100万ボルト", "YELLOW", 1.5, 0.7)
            # self.skills = [self.skill1, self.skill2, self.skill3, self.skill4]
        self.skills.append(self.skill1)
        self.skills.append(self.skill2)
        self.skills.append(self.skill3)
        self.skills.append(self.skill4)
        return self.skills

    def useSkill(self, executer, target, selectCommand):
        if executer.monsterName == "denchu_red" or executer.monsterName == "denchu_green" or executer.monsterName == "denchu_yellow":
            # selectSkill = executer.skills[selectCommand]
            # executer.attackDamage(target, selectSkill)
            executer.attackDamage(target, executer.skills[int(selectCommand)])
        elif executer.monsterName == "boss" or executer.monsterName == "robot" or executer.monsterName == "enemy":
            # selectSkill = executer.skills[random.randint(0,4)]
            # executer.attackDamage(target, selectSkill)
            executer.attackDamage(target, selectCommand)

    def attackDamage(self, target, selectSkill):
        if random.choices(target.items, weights=[(1-selectSkill.hit), selectSkill.hit], k=1):
            if selectSkill.skillColor == "RED" and target.color == "GREEN":
                self.damage = int(self.power * selectSkill.might * 2)
            elif selectSkill.skillColor == "RED" and target.color == "YELLOW":
                self.damage = int(self.power * selectSkill.might * 0.5)
            elif selectSkill.skillColor == "GREEN" and target.color == "YELLOW":
                self.damage = int(self.power * selectSkill.might * 2)
            elif selectSkill.skillColor == "GREEN" and target.color == "RED":
                self.damage = int(self.power * selectSkill.might * 0.5)
            elif selectSkill.skillColor == "YELLOW" and target.color == "RED":
                self.damage = int(self.power * selectSkill.might * 2)
            elif selectSkill.skillColor == "YELLOW" and target.color == "GREEN":
                self.damage = int(self.power * selectSkill.might * 0.5)
            self.recieveDagame(target, self.damage)


    def recieveDagame(self, target, damage):
        target.hp -= damage
        target.isDead(target)

    def heal(self, healAmount):
        if self.hp >= self.maxHP - 30:
            self.hp = self.maxHP
        else:
            self.hp += healAmount

    def addPower(self, addAmount):
        self.power += addAmount

    def disapper():
        pass

    def isDead(self, target):
        if target.hp <= 0:
            target.dead = True


class SpeSkill:
    def __init__(self, name, skillColor, might, hit):
        self.skillName = name
        self.skillColor = ""
        self.might = 0
        self.hit = 0
    

class Model:
    def __init__(self,view):
        self.view = view
        self.player = Player()
        self.computer = Opponent()
        self.items = Item()
    

    def setMonster(self, key):
        self.player.selectMonster(key)
        self.computer.selectMonster()

    def selectFight(self, selectCommand):
        # if self.player.monster.speed < self.computer.monster.speed:
        #     self.computer.fight(self.computer.monster, self.player.monster)
        #     self.player.fight(self.player.monster, self.computer.monster, selectCommand)
        # else:
        #     self.player.fight(self.player.monster, self.computer.monster, selectCommand)
        #     self.computer.fight(self.player.monster, self.player.monster)
        self.player.fight(self.player.monster, self.computer.monster, selectCommand)
        self.computer.fight(self.computer.monster, self.player.monster)

    def activateItem(self, item):
        self.player.useItem(item)

    def selectEscape():
        pass

    def writeStatus(self, target1, target2):
        with open("Status.py", 'w') as f:
            f.write("class Stutas:\n")
            f.write("   " + "denchuHP = " + str(target1.hp) + "\n")
            f.write(f"   denchuName = '{target1.monsterName}' \n")
            f.write("   " + "monsterHP = " + str(target2.hp) + "\n")
            f.write(f"   monsterName = '{target2.monsterName}' \n")