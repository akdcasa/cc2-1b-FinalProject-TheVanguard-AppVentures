import time


def startGame():
    print("\033[92m")
    print("              ︵‿︵‿୨♡୧‿︵‿︵            ")                      
    print("        ╔════════ ≪ ✧✬✧ ≫ ═════════╗")
    print("        |𝐖 𝐄𝐋𝐂𝐎𝐌𝐄    𝐓𝐎  𝐀𝐏𝐏𝐕𝐄𝐍𝐓𝐔𝐑𝐄|")
    print("       ╔╚════════ ≪ ✧✬✧ ≫ ═════════╝╗")
    print("╔════════════════════•●•═══════════════════╗")
    print("|              --->| ▄█ |<---              |")
    print("|              --->| ░█ |<---              |")
    print("| █▀ ▀█▀ ▄▀█ █▀█ ▀█▀    █▀▀ ▄▀█ █▀▄▀█ █▀▀  |")
    print("| ▄█ ░█░ █▀█ █▀▄ ░█░    █▄█ █▀█ █░▀░█ ██▄  |")
    print("|────────────────── ⋆⋅☆⋅⋆ ─────────────────|")
    print("|              --->| ▀█ |<---              |")
    print("|              --->| █▄ |<---              |")
    print("|        █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀          |")
    print("|        █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█          |")
    print("|────────────────── ⋆⋅☆⋅⋆ ─────────────────|")
    print("|             --->| ▀██ |<---              |")
    print("|             --->| ▄▄█ |<---              |")
    print("|              █▀█ █░█ █ ▀█▀               |")
    print("|              ▀▀█ █▄█ █ ░█░               |")
    print("╚════════════════════•●•═══════════════════╝")
    print()

    user_input = input("Enter an option: ")

    if user_input == '1':
     import Introduction
    elif user_input == '2':
        credits()
    elif user_input == '3':
        global isPlaying
        print("""
▀▀█▀▀▒█░▒█░█▀▀█▒█▄░▒█▒█░▄▀ ▒█░░▒█▒█▀▀▀█▒█░▒█ 　 ▒█▀▀▀▒█▀▀▀█▒█▀▀█ 　 ▒█▀▀█▒█░░░░█▀▀█▒█░░▒█▀█▀▒█▄░▒█▒█▀▀█ 　 ▀▀█▀▀▒█░▒█▒█▀▀▀ ░█▀▀█▒█▀▀█▒█▀▀█ 　 ▒█░░▒█▒█▀▀▀▒█▄░▒█▀▀█▀▀▒█░▒█▒█▀▀█▒█▀▀▀ █ 
░▒█░░▒█▀▀█▒█▄▄█▒█▒█▒█▒█▀▄░ ▒█▄▄▄█▒█░░▒█▒█░▒█ 　 ▒█▀▀▀▒█░░▒█▒█▄▄▀ 　 ▒█▄▄█▒█░░░▒█▄▄█▒█▄▄▄█▒█░▒█▒█▒█▒█░▄▄ 　 ░▒█░░▒█▀▀█▒█▀▀▀ ▒█▄▄█▒█▄▄█▒█▄▄█ 　 ░▒█▒█░▒█▀▀▀▒█▒█▒█░▒█░░▒█░▒█▒█▄▄▀▒█▀▀▀ ▀ 
░▒█░░▒█░▒█▒█░▒█▒█░░▀█▒█░▒█ ░░▒█░░▒█▄▄▄█░▀▄▄▀ 　 ▒█░░░▒█▄▄▄█ █░▒█ 　 ▒█░░░▒█▄▄█▒█░▒█░░▒█░░▄█▄▒█░░▀█▒█▄▄█ 　 ░▒█░░▒█░▒█▒█▄▄▄ ▒█░▒█▒█░░░▒█░░░ 　 ░░▀▄▀░▒█▄▄▄▒█░░▀█░▒█░░░▀▄▄▀▒█░▒█▒█▄▄▄ ▄

""")
        print("")
        isPlaying = False
    else:
        print("\nOption Invalid!")

def credits():
    print("\n════════════════════════════ ⋆★⋆ ════════════════════════════\n")
    time.sleep(1)
    print(""
          )
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

    print("░█████╗░░█████╗░░██████╗░█████╗░  ░█████╗░██╗░░░░░██████╗░░██╗░░░░░░░██╗██╗███╗░░██╗")
    print("██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗░██║░░██╗░░██║██║████╗░██║")
    print("██║░░╚═╝███████║╚█████╗░███████║  ███████║██║░░░░░██║░░██║░╚██╗████╗██╔╝██║██╔██╗██║")
    print("██║░░██╗██╔══██║░╚═══██╗██╔══██║  ██╔══██║██║░░░░░██║░░██║░░████╔═████║░██║██║╚████║")
    print("╚█████╔╝██║░░██║██████╔╝██║░░██║  ██║░░██║███████╗██████╔╝░░╚██╔╝░╚██╔╝░██║██║░╚███║")
    print("░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝ , ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝")
    time.sleep(1)
    print("░█████╗░░█████╗░░██████╗░██████╗░░█████╗░██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██╗░░░░░")
    print("██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██║░░░░░")
    print("██║░░╚═╝███████║██║░░██╗░██████╦╝███████║░╚████╔╝░  ██████╔╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░░░░")
    print("██║░░██╗██╔══██║██║░░╚██╗██╔══██╗██╔══██║░░╚██╔╝░░  ██╔══██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░░░░")
    print("╚█████╔╝██║░░██║╚██████╔╝██████╦╝██║░░██║░░░██║░░░  ██║░░██║╚█████╔╝██║░╚███║██║░╚███║███████╗███████╗")
    print("░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░ , ╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚══════╝")
    time.sleep(1)
    print("░██████╗░█████╗░░██████╗░░█████╗░██╗░░░██╗░█████╗░  ░░░░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██████╗░")
    print("██╔════╝██╔══██╗██╔════╝░██╔══██╗╚██╗░██╔╝██╔══██╗  ░░░░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗")
    print("╚█████╗░███████║██║░░██╗░███████║░╚████╔╝░██║░░██║  ░░░░░██║███████║██╔██╗██║██║░░╚═╝█████╗░░██████╔╝")
    print("░╚═══██╗██╔══██║██║░░╚██╗██╔══██║░░╚██╔╝░░██║░░██║  ██╗░░██║██╔══██║██║╚████║██║░░██╗██╔══╝░░██╔══██╗")
    print("██████╔╝██║░░██║╚██████╔╝██║░░██║░░░██║░░░╚█████╔╝  ╚█████╔╝██║░░██║██║░╚███║╚█████╔╝███████╗██║░░██║")
    print("╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░ , ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░╚═╝")
    time.sleep(1)
    print("░█████╗░████████╗░██████╗░░█████╗░██╗░░░░░░█████╗░███╗░░██╗  ░░░░░██╗░█████╗░██╗░░██╗███╗░░██╗")
    print("██╔══██╗╚══██╔══╝██╔════╝░██╔══██╗██║░░░░░██╔══██╗████╗░██║  ░░░░░██║██╔══██╗██║░░██║████╗░██║")
    print("██║░░██║░░░██║░░░██║░░██╗░███████║██║░░░░░██║░░██║██╔██╗██║  ░░░░░██║██║░░██║███████║██╔██╗██║")
    print("██║░░██║░░░██║░░░██║░░╚██╗██╔══██║██║░░░░░██║░░██║██║╚████║  ██╗░░██║██║░░██║██╔══██║██║╚████║")
    print("╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗╚█████╔╝██║░╚███║  ╚█████╔╝╚█████╔╝██║░░██║██║░╚███║")
    print("╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝░  ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝")
    print("=====================================================================")

# Initialize isPlaying
isPlaying = True

# Start the game loop
while isPlaying:
    startGame()
