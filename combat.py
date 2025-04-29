def attack(character, enemy):
    print(f"{character.name} attacks {enemy.name}")
    damage = character.strength - enemy.resistance
    if damage > 0:
        enemy.health = max(0, enemy.health - damage)
        print(f"{enemy.name} takes {damage} damage")
        print(f"{enemy.name}'s health is now {enemy.health}")
        return damage
    else:
        print(f"{enemy.name} takes no damage")

def flee(character, enemy):
    if character.agility > enemy.agility:
        print(f"{character.name} successfully fled")
        return True
    else:
        print(f"{character.name} failed to flee")
        return False

def start_combat(character, enemy):
    turns = 0
    max_turns = 10
    while turns < max_turns:
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Flee")
        option = input("Select an option: ")

        if option == "1":
            print("Attacking...")
            attack(character, enemy)
            turns += 1
            print(f"Turn {turns} of {max_turns}")
        elif option == "2":
            print("Attempting to flee...")
            if flee(character, enemy):
                break
            turns += 1
            print(f"Turn {turns} of {max_turns}")
        else:
            print("Invalid option. Please try again.")

        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated")
            break
