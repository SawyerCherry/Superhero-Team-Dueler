from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

def __init__(self, team_one, team_two):
    self.team_one = team_one
    self.team_two = team_two

def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = input(
            "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

def create_weapon(self):
    weapon_name = input("What is the weapon name?  ")
    maximum_damage  = input("What is the maximum damage of the weapon?  ")

    return weapon_name, maximum_damage

def create_armor(self):
    armor_name = input("What is the armor name?  ")
    maximum_block  = input("What is the maximum block of the armor?  ")

    return armor_name, maximum_block

def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               add_ability = self.create_ability
               hero.add_ability(add_ability)
           elif add_item == "2":
               add_a_weapon = self.create_weapon
               hero.add_weapon(add_a_weapon)
           elif add_item == "3":
               add_armor = self.create_armor
               hero.add_armor(add_armor)
        return hero




