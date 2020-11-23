class Character: 
    def __init__(self, health, power, name, bounty):
        self.health = health
        self.power = power
        self.name = name
        self.bounty = bounty

    def alive(self):
        return self.health > 0
    
                
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

    def attack(self, enemy):
        if not self.alive():
            return
        print(f"{self.name} attacks!")
        enemy.receive_damage(self.power)
    
    # def bounty(self, )
    
    
class Hero(Character):
    def __init__(self, health, power, name, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.coins = bounty
    
    def receive_damage(self, power):
        self.health -= power

        print(f"{self.name} received {power} damage.")

        if self.health <= 0:
            print(f"{self.name} is dead.")
            print("That was a valiant effort. I'm sorry it came to this.")

    def shop(self):
        Store.shopping(self.coins)

    def buy(self, item):
        self.coins -= item.cost
        print(f"You now have {self.coins} coins.")

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
            print(f"Huzzah! {self.name} has been defeated! You are a true Knight.")
            

class Medic(Enemy):
    def receive_damage(self, power):
        import random
        rand_num = random.randint(1, 10)
        rand_num2 = random.randint(1, 10)
        if rand_num > 8: 
            power = (power * 2)
            self.health -= power
            print(f"Critical Hit! Double damage! {self.name} received {power} damage.")
        else:
            self.health -= power
            print(f"{self.name} received {power} damage.")

        if rand_num2 > 8:
            self.health += 2
            print(f"{self.name} recouped 2 health points! Better watch out for him.")
        if self.health <= 0:
            print(f"{self.name} is dead.")
            print(f"Huzzah! {self.name} has been defeated! You are a true Knight.")

class Shadow(Enemy):
    def receive_damage(self, power):
        import random
        rand_num = random.randint(1, 10)
        rand_num2 = random.randint(1, 10)
        if rand_num2 > 9: 
            self.health -= power
            print(f"{self.name} received {power} damage.")
        elif rand_num2 > 9 and rand_num1 < 2:
            self.health -= (power * 2)
            print(f"Critical Hit! Double damage! {self.name} received {power} damage.")
        else:
            print(f"{self.name} avoided your damage. He is very elusive.")

        if self.health <= 0:
            print(f"{self.name} is dead.")
            print(f"Huzzah! {self.name} has been defeated! You are a true Knight.")
class Zombie(Enemy):
    def alive(self):
        return True
    
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
            print(f"{self.name} is still alive. He can't die. You better run!")

hero = Hero(10, 4, 'Sir John', 10)
goblin = Enemy(8, 2, 'Goblin King', 5)
medic = Medic(8, 1, 'Medic', 7)
zombie = Zombie(8, 1, 'Zombie', 1000)
shadow = Shadow(5, 1, 'Shadow', 50)

class Tonic:
    def __init__(self, cost, name):
        self.cost = 5 
        self.name = 'tonic'

    def apply(self, hero):
        hero.health += 2
        print(f"{hero.name} increased to {hero.health}")

class Sword:
    def __init__(self, cost, name):
        self.cost = 10
        self.name = 'sword'

    def apply(self, hero):
        hero.power += 2
        print(f"{hero.name} power increased to {hero.power}")


class Store:
    items = [Tonic, Sword]

    def shopping(self):

        while True:

            print(">>>>>>>>>>>>>>>>>>>>>")
            print("Welcome to the armory.")
            print(f"You have {hero.coins} coins.")
            print("What do you want to do?")

            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i + 1}. buy {item.name} ({item.cost})")
            print("10. Return to battle.")

            store_input = int(input("> "))

            if store_input == 10:
                battle()
            else:

                ItemToBuy = Store.items[store_input -1]

                item = ItemToBuy()

                hero.buy(item)

tonic = Tonic(5, 'tonic')
sword = Sword(10, 'sword')

def intro_question():
    print("")
    print("What do you want to do?")
    print("1. fight zombie")
    print("2. do nothing")
    print("3. Shop for a weapon")
    print("4. flee")
    print("> ", end=' ')

def battle():
    print(f"Welcome to battle.\nOur hero, Sir John, is trying to defeat his archnemesis, {zombie.name}.\nWe need your help.")
    while zombie.alive() and hero.alive():
            print("......................")
            hero.print_status()
            zombie.print_status()

            intro_question()
            raw_input = input()
            if raw_input == "1":
                hero.attack(zombie)
            elif raw_input == "2":
                print("Okay, but inaction is a costly choice...")
            elif raw_input == "3":
                hero.shop()
            elif raw_input == "4":
                print("We shall try and carry on without you. Good luck on your journey.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if zombie.alive():
                zombie.attack(hero)


battle()