from player import choose_class
from areas_data import areas_list
from utils import slow_print

def main():
    slow_print("Welcome to the Epic Text RPG!\n")
    
    # Get player name
    player_name = input("Enter your character's name: ")
    player = choose_class(player_name)

    slow_print(f"Welcome, {player.name} the {player.class_name}!\n")

    # Main game loop through areas
    for area in areas_list:
        slow_print(f"--- Entering {area.name} ---\n")
        area.explore(player)  # battles and random shop occur inside explore()

        if not player.is_alive():
            slow_print("Game Over. Better luck next time!")
            return

    slow_print("Congratulations! You have defeated all the bosses and completed the game!")
    slow_print("Thanks for playing!\n")

if __name__ == "__main__":
    main()
