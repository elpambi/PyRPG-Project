def show_inventory(character):
    print("Inventory:")
    if len(character.inventory) > 0:
        for item in character.inventory:
            print(item)  # Here I use __str__ to format the item from list 
    else:
        print("The inventory is empty.")

class Item:
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

    def use_consumables(self):
        if self.amount > 0 and self.type == "consumable":
            self.amount -= 1
            print(f"Using {self.name}. Remain {self.amount} in the inventory.")
        else:
            print(f"There are no {self.name} left in the inventory.")

    def equip(self):
        if self.type == "weapon" and self.amount > 0:
            print(f"Equipped {self.name}.")
        else:
            print(f"{self.name} can't be equipped.")
            
    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Amount: {self.amount}"

