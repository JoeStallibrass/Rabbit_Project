import time
from Male_Rabbit import MaleRabbit
from Female_Rabbit import FemaleRabbit
from Breeding import RabbitBreeding
import json
f = open('rabbit_default.json')
rabbit_config = json.load(f)


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
        self.alive_per_month_male = 0
        self.alive_per_month_female = 0
        self.rabbit_list = []
        self.num_starting_rabbits = rabbit_config['num_starting_rabbits']

    def starting_rabbits(self):
        # This method is called at the very start of the simulation to create a starting pair
        for rabbit in range(self.num_starting_rabbits):
            if rabbit % 2 == 0:
                self.rabbit_list.append(MaleRabbit())
            else:
                self.rabbit_list.append(FemaleRabbit())


    def rabbit_gender_status(self):
        # This method counts how many males and females are alive each month, resetting on each iteration
        self.alive_per_month_male = 0
        self.alive_per_month_female = 0
        for rabbit in self.rabbit_list:
            if rabbit.sex == "M":
                self.alive_per_month_male += 1
            elif rabbit.sex == "F":
                self.alive_per_month_female += 1
        print(f"Male rabbits alive is {self.alive_per_month_male}")
        print(f"Female rabbits alive is {self.alive_per_month_female}")
        print('\n')

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

    def simulation_start(self):

        # Here the method prints the month for each iteration, at 1 month per second
        self.starting_rabbits()
        ascending_month = 0


        while ascending_month != self.month_input:
            time.sleep(self.sim_rate)

            ascending_month += 1
            print(f"Month {ascending_month}")

            # For each rabbit, Group 1's class is called to run a few updates:
            # Age is checked, maturity, and whether the rabbit should be dead
            # for rabbit in self.rabbit_list:
            #     # rabbit.aging has built in functions that call upon more methods
            #     rabbit.aging()
            self._age_rabbits()

            # Calls the method that checks whether they are alive or dead
            # self.rabbit_alive_status()

            # Calls the method that checks how many are alive for each gender during this month
            self.rabbit_gender_status()

            #call breeding function
            new_rabbit_list = RabbitBreeding(self.rabbit_list)
            self.rabbit_list = new_rabbit_list.new_rabbit_list


        if ascending_month == self.month_input:
            print(f"The total number of alive rabbits is: {len(self.rabbit_list)}")
            print(f"The total number of dead rabbits is: {self.dead_rabbits}")

sim = Enclosure()

sim.simulation_start()