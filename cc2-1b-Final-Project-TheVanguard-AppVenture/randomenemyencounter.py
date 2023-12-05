import random
#Hero Classes
class Iso (object):
    name = "Iso"
    health = 25
    strength = 11
    defence = 15
    loot = random.randint(0,2)
class Jett (object):
    name = "Jett"
    health = 25
    strength = 11
    defence = 15
    loot = random.randint(0,2)
# Enemy Classes
class goblin (object):
    name = "Goblin"
    health = 30
    strength  = 22
    defence = 2
    loot = random.randint(0,2)

class bat (object):
    name = "Bat"
    health = 10
    strength = 32
    defence = 3
    loot = random.randint(0,2)

class troll (object):
    name = "Troll"
    health = 30
    strength = 23
    defence = 1.5
    loot = random.randint(0,2)

def gameOver(character, score):
    if character.health <1:
        print("You Died")
        print("Thanks for playing...")
        print("You have scored...",score)
        name = input("Type your name...")
        writeScore(score,name)

        file=open("score.txt","r")

        for line in file:
            xline = line.split(",")
            print(xline[0],":",xline[1])

        exit()

def writeScore(score, name):
    file = open("score.txt","a")
    file.write(str(name))
    file.write(",")
    file.write("\n")
    file.close()
def heroselect():
    print ("Select your hero!")
    selection = input("1. Iso \n2. Jett\nEnter your Choice: ")
    if selection == "1":
        character = Iso
        print ("You have selected the Iso... These are their stat...")
        print ("Health - ", character.health)
        print ("Strenght - ", character.strength)
        print ("Defence -", character.defence)

        return character

    elif selection == "2":
        character = Jett
        print ("You have selected Jett... These are their stat...")
        print ("Health - ", character.health)
        print ("Strenght - ", character.strength)
        print ("Defence -", character.defence)
        return character

    else:
        print("Only press 1 or 2")
        heroselect()
#input character++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def enemyselect(goblin,bat,troll):
    enemyList =[goblin,bat,troll]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print ("you drink the potion, increasing your health by 20!")
        print ("Your health is now", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength
        print ("you sharpened and upgrade your sword")
        print ("Your strength has been increased by 2")
        print ("your new strength is now", character.strength)
        return character

    elif lootDrop == "shield":
        character.strength = character.strength
        print ("you upgrade your shield")
        print ("Your shield protection has been increased by 2")
        print ("your new shield is now", character.defence)
        return character


def battlestate(score):
    enemy = enemyselect(goblin,bat,troll)
    print("a strong", enemy.name, "has appeared!")
    print("you have 3 options...")
    while enemy.health > 0:
        choice = input("1. Sword\n2. Laser Gun \n3. RUN!\nEnter your Choice:")
#sword+++++++++++==
        if choice == "1":
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

                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score = +  5

                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score = + 15

                    
                    print ("You have crushed the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    import Ending
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health = character.health
                print("You now only have", character.health, "remaining")
                gameOver(character, score)
#LASER gUN++++++++++++++++++++++++++++++

        if choice == "2":
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

                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score = + 5
                        
                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score = + 15
                        
                    print ("You have shot the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    import Ending
                    break
                    
                

            else:
                print("You didn't hit the enemy, the enemy is running so you miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health = enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)
#Run!+++++++++++++++++++++++++++==
        elif choice == "3":
            print("you try to run because you're gay ...")
            runchance = random.randint(1,10)
            if runchance > 4:
                print("You succesfully escaped!")
                break
            else:
                print("You got caught!")
                print("You try to defend yourself but cannot, the enemy hits you for full damaged...")
                character.health = character.health - enemy.strength
                print ("Your health is now", character.health)
                gameOver(character, score)

    else:
        print ("Invalid input, please only type the following")

score = random
character = heroselect()
score = battlestate(score)
print ("")
import main






