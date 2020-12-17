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
from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
#from rabbit_project.Enclosure import *
import random



class RabbitBreeding():

    def __init__(self, rabbit_list):
        #super().__init__()
        self.rabbit_list = rabbit_list
        self.new_rabbit_list = []
        self.new_population()


    def new_population(self):
        self.can_breed = self.breed_check()
        print(self.can_breed)
        for rabbit in self.rabbit_list:
            if rabbit.sex == "M":
                self.new_rabbit_list.append(rabbit)
            else:
                self.age_check(rabbit)

    def breed_check(self):
        for rabbit in self.rabbit_list:
            if rabbit.sex == "M" and rabbit.available is True and rabbit.mature is True:
                rabbit.available = False
                return True
            else:
                rabbit.available = True
        return False


    def age_check(self, rabbit):
        if self.can_breed:
            if rabbit.sex == "F" and rabbit.mature is True:
                if not rabbit.pregnant:

                    rabbit.pregnant = bool(random.getrandbits(1))
                    self.new_rabbit_list.append(rabbit)
                else:
                    self.give_birth()
                    rabbit.pregnant = False
                    self.new_rabbit_list.append(rabbit)
            else:
                self.new_rabbit_list.append(rabbit)
        else:
            if rabbit.pregnant is True:
                self.give_birth()
                rabbit.pregnant = False
                self.new_rabbit_list.append(rabbit)
            else:
                self.new_rabbit_list.append(rabbit)

    def give_birth(self):
        for i in range(random.randint(1, 2)):
            sex = random.randint(0, 1)
            if sex == 1:
                rabbit = MaleRabbit()
            else:
                rabbit = FemaleRabbit()

            self.new_rabbit_list.append(rabbit)





