# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("What's your name, brave adventurer? ")
    print(f"\nGreetings, {player_name}! You find yourself in a mysterious dungeon with two doors in front of you.")
    choose_door(player_name)

def choose_door(player_name):
    print("\nDo you choose the left door or the right door?")
    choice = input("Type 'left' or 'right': ").lower()

    if choice == 'left':
        empty_room(player_name)
    elif choice == 'right':
        dragon_room(player_name)
    else:
        print("\nInvalid choice. Please try again.")
        choose_door(player_name)

def empty_room(player_name):
    print("\nYou enter the left door and find yourself in an empty room.")
    print("You see nothing of interest here, but the room feels eerie.")

    action = input("Do you want to 'look around' or 'go back'? ").lower()

    if action == 'look around':
        find_sword(player_name)
    elif action == 'go back':
        choose_door(player_name)
    else:
        print("\nInvalid choice. Please try again.")
        empty_room(player_name)

def find_sword(player_name):
    print("\nYou look around the room and find a hidden sword!")
    take_sword = input("Do you want to 'take' the sword or 'leave' it? ").lower()

    if take_sword == 'take':
        print("\nYou have taken the sword. It feels powerful in your hands.")
        dragon_room(player_name, has_sword=True)
    elif take_sword == 'leave':
        print("\nYou decide to leave the sword and return to the previous room.")
        choose_door(player_name)
    else:
        print("\nInvalid choice. Please try again.")
        find_sword(player_name)

def dragon_room(player_name, has_sword=False):
    print("\nYou enter the right door and encounter a fierce dragon!")
    fight = input("Do you want to 'fight' the dragon or 'run away'? ").lower()

    if fight == 'fight':
        if has_sword:
            print("\nYou bravely fight the dragon with your sword and emerge victorious!")
            print(f"Congratulations, {player_name}, you have won the game!")
        else:
            print("\nYou attempt to fight the dragon, but without a weapon, you are no match for it.")
            print("The dragon devours you. You have lost the game.")
    elif fight == 'run away':
        print("\nYou run back to the previous room, safe for now.")
        choose_door(player_name)
    else:
        print("\nInvalid choice. Please try again.")
        dragon_room(player_name, has_sword)

if __name__ == "__main__":
    start_game()