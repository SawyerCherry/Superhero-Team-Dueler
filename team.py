import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()


    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True      
        if not foundHero:
            return 0

    def view_all_heroes(self):
    # simple for loop to print out all of them
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
    #used .append method to add to the list
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        #im going to use a for loop to do this, it will loop through each hero and give them each 100 health
        for hero in self.heroes:
            hero.current_health = 100


    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
           
            # 1) Randomly select a living hero from each team 
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            # 2) have the heroes fight each other 
            big_loser = hero.fight(opponent)

            # 3) update the list of living_heroes and living_opponents to reflect the result of fight 
            for hero in living_heroes:
                if big_loser.name == hero.name:
                    living_heroes.remove(hero)
            for opponent in living_opponents:
                if big_loser.name == opponent.name:
                    living_opponents.remove(opponent)

           

    
        

        
        


