
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
