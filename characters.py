from inventory import Item

class Character: 
    def __init__(self):
        self.name = ""
        self.health = 10
        self.mana = 10  
        self.strength = 10
        self.agility = 10
        self.intelligence = 10 
        self.dexterity = 10
        self.endurance = 10
        self.level = 1
        self.gold = 0
        self.inventory = [Item("Sword", "weapon", 1), Item("Potion", "consumable", 3)]
    
    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Mana: {self.mana}, Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}, Dexterity: {self.dexterity}, Endurance: {self.endurance}, Level: {self.level}, Gold: {self.gold}, Inventory: {[str(item) for item in self.inventory]}"
    
    def request_name(self):
        self.name = input("Insert your name: ") 

if __name__ == "__main__":
    character = Character()
    print(character)

