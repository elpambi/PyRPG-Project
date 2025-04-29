from characters import Character
from enemys import Enemy
from inventory import show_inventory
from combat import start_combat

def main_menu():
    print("1. Play")
    print("2. Exit")
    option = input("Select an option: ")
    return option

def start_game():
    character = Character()
    goblin = Enemy("Goblin", 20, 5)

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. View Inventory")
        print("3. Attack an enemy")
        print("4. Exit the game")
        
        option = input("Select an option: ")

        if option == "1":
            print(f"{character.name} explores the world.")
        elif option == "2":
            show_inventory(character)
        elif option == "3":
            start_combat(character, goblin)
        elif option == "4":
            print("Exiting the game...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    while True:
        option = main_menu()

        if option == "1":
            print("Starting the game...")
            start_game()
        elif option == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
