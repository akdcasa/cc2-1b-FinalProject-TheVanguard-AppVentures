import random

class Iso(object):
    def __init__(self):
        self.name = "Iso"
        self.health = 25
        self.strength = 11
        self.defence = 15
        self.loot = random.randint(0, 2)

class Jett(object):
    def __init__(self):
        self.name = "Jett"
        self.health = 25
        self.strength = 11
        self.defence = 15
        self.loot = random.randint(0, 2)

class Goblin(object):
    def __init__(self):
        self.name = "Goblin"
        self.health = 30
        self.strength = 22
        self.defence = 2
        self.loot = random.randint(0, 2)

def gameOver(character, score):
    if character.health < 1:
        print("You Died")
        print("Thanks for playing...")
        print("You have scored...", score)
        name = input("Type your name...")
        writeScore(score, name)

        file = open("score.txt", "r")

        for line in file:
            xline = line.split(",")
            print(xline[0], ":", xline[1])

        exit()

def writeScore(score, name):
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write("\n")
    file.close()

def enemyselect():
    enemy= [Goblin]


def loot():
    loot_items = ["potion", "sword", "shield"]
    loot_drop = random.choice(loot_items)
    return loot_drop

def lootEffect(loot_drop, character):
    if loot_drop == "potion":
        character.health += 20
        print("You drink the potion, increasing your health by 20!")
        print("Your health is now", character.health)
        return
    elif loot_drop == "sword":
        character.strength += 2
        print("You sharpen and upgrade your sword")
        print("Your strength has been increased by 2")
        print("Your new strength is now", character.strength)
        return
    elif loot_drop == "shield":
        character.defence += 2
        print("You upgrade your shield")
        print("Your shield protection has been increased by 2")
        print("Your new shield is now", character.defence)
        return
def battlestate(score):
    character = Iso()  # Choose either Iso() or Jett() here
    enemy = Goblin()
    print("A strong", enemy.name, "has appeared!")
    print("You have 2 options...")
    while enemy.health > 0:
        choice = input("1. 𝕊 𝕨 𝕠 𝕣 𝕕\n2. 𝕃 𝕒 𝕤 𝕖 𝕣  𝔾 𝕦 𝕟 \nEnter your Choice:")
        if choice == "1":
             if choice == "1":
               print ("┏━━━                  ━━━┓")
               print ("| (｀▽´)=o==[]::::::::::>|")
               print ("┗━━━                  ━━━┛")
               print ("You swing your sword, attacking the", enemy.name)
               hitchance = random.randint(0,10)
             if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("you hit the enemy, their health is now....", enemy.health)
                
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score = + 10


                    print ("You have crushed the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                  
        elif choice == "2":
            print ("┏━━━                  ━━━┓")
            print ("| ( う-´)づ︻╦̵̵̿╤── ooooooo |")     
            print ("┗━━━                  ━━━┛")
            print ("You shoot him with Laser Gun, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("you hit the enemy, their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score = + 10

                    print ("You have shot the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    

            else:
                print("You didn't hit the enemy, the enemy is running so you miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health = enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)
            # Implement laser gun logic
            pass
        else:
            print("Invalid input. Please choose 1 or 2")
score = 0
battlestate(score)
import end
