

#scrapppppppppppppppppppppppppppppppp




import random
import heroselection
#Hero Classes
class Iso (object):
    Heroname = "Iso"
    health = 25
    strength = 11
    defence = 15
    loot = random.randint(0,2)
class Jett (object):
    Heroname = "Jett"
    health = 25
    strength = 11
    defence = 15
    loot = random.randint(0,2)
# Enemy Classes
class goblin (object):
    enemy = "Goblin"
    health = 30
    strength  = 22
    defence = 2
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
    #input character++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def enemyselect(goblin):
    enemyList =[goblin]
    

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
    enemy = enemyselect(goblin)
    print("a strong", goblin, "has appeared!")
    print("you have 3 options...")
    while goblin.health > 0:
        choice = input("1. Sword\n2. Laser Gun\nEnter your Choice:")
#sword+++++++++++==
        if choice == "1":
            print ("You swing your sword, attacking the", goblin)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                goblin.health = goblin.health - character.strength
                print ("you hit the enemy, their health is now....", goblin.health)

                if enemy.health > 0:
                    character.health = character.health - (goblin.strength / character.defence)
                    print ("The", goblin, "takes a swing, it hits you leaving", character.health)
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
                    import ending
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health = character.health
                print("You now only have", character.health, "remaining")
                gameOver(character, score)
#LASER gUN++++++++++++++++++++++++++++++

        if choice == "2":
            print ("You shoot him with Laser Gun, attacking the", goblin)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                goblin.health = goblin.health - character.strength
                print ("you hit the enemy, their health is now....",goblin.health)

                if goblin.health > 0:
                    character.health = character.health - (goblin.strength / character.defence)
                    print ("The", gobliny.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                else:
                    if goblin.name == "Goblin":
                        goblin.health = 20
                        score = score = + 10

                    
                    print ("You have shot the", goblin)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    import ending
                    break
                    
                

            else:
                print("You didn't hit the enemy, the enemy is running so you miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health = enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)
#Run!+++++++++++++++++++++++++++==
       

    else:
        print ("Invalid input, please only type the following")

score = random
battlestate(score)
print ("")






