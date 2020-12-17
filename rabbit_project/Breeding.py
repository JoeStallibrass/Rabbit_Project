

from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
import random
import json

f = open('rabbit_project/rabbit_default.json')
rabbit_config = json.load(f)


class RabbitBreeding():

    def __init__(self, rabbit_list):
        self.rabbit_list = rabbit_list
        self.new_rabbit_list = []
        self.max_num_babies = rabbit_config['max_num_babies']
        self.ratio_male_female = rabbit_config['ratio_male_to_female']
        self.female_fertility = rabbit_config['female_fertility']



        self.new_population()

    def new_population(self):
        self.can_breed = self.breed_check()
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
                    fertility = random.random()
                    if fertility < self.female_fertility:
                        rabbit.pregnant = True
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
        for i in range(random.randint(0, self.max_num_babies)):
            sex = random.random()
            if sex < self.ratio_male_female:
                rabbit = MaleRabbit()
            else:
                rabbit = FemaleRabbit()

            self.new_rabbit_list.append(rabbit)