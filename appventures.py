def main():
    # Display the main menu
    print("Welcome to the RPG Game!")
    print("----------------------")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit Game")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Handle the user's choice
    if choice == 1:
        start_new_game()
    elif choice == 2:
        load_game()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def start_new_game():
    # Create a new player character
    player = create_player()

    # Start the game loop
    while True:
        # Display the game menu
        print("Game Menu")
        print("----------------------")
        print("1. Travel")
        print("2. Battle")
        print("3. Inventory")
        print("4. Save Game")
        print("5. Exit Game")

        # Get the user's choice
        choice = int(input("Enter your choice: "))

        # Handle the user's choice
        if choice == 1:
            travel(player)
        elif choice == 2:
            battle(player)
        elif choice == 3:
            inventory(player)
        elif choice == 4:
            save_game(player)
        elif choice == 5:
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def create_player():
    # Get the player's name
    name = input("What is your name? ")

    # Create a new player object
    player = Player(name)

    return player

def travel(player):
    # Display the travel options
    print("Travel Options")
    print("----------------------")
    print("1. Forest")
    print("2. Mountains")
    print("3. Caves")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Handle the user's choice
    if choice == 1:
        travel_forest(player)
    elif choice == 2:
        travel_mountains(player)
    elif choice == 3:
        travel_caves(player)
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def battle(player):
    # Generate a random enemy
    enemy = generate_enemy()

    # Start the battle
    while player.health > 0 and enemy.health > 0:
        # Display the battle menu
        print("Battle Menu")
        print("----------------------")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Item")
        print("4. Run Away")

        # Get the user's choice
        choice = int(input("Enter your choice: "))

        # Handle the user's choice
        if choice == 1:
            player_attack(player, enemy)
        elif choice == 2:
            player_defend(player)
        elif choice == 3:
            use_item(player)
        elif choice == 4:
            run_away(player)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        # Check if the enemy is defeated
        if enemy.health <= 0:
            print("You defeated the enemy!")
            player.experience += enemy.experience
            break

        # The enemy's turn
        enemy_attack(enemy, player)

        # Check if the player is defeated
        if player.health <= 0:
            print("You have been defeated!")
            break

    # Check if the player won or lost
    if player.health > 0:
        print("You won the battle!")
    else:
        print("You lost the battle!")

def inventory(player):
    # Display the player's inventory
    print("Inventory")
    print("----------------------")

    for item in player.inventory:
        print(item.name)

def save_game(player):
    # Save the player's data to a file
    with open("player.data", "wb") as f:
        pickle
