import time
import random
from rabbit_project.Male_Rabbit import MaleRabbit
from rabbit_project.Female_Rabbit import FemaleRabbit
from rabbit_project.Breeding import RabbitBreeding
from rabbit_project.Male_Fox import MaleFox
from rabbit_project.Female_Fox import FemaleFox
from rabbit_project.Fox_Breeding import FoxBreeding
import json

f = open('rabbit_project/rabbit_default.json')
rabbit_config = json.load(f)
g = open('rabbit_project/fox_default.json')
fox_config = json.load(g)

class Enclosure():

    def __init__(self):
        # First we initialise year input by asking user the simulation duration
        # This is where the user fulfills the 'population limit'
        self.year_input = rabbit_config['sim_duration_years']
        # The program runs on a monthly basis, so years converted to months and proceeds
        self.month_input = self.year_input * 12
        self.sim_rate = rabbit_config['sim_rate']
        # Initialise the rabbit list by inheriting it from the other group
        # self.rabbit_list = Breeding.self.function.self.rabbit_list
        self.dead_rabbits = 0
        self.alive_per_month_male_rabbit = 0
        self.alive_per_month_female_rabbit = 0
        self.rabbit_list = []
        self.num_starting_rabbits = rabbit_config['num_starting_rabbits']
        self.eaten_rabbits = 0

        # Foxes Info
        self.dead_foxes = 0
        self.alive_per_month_male_fox = 0
        self.alive_per_month_female_fox = 0
        self.fox_list = []
        self.num_starting_foxes = fox_config['num_starting_foxes']
        self.num_rabbits_eaten = fox_config['num_rabbits_eaten']
        self.integrating_month = fox_config['integrating_month']

    def starting_rabbits(self):
        # This method is called at the very start of the simulation to create a starting pair
        for rabbit in range(self.num_starting_rabbits):
            if rabbit % 2 == 0:
                self.rabbit_list.append(MaleRabbit())
            else:
                self.rabbit_list.append(FemaleRabbit())

    def starting_foxes(self):
        # This method is called at the very start of the simulation to create a starting pair
        for fox in range(self.num_starting_foxes):
            if fox % 2 == 0:
                self.fox_list.append(MaleFox())
            else:
                self.fox_list.append(FemaleFox())

    # --------------------------------------------------------------------------
    def rabbit_gender_status(self):
        # This method counts how many males and females are alive each month, resetting on each iteration
        self.alive_per_month_male_rabbit = 0
        self.alive_per_month_female_rabbit = 0
        for rabbit in self.rabbit_list:
            if rabbit.sex == "M":
                self.alive_per_month_male_rabbit += 1
            elif rabbit.sex == "F":
                self.alive_per_month_female_rabbit += 1
        print(f"Male rabbits alive is {'{:,}'.format(self.alive_per_month_male_rabbit)}")
        print(f"Female rabbits alive is {'{:,}'.format(self.alive_per_month_female_rabbit)}")
        print('\n')

    def fox_gender_status(self):
        # This method counts how many males and females are alive each month, resetting on each iteration
        self.alive_per_month_male_fox = 0
        self.alive_per_month_female_fox = 0
        for fox in self.fox_list:
            if fox.sex == "M":
                self.alive_per_month_male_fox += 1
            elif fox.sex == "F":
                self.alive_per_month_female_fox += 1
        print(f"Male foxes alive is {'{:,}'.format(self.alive_per_month_male_fox)}")
        print(f"Female foxes alive is {'{:,}'.format(self.alive_per_month_female_fox)}")
        print('\n')

    # -------------------------------------------------------------------------------
    # def rabbit_alive_status(self):
    #     # This method keeps track of the total that are alive and removes
    #     for rabbit in self.rabbit_list:
    #         print(self.rabbit_list)
    #         if rabbit.dead:
    #             print('hello')
    #             self.dead_rabbits += 1
    #             self.rabbit_list.remove(rabbit)

    def _age_rabbits(self):
        for rabbit in self.rabbit_list:
            rabbit.aging()
        alive_rabbits = [x for x in self.rabbit_list if x.dead != True]
        self.dead_rabbits += (len(self.rabbit_list) - len(alive_rabbits))
        self.rabbit_list = alive_rabbits

    def _age_foxes(self):
        for fox in self.fox_list:
            fox.aging()
        alive_foxes = [x for x in self.fox_list if x.dead != True]
        self.dead_foxes += (len(self.fox_list) - len(alive_foxes))
        self.fox_list = alive_foxes

    # ------------------------------------------------------------------------------------

    def _foxes_eat(self):
        for fox in self.fox_list:
            if fox.rabbit_eating_maturity:
                for i in range(self.num_rabbits_eaten):
                    if len(self.rabbit_list) >= 1:
                        self.rabbit_list.pop(random.randint(0, len(self.rabbit_list)-1))
                        self.dead_rabbits += 1
                        self.eaten_rabbits += 1
                    elif len(self.rabbit_list) == 1:
                        self.rabbit_list.pop()
                        self.dead_rabbits += 1
                        self.eaten_rabbits += 1


    # -------------------------------------------------------------------------------------

    def simulation_start(self):

        # Here the method prints the month for each iteration, at 1 month per second
        self.starting_rabbits()
        ascending_month = 0

        while ascending_month != self.month_input:

            if ascending_month == self.integrating_month:
                self.starting_foxes()


            time.sleep(self.sim_rate)

            ascending_month += 1
            print(f"Month {ascending_month}")

            # For each rabbit, Group 1's class is called to run a few updates:
            # Age is checked, maturity, and whether the rabbit should be dead
            # for rabbit in self.rabbit_list:
            #     # rabbit.aging has built in functions that call upon more methods
            #     rabbit.aging()
            self._age_rabbits()
            self._age_foxes()

            # Calls the method that checks whether they are alive or dead
            # self.rabbit_alive_status()
            new_rabbit_list = RabbitBreeding(self.rabbit_list)
            self.rabbit_list = new_rabbit_list.new_rabbit_list

            new_fox_list = FoxBreeding(self.fox_list)
            self.fox_list = new_fox_list.new_fox_list
            # Calls the method that checks how many are alive for each gender during this month
            self.rabbit_gender_status()
            self.fox_gender_status()

            self._foxes_eat()

        if ascending_month == self.month_input:
            print(f"The total number of alive rabbits is: {'{:,}'.format(len(self.rabbit_list))}")
            print(f"The total number of dead rabbits is: {'{:,}'.format(self.dead_rabbits)}")
            print(f"The total number of eaten rabbits is: {'{:,}'.format(self.eaten_rabbits)}")

            print(f"The total number of alive foxes is: {'{:,}'.format(len(self.fox_list))}")
            print(f"The total number of dead foxes is: {'{:,}'.format(self.dead_foxes)}")
