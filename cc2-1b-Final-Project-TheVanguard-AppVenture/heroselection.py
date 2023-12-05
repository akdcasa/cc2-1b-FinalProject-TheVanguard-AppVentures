import random
class Iso(object):
    def __init__(self):
        self.name = "Iso"
        self.health = 25
        self.strength = 11
        self.defence = 15

class Jett(object):
    def __init__(self):
        self.name = "Jett"
        self.health = 25
        self.strength = 11
        self.defence = 15

def heroselect():
    print("Select your hero!")
    selection = input("1. Iso \n2. Jett\nEnter your Choice: ")

    if selection == "1":
        character = Iso()
        print("You have selected Iso... These are their stats:")
        print("Health -", character.health)
        print("Strength -", character.strength)
        print("Defence -", character.defence)
        return character
        
    elif selection == "2":
        character = Jett()
        print("You have selected Jett... These are their stats:")
        print("Health -", character.health)
        print("Strength -", character.strength)
        print("Defence -", character.defence)
        return character
      
    else:
        print("Only press 1 or 2")
        return heroselect()

# Example usage:
selected_hero = heroselect()
import mapa