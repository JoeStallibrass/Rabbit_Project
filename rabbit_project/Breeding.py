# this class will receive a list of mature rabbits
# it will go through all non pregnant females and match them up with a male (only one male so not too bad atm)
# it will also go through pregnant females and generate their offspring
# OFFSPRING: As a user I want a litter of offspring between 1 and 14 and to have a random chance to be either male or female.
# SEX: As a user I want to the program to be able to pair an available male and female who are mature to mate at the earliest opportunity.

"""
rabbits have
self.age int
self.mature bool
self.sex      (either 'M' or 'F)
self.pregnant   bool
and self.dead bool
the ones u care about will be mature sex and pregnant
"""
from Female_Rabbit import *
from Male_Rabbit import *
from Enclosure import *
from Rabbit import *
import random



class RabbitBreeding(Enclosure):

    def __init__(self):
        super().__init__()
        rabbit_list = self.enclosure.rabbit_list
        new_rabbit_list = []

    def breed_check(self):
        if self.male.mature not in rabbit_list:
            return True
        else:
            return False

    def age_check(self, rabbit):
        self.breed_check()
        if self.breed_check():
            if self.female.mature:
                if self.female.pregnant is False:

                    self.female.pregnant = bool(random.getrandbits(1))
                    self.new_rabbit_list.append(rabbit)
                else:
                    self.give_birth()
                    self.female.pregnant = False
                    self.new_rabbit_list.append(rabbit)

    def give_birth(self):
        for i in range(random.randint(1, 15)):
            self.new_rabbit_list.append(new_born_rabbit)

    def new_population(self):
        if self.breed_check is True:
            for rabbit in self.rabbit_list:
                if self.male:
                    self.new_rabbit_list.append(rabbit)
                else:
                    self.age_check(rabbit)

        else:

        return self.new_rabbit_list



