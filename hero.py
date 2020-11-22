from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor): 
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # This method will append the weapon object passed in as an
        # argument to self.abilities.
        self.abilities.append(weapon)
        # This means that self.abilities will be a list of
        # abilities and weapons.
        print(f"{self.name} has the weapon {weapon.name} and it is added to their abilities")



    def defend(self, incoming_damage: int):
        block_amt = 0
        # basically just like the attack method using a for loop. 
        for armor in self.armors:
            block_amt += armor.block()
        return incoming_damage - block_amt

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(f"{self.name} has taken {damage} damage. Their updated health is {self.current_health}")


    def is_alive(self):
        if self.current_health <= 0:
            print(f"The hero {self.name}, is no longer alive.")
        elif self.current_health > 0: 
            print(f"The hero {self.name}, is alive")


    

    
            
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())




