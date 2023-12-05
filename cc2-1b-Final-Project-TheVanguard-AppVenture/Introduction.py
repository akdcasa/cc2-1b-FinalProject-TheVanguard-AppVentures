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
\n"""
for char in line2:
    print(char, end='')
    time.sleep(.02)

time.sleep(1)
print()


# Continue adding more lines in a similar manner for the remaining parts of your story
