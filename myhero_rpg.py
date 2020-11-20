#### Hero rpg game

class Character: 
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        return self.health > 0
    
                
    def print_status(self):
        print(f'{self.name} has {self.health} health and {self.power} power.')

    def attack(self, enemy):
        if not self.alive():
            return
        print(f"{self.name} attacks!")
        enemy.receive_damage(self.power)
    
    
class Hero(Character):
    def receive_damage(self, power):
        self.health -= power

        print(f"{self.name} received {power} damage.")

        if self.health <= 0:
            print(f"{self.name} is dead.")


class Enemy(Character):
    def receive_damage(self, power):
        import random
        rand_num = random.randint(1, 10)
        if rand_num > 8: 
            self.health -= (power * 2)
            print(f"Critical Hit! Double damage!")
        else:
            self.health -= power
            print(f"{self.name} received {power} damage.")

        if self.health <= 0:
            print(f"{self.name} is dead.")
        


class Immortal_Enemy(Enemy):
    def alive(self):
        return True

class Medic(Enemy):
    pass

hero = Hero(10, 4, 'Sir John')
goblin = Enemy(9, 2, 'Goblin King')
medic = Enemy(10, 2, 'Medic')
zombie = Immortal_Enemy(4, 1, 'Zombie')

def intro_question():
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')

def battle():
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

battle()