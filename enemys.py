class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.resistance = 5  # Default resistance value
        self.agility = 5     # Default agility value

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Strength: {self.strength}, Resistance: {self.resistance}, Agility: {self.agility}"

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} received {damage} damage. Remaining health: {self.health}")

    def attack(self, character):
        damage = self.strength - character.resistance
        if damage > 0:
            print(f"{self.name} attacks {character.name} for {damage} damage.")
            character.health -= damage
            if character.health < 0:
                character.health = 0
            print(f"{character.name} remaining health: {character.health}")
        else:
            print(f"{self.name}'s attack had no effect.")
