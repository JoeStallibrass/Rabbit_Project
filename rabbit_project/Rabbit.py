# base rabbit class for both male and female rabbits
# rabbits need to age, reach maturity and die (or at least change thier bools)

class Rabbit:

    def __init__(self):
        self.age = 0
        self.dead = False
        self.mature = False

    # method to age rabbit by one month, check for death and maturity
    def aging(self):
        if not self.dead:
            self.age += 1
            self.death()
            self.maturity()

    # set death to True when rabbit is 60 months old
    def death(self):
        if self.age >= 60:
            self.dead = True

    # set maturity to True when rabbit is 3 months old
    def maturity(self):
        if self.age >= 3:
            self.mature = True





