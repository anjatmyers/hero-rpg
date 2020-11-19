#### Hero rpg game


class Character: 
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            return True
        elif self.name == 'Superman':
            print("You are dead.")
        else:
            print(f"The {self.name} is dead!")
    
    def print_status(self):
        if self.name == 'Superman':
            print(f'You have {self.health} health and {self.power} power.')
        else:
            print(f'{self.name} has {self.health} health and {self.power} power.')

    def attack(self, enemy):
        enemy.health -= self.power
        if self.name == 'Superman':
            print(f"You do {self.power} damage to the {enemy.name}.")
        else:
            print(f"{self.name} does {self.power} damage to you.")

class Immortal_Enemy(Character):
    def alive(self):
        return True



hero = Character(10, 5, 'Superman')
goblin = Character(6, 2, 'Goblin King')
zombie = Immortal_Enemy(4, 1, 'Zombie')

def intro_question():
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')



while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()

        intro_question()
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            goblin.attack(hero)