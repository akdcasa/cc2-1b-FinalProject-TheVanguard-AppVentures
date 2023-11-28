import time


def startGame():
    print("||##########################################||")
    print("||###########|      WELCOME    |############||")
    print("||###########|        TO       |############||")
    print("||###########|    AppVenture   |############||")
    print("||##########################################||")
    print("||              --->| ▄█ |<---              ||")
    print("||              --->| ░█ |<---              ||")
    print("|| █▀ ▀█▀ ▄▀█ █▀█ ▀█▀    █▀▀ ▄▀█ █▀▄▀█ █▀▀  ||")
    print("|| ▄█ ░█░ █▀█ █▀▄ ░█░    █▄█ █▀█ █░▀░█ ██▄  ||")
    print("||##########################################||")
    print("||             --->| ▀█ |<---               ||")
    print("||             --->| █▄ |<---               ||")
    print("||        █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀          ||")
    print("||        █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█          ||")
    print("||##########################################||")
    print("||             --->| ▀██ |<---              ||")
    print("||             --->| ▄▄█ |<---              ||")
    print("||              █▀█ █░█ █ ▀█▀               ||")
    print("||              ▀▀█ █▄█ █ ░█░               ||")
    print("||##########################################||")
    print()

    user_input = input("Enter an option: ")

    if user_input == '1':
       import Introduction
    if user_input == "1":    
        import mAPpygame 
    if user_input == '1':
        import randomenemyencounter

    elif user_input == '2':
        credits()
    elif user_input == '3':
        global isPlaying
        print("\nThank you for playing AppVenture!")
        print("")
        isPlaying = False
    else:
        print("\nOption Invalid!")

def credits():
    print("\n===================================================================\n")
    time.sleep(1)
    print("The Masterminds behind The Vanguard!")
    print()
    time.sleep(1)

    load = "..."
    for char in load:
        print(char, end='')
        time.sleep(.5)

    time.sleep(1)
    print("The Vanguard")
    print()

    time.sleep(1)

    print("Casa, Aldwin Keith")
    time.sleep(1)
    print("Cagbay, Ronnel")
    time.sleep(1)
    print("Sagayo, Jancer")
    time.sleep(1)
    print("Otgalon, John Wyne")
    time.sleep(1)
    print("=====================================================================")

# Initialize isPlaying
isPlaying = True

# Start the game loop
while isPlaying:
    startGame()
