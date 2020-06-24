import random

hp = 100
kill_count = 0
enemy_hp = random.randint(8, 13)

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
    log['health healed'] = healing
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
    if player_option == '2':
        heal()
    enemy_attack()
    print('Health:', hp)
    print('Enemy health:', enemy_hp)

print('Oh! You died lol. But you killed:', kill_count, 'peeple tho')
