
import json


#f = open('rabbit_project/rabbit_default.json')
fox_config = json.load(f)

class Fox:

    def __init__(self):
        self.age = 0
        self.dead = False
        self.mature = False
        self.maturity_age = fox_config['maturity_age_months']
        self.life_expectancy = fox_config['life_expectancy_months']

    # method to age fox by one month, check for death and maturity
    def aging(self):
        if not self.dead:
            self.age += 1
            self.death()
            self.maturity()

    # set death to True when fox is x months old
    def death(self):
        if self.age >= self.life_expectancy:
            self.dead = True

    # set maturity to True when fox is x months old
    def maturity(self):
        if self.age >= self.maturity_age:
            self.mature = True


f = Fox()
print(f.maturity_age)