class Character:
    game_name = "Battle Arena"

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def display_info(self):
        print(f"{self.name} - {self.health} - {self.level}")

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name, health, level, weapon):
        super().__init__(name, health, level)
        self.weapon = weapon

    def attack(self):
        print("A warrior attacks with a sword")
        return 20

class Mage(Character):
    def __init__(self, name, health, level, magic_power):
        super().__init__(name, health, level)
        self.magic_power = magic_power

    def attack(self):
        print("A mage attacks with magic")
        return 30


character1 = Character("Hemzel", 100, 43)
character2 = Character("Joe", 88, 65)
character3 = Character("Nana", 98, 88)

warrior1 = Warrior("Mike", 54, 45, "Excaluber")
warrior2 = Warrior("Fredy", 74, 25, "Rapiar")
mage1 = Mage("Sissy", 41, 86, "Dark Magic")
mage2 = Mage("Ama", 92, 75, "Flame Magic")

print(character1.name)
character2.display_info()
print(character1.game_name)


print(f"Nana's health after damage: {character3.health}")
print(character3.is_alive())

print(warrior1.name)
warrior2.attack()
print(mage1.name)
mage2.attack()

damage = warrior2.attack() 
character3.take_damage(damage)
print(character3.health)

damage = mage2.attack() 
character2.take_damage(damage)
print(character2.health)