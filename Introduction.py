import time
  
def startGame():
    print()

line1 = "========================================================================================================================"
for char in line1:
    print(char, end='')
    time.sleep(.01)

time.sleep(1)
print()

line2 = """Quest for the Crystal Kingdom

In the magical realm of Eldoria, Iso and Jett, two valiant adventurers, received a summons from the wise wizard Merlin. The Crystal Kingdom, a realm of untold power, was in peril. Trolls, bats, and goblins threatened its existence.

Chapter 1: The Call to Adventure

Armed with a sword and a laser gun, Iso and Jett ventured into the Enchanted Forest. A foreboding cave loomed ahead, harboring a fearsome troll.

What will you do?

Attack the troll with the sword.
Use the laser gun to shoot the troll.
Choose wisely.\n"""
for char in line2:
    print(char, end='')
    time.sleep(.02)

time.sleep(1)
print()

line3 = """Chapter 2: The Enchanted Forest

Outcome 1: Iso's sword clashed with the troll's club, a battle of strength and skill. After a fierce struggle, Iso emerged victorious, gaining valuable experience.

Outcome 2: Jett skillfully aimed the laser gun, firing bursts of energy at the troll. Overwhelmed, the troll retreated into the shadows.

Continuing their journey, a swarm of bats blocked the path.

What will you do?

Confront the bats with the sword.
Use the laser gun to clear a path through the bats.
Choose your action.\n"""
for char in line3:
    print(char, end='')
    time.sleep(.02)

time.sleep(1)
print()

line4 = """Chapter 3: The Bat Swarm

Outcome 1: Iso swung the sword in swift arcs, dispersing the bats. The path ahead was clear, but the sound attracted the attention of a nearby goblin.

Outcome 2: Jett's laser gun emitted a dazzling light show, dispersing the bats. The path ahead was clear, but the noise alerted a nearby goblin.

Confronted by the goblin, a decision had to be made.

What will you do?

Sneak past the goblin.
Confront the goblin with the sword.
Choose your action.\n"""
for char in line4:
    print(char, end='')
    time.sleep(.02)

# Continue adding more lines in a similar manner for the remaining parts of your story
