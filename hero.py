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
        self.deaths = 0
        self.kills = 0

    

    def add_ability(self, ability):
        self.abilities.append(ability)

    def fight(self, opponent):
        if self.is_alive() is True:
            opponent.take_damage(self.attack())
        else:
            opponent.add_kill(1)
            self.add_death(1)
            print(f"{self.name} is dead :(")
            return self.name
        if opponent.is_alive() is True:
            self.take_damage(opponent.attack())
        else:
            self.add_kill(1)
            opponent.add_death(1)
            print(f"{opponent.name} is dead :(")
            return opponent.name
        self.fight(opponent)


    
    def add_armor(self, armor): 
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print(f"{self.name} has the weapon {weapon.name} and it is added to their abilities")

    def attack(self):
        damage_amt = 0
        for ability in self.abilities:
            damage_amt += ability.attack()
        return damage_amt

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
            print(f"The hero {self.name}, is very much dead :(")
        elif self.current_health > 0: 
            print(f"The hero {self.name}, is alive")

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    


    

    





