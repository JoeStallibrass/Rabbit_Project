
import json


f = open('rabbit_default.json')
rabbit_config = json.load(f)

class Rabbit:

    def __init__(self):
        self.age = 0
        self.dead = False
        self.mature = False
        self.maturity_age = rabbit_config['maturity_age_months']
        self.life_expectancy = rabbit_config['life_expectancy_months']

    # method to age rabbit by one month, check for death and maturity
    def aging(self):
        self.age += 1
        self.death()
        self.maturity()

    # set death to True when rabbit is 60 months old
    def death(self):
        if self.age >= self.life_expectancy:
            self.dead = True

    # set maturity to True when rabbit is 3 months old
    def maturity(self):
        if self.age >= self.maturity_age:
            self.mature = True


r = Rabbit()
print(r.maturity_age)


