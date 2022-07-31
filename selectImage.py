from monster_kari import monster

class SelectImage:
    #デンチュウの色と相手モンスターの組み合わせによって表示する画像を決める
    image = ''
    if monster.monsetrName == 'boss' and monster.denchuName == 'red':
        image = 'red_boss.png'
    elif monster.monsetrName == 'enemy' and monster.denchuName == 'red':
        image = 'red_enemy.png'
    elif monster.monsetrName == 'robot' and monster.denchuName == 'red':
        image = 'red_robot.png'
    elif monster.monsetrName == 'boss' and monster.denchuName == 'yellow':
        image = 'yellow_boss.png'
    elif monster.monsetrName == 'enemy' and monster.denchuName == 'yellow':
        image = 'yellow_enemy.png'
    elif monster.monsetrName == 'robot' and monster.denchuName == 'yellow':
        image = 'yellow_robot.png'
    elif monster.monsetrName == 'boss' and monster.denchuName == 'green':
        image = 'green_boss.png'
    elif monster.monsetrName == 'enemy' and monster.denchuName == 'green':
        image = 'green_enemy.png'
    elif monster.monsetrName == 'robot' and monster.denchuName == 'green':
        image = 'green_robot.png'