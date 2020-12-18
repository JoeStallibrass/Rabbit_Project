

from rabbit_project.Female_Fox import *
from rabbit_project.Male_Fox import *
import random
import json

f = open('rabbit_project/fox_default.json')
fox_config = json.load(f)


class FoxBreeding():

    def __init__(self, fox_list):
        self.fox_list = fox_list
        self.new_fox_list = []
        self.max_num_babies = fox_config['max_num_babies']
        self.ratio_male_female = fox_config['ratio_male_to_female']
        self.female_fertility = fox_config['female_fertility']



        self.new_population()

    def new_population(self):
        self.can_breed = self.breed_check()
        for fox in self.fox_list:
            if fox.sex == "M":
                self.new_fox_list.append(fox)
            else:
                self.age_check(fox)

    def breed_check(self):
        for fox in self.fox_list:
            if fox.sex == "M" and fox.available is True and fox.mature is True:
                fox.available = False
                return True
            else:
                fox.available = True
        return False


    def age_check(self, fox):
        if self.can_breed:
            if fox.sex == "F" and fox.mature is True:
                if not fox.pregnant:
                    fertility = random.random()
                    if fertility < self.female_fertility:
                        fox.pregnant = True
                    self.new_fox_list.append(fox)
                else:
                    self.give_birth()
                    fox.pregnant = False
                    self.new_fox_list.append(fox)
            else:
                self.new_fox_list.append(fox)
        else:
            if fox.pregnant is True:
                self.give_birth()
                fox.pregnant = False
                self.new_fox_list.append(fox)
            else:
                self.new_fox_list.append(fox)

    def give_birth(self):
        for i in range(random.randint(0, self.max_num_babies)):
            sex = random.random()
            if sex < self.ratio_male_female:
                fox = MaleFox()
            else:
                fox = FemaleFox()

            self.new_fox_list.append(fox)