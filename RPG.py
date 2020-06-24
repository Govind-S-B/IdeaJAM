import random

hp = 100
kill_count = 0
enemy_hp = 0

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
    if enemy_hp < 0:
        create_new_enemy()


def heal():
    global hp
    healing = random.randint(20, 30)
    hp += healing
    log['health healed'] = healing


def enemy_attack():
    global hp
    dmg = random.randint(15, 35)
    hp -= dmg
    log['damage taken'] = dmg


create_new_enemy()
print(enemy_hp)
