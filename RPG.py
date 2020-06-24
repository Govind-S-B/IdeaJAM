import random

hp = 100
kill_count = 0
enemy_hp = random.randint(8, 13)

Save_outer = {}

def Choose():
    
    x = input("Would u like to load a game ( y if yes )")

    if x == "y":
        Load()
    else:
        global Save_outer
        Save_outer={}


def Save():        
    Name = input("What would ur save file be called")
    Save_inner = {"hp":hp,
            "kill_count":kill_count,
            "enemy_hp":enemy_hp}
    Save_outer.update({Name:Save_inner})

    with open('Save.txt','w') as file:
        file.write(str(Save_outer))

def Load():
    global Save_outer
    global hp
    global kill_count
    global enemy_hp
    
    name = input("what is ur savefile name")
    
    with open('Save.txt','r') as file:
        Save_outer = eval(file.read())

    hp=Save_outer[name]["hp"]
    kill_count=Save_outer[name]["kill_count"]
    enemy_hp=Save_outer[name]["enemy_hp"]


Choose()

log = {
    'damage dealt': None,
    'damage taken': None,
    'health healed': None}


def create_new_enemy():
    global kill_count
    kill_count += 1
    global enemy_hp
    enemy_hp = random.randint(8, 13)


def fight():
    global enemy_hp
    dmg = random.randint(2, 5)
    enemy_hp -= random.randint(2, 5)
    log['damage dealt'] = dmg
    print('Damage dealt:', dmg)
    if enemy_hp <= 0:
        print('Enemy died')
        create_new_enemy()


def heal():
    global hp
    healing = random.randint(20, 30)
    hp += healing
##    log['health healed'] = healing
    if hp > 100:
        hp = 100


def enemy_attack():
    global hp
    dmg = random.randint(15, 35)
    hp -= dmg
    log['damage taken'] = dmg
    print('Damage taken:', dmg)


while hp > 0:
    player_option = input('Whatchu gon do?')
    if player_option == '1':
        fight()
        enemy_attack()
    if player_option == '2':
        heal()
        enemy_attack()
    if player_option == '3':
        Save()
    print('Health:', hp)
    print('Enemy health:', enemy_hp)
    

print('Oh! You died lol. But you killed:', kill_count, 'peeple tho')
input('press enter to close game')
