from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        weapon_name = input("What is the weapon name?  ")
        maximum_damage  = int(input("What is the maximum damage of the weapon?  "))

        return Weapon(weapon_name, maximum_damage)

    def create_armor(self):
        armor_name = input("What is the armor name?  ")
        maximum_block  = int(input("What is the maximum block of the armor?  "))

        return Armor(armor_name, maximum_block)

    def create_hero(self):
      
            hero_name = input("Hero's name: ")
            hero = Hero(hero_name)
            add_item = None
            while add_item != "4":
                add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
                if add_item == "1":
                    add_ability = self.create_ability()
                    hero.add_ability(add_ability)
                elif add_item == "2":
                    add_a_weapon = self.create_weapon()
                    hero.add_weapon(add_a_weapon)
                elif add_item == "3":
                    add_armor = self.create_armor()
                    hero.add_armor(add_armor)
            return hero

      # build_team_one is provided to you
    def build_team_one(self):
       
        # This method should allow a user to create team one.
       
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    
    def build_team_two(self):
        #we gonna make team two, we will prompt the user 
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def team_one_statistics(self):
        team_kills = 0
        team_deaths = 0
        #this will loop through each hero's kills and deaths and increment them by using +=
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + "The K/D ratio was: " +
              str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
    #the next one shows stats for team 1 so it is the same thing, just have to change out some variable names!

    def team_two_statistics(self):
        team_kills = 0
        team_deaths = 0
        #this will loop through each hero's kills and deaths and increment them by using +=
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + "The K/D ratio was: " +
              str(team_kills/team_deaths))

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

    #gotta have a function to show the stats!

    def show_stats(self):
        print("**-----------------------**")
        print("Now Showing Team One Statitistics!")
        self.team_one_statistics()
        print("**-----------------------**")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("**-----------------------**")
        print("Now Showing Team Two Statitistics!")
        self.team_two_statistics()
        print("**-----------------------**")


    
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena(Team("X Men"), Team("Teen Titans"))

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
