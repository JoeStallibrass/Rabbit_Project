import time
from Male_Rabbit import MaleRabbit
from Female_Rabbit import FemaleRabbit


# Importing Group 1's classes


class Enclosure():

    def __init__(self):
        # First we initialise year input by asking user the simulation duration
        # This is where the user fulfills the 'population limit'
        self.year_input = int(input("Enter a number of years:\n"))

        # The program runs on a monthly basis, so years converted to months and proceeds
        self.month_input = self.year_input * 12

        # Initialise the rabbit list by inheriting it from the other group
        # self.rabbit_list = Breeding.self.function.self.rabbit_list
        self.dead_rabbits = 0
        self.alive_per_month_male = 0
        self.alive_per_month_female = 0
        self.rabbit_list = []

    def starting_pair(self):
        # This method is called at the very start of the simulation to create a starting pair
        self.rabbit_list.append(MaleRabbit())
        self.rabbit_list.append(FemaleRabbit())
        print(len(self.rabbit_list))

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

    def simulation_rate(self):

        # Here the method prints the month for each iteration, at 1 month per second
        self.starting_pair()
        ascending_month = 0


        while ascending_month != self.month_input:
            time.sleep(0.01)
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

        if ascending_month == self.month_input:
            print(f"The total number of alive rabbits is: {len(self.rabbit_list)}")
            print(f"The total number of dead rabbits is: {self.dead_rabbits}")


initiator = Enclosure()
initiator.simulation_rate()
