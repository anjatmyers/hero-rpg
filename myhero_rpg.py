#### Hero rpg game

class Character: 
    def __init__(self, health, power, name, bounty):
        self.health = health
        self.power = power
        self.name = name
        self.bounty = bounty

    def alive(self):
        return self.health > 0
    
                
    def print_status(self):
        print(f'{self.name} has {self.health} health and {self.power} power.')

    def attack(self, enemy):
        if not self.alive():
            return
        print(f"{self.name} attacks!")
        enemy.receive_damage(self.power)
    
    # def bounty(self, )
class Tonic(object):
    def __init__(self, cost, name):
        self.cost = 5 
        self.name = 'tonic'

    def apply(self, hero):
        hero.health += 2
        print(f"{hero.name} increased to {hero.health}")

class Sword(object):
    def __init__(self, cost, name):
        self.cost = 10
        self.name = 'sword'

class Shield(object):
    def __init__(self, cost, name):
        self.cost = 6
        self.name = 'shield'

class Evade(object):
    def __init__(self, cost, name):
        self.cost = 3
        self.name = 'evade'

    # def apply(self, hero):
    #     hero.power += 2
    #     print(f"{hero.name} power increased to {hero.power}")
items = [Tonic, Sword]

tonic = Tonic(5, 'tonic')
sword = Sword(10, 'sword')
shield = Shield(6, 'shield')
evade = Evade(3, 'evade')
    
class Hero(Character):
    def __init__(self, health, power, name, bounty, evade):
        self.name = name
        self.health = health
        self.power = power
        self.coins = bounty
        self.evade = evade
    
    def receive_damage(self, power):
        self.health -= power

        print(f"{self.name} received {power} damage.")

        if self.health <= 0:
            print(f"{self.name} is dead.")
            print("That was a valiant effort. I'm sorry it came to this.")
            print("""
                       RIP
                Sir John 1985 - 2020
            His flame burned out too soon.
     )
    ()
   |--|
   |  |
 .-|  |-.
:  |  |  :
:  '--'  :
 '-....-' """)

    def shop(self):
        while True:

            print(">>>>>>>>>>>>>>>>>>>>>")
            print("You are now in the armory.")
            print(f"You have {hero.coins} coins.")
            print("What do you want to do?")
            print("1. Buy a health tonic")
            print("2. Buy a sword")
            print("3. Buy a shield")
            print("4. Buy an evade maneuver")
            print("5. Return to battle.")

            store_input = int(input("> "))

            if store_input == 5:
                break
                
            elif store_input == 1:
                self.coins -= tonic.cost
                print("""
<____________>
|            |
|            |
|            |
 \          /
  \________/
      ||
      ||
      ||
      ||
   ___||___
  /\/\/\/\/\ """)
                print(f"The health tonic is yours. You now have {self.coins} coins.")
                hero.apply1(tonic)

            elif store_input == 2:
                self.coins -= sword.cost
                print("""
                           O
              {____________________________________
@XXXXXXXXXXXXXX___________________________________.>
              {
              O
              """)
                print(f"The sword is yours. You now have {self.coins} coins.")
                hero.apply2(sword)
            elif store_input == 3:
                self.coins -= shield.cost
                print("""

  |`-._/\_.-`|
  |    ||    |
  |___o()o___|
  |__((<>))__|
  \   o\/o   /
   \   ||   /
    \  ||  /
     '.||.'
       ``
                """)
                print(f"The shield is yours. You now have {self.coins} coins.")
                hero.apply3(shield)
            elif store_input == 4:
                self.coins -= evade.cost
                print(f"The maneuver is yours. You now have {self.coins} coins.")
                hero.apply4(evade)

    def apply1(self, item):
        self.health += 2
        print(f"{self.name}'s health increased to {self.health}.")
    
    def apply2(self, item):
        self.power += 2
        print(f"{self.name}'s power increased to {self.health}.")

    def apply3(self, item):
        self.health += 5
        print(f"{self.name}'s health increased to {self.health}.")

    def apply4(self, item):
        self.evade += 2
        print(f"{self.name} now has {self.evade} evade points.")

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
            print("""                 .-.
                          {{#}}
          {}               8@8
        .::::.             888
    @\\/W\/\/W\//@         8@8
     \\/^\/\/^\//     _    )8(    _
      \_O_{}_O_/     (@)__/8@8\__(@)
 ____________________ `~"-=):(=-"~`
|<><><>  |  |  <><><>|     |.|
|<>      |  |      <>|     |S|
|<>      |  |      <>|     |'|
|<>   .--------.   <>|     |.|
|     |   ()   |     |     |P|
|_____| (O\/O) |_____|     |'|
|     \   /\   /     |     |.|
|------\  \/  /------|     |U|
|       '.__.'       |     |'|
|        |  |        |     |.|
:        |  |        :     |N|
 \       |  |       /      |'|
  \<>    |  |    <>/       |.|
   \<>   |  |   <>/        |K|
    `\<> |  | <>/'         |'|
      `-.|__|.-`           \ /
                            ^""")
            

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
            print("""                 .-.
                          {{#}}
          {}               8@8
        .::::.             888
    @\\/W\/\/W\//@         8@8
     \\/^\/\/^\//     _    )8(    _
      \_O_{}_O_/     (@)__/8@8\__(@)
 ____________________ `~"-=):(=-"~`
|<><><>  |  |  <><><>|     |.|
|<>      |  |      <>|     |S|
|<>      |  |      <>|     |'|
|<>   .--------.   <>|     |.|
|     |   ()   |     |     |P|
|_____| (O\/O) |_____|     |'|
|     \   /\   /     |     |.|
|------\  \/  /------|     |U|
|       '.__.'       |     |'|
|        |  |        |     |.|
:        |  |        :     |N|
 \       |  |       /      |'|
  \<>    |  |    <>/       |.|
   \<>   |  |   <>/        |K|
    `\<> |  | <>/'         |'|
      `-.|__|.-`           \ /
                            ^""")

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
            print("""                 .-.
                          {{#}}
          {}               8@8
        .::::.             888
    @\\/W\/\/W\//@         8@8
     \\/^\/\/^\//     _    )8(    _
      \_O_{}_O_/     (@)__/8@8\__(@)
 ____________________ `~"-=):(=-"~`
|<><><>  |  |  <><><>|     |.|
|<>      |  |      <>|     |S|
|<>      |  |      <>|     |'|
|<>   .--------.   <>|     |.|
|     |   ()   |     |     |P|
|_____| (O\/O) |_____|     |'|
|     \   /\   /     |     |.|
|------\  \/  /------|     |U|
|       '.__.'       |     |'|
|        |  |        |     |.|
:        |  |        :     |N|
 \       |  |       /      |'|
  \<>    |  |    <>/       |.|
   \<>   |  |   <>/        |K|
    `\<> |  | <>/'         |'|
      `-.|__|.-`           \ /
                            ^""")

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

hero = Hero(10, 4, 'Sir John', 10, 0)
dragon = Enemy(8, 2, 'Dragon King', 5)
medic = Medic(8, 1, 'Medic', 7)
zombie = Zombie(8, 1, 'Zombie', 1000)
shadow = Shadow(5, 1, 'Shadow', 50)


def intro_question():
    print("")
    print("What do you want to do?")
    print("1. fight dragon")
    print("2. do nothing")
    print("3. Shop for a weapon")
    print("4. flee")
    print("> ", end=' ')

def battle():
    print(f"Welcome to the Woodcroft Castle.\nOur hero, Sir John, is trying to protect his home.\nHe has to defeat his archnemesis, {dragon.name} in order to keep the castle safe.\nWe need your help.")
    print("""   |>>>                                                      |>>>
    |                     |>>>          |>>>                  |
    *                     |             |                     *
   / \                    *             *                    / \
  /___\                 _/ \           / \_                 /___\
  [   ]                |/   \_________/   \|                [   ]
  [ I ]                /     \       /     \                [ I ]
  [   ]_ _ _          /       \     /       \          _ _ _[   ]
  [   ] U U |        {#########}   {#########}        | U U [   ]
  [   ]====/          \=======/     \=======/          \====[   ]
  [   ]    |           |   I |_ _ _ _| I   |           |    [   ]
  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]
  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/
   \=/     |===========| I   | + W + |   I |===========|     \=/
    |  I   |           |     |_______|     |           |   I  |
    |      |           |     |||||||||     |           |      |
    |      |           |   I ||vvvvv|| I   |           |      |
_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_
   /________\         /______||     ||______\         /________\
  |__________|-------|________\_____/________|-------|__________|""")
    while dragon.alive() and hero.alive():
            print("......................")
            hero.print_status()
            dragon.print_status()

            intro_question()
            raw_input = input()
            if raw_input == "1":
                hero.attack(dragon)
            elif raw_input == "2":
                print("Okay, but inaction is a costly choice...")
            elif raw_input == "3":
                hero.shop()
            elif raw_input == "4":
                print("We shall try and carry on without you. Good luck on your journey.\n If I were you, I would not return.")
                print("""|>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       \,/
                                             ||: , |            /`\
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~""")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if dragon.alive():
                dragon.attack(hero)


battle()






