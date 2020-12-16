import time


# \/ Here we will import the classes which should contain the list/definition
# from RabbitClasses import rabbit_dict

class Enclosure:
    def __init__(self):
        # First we initialise year input by asking user the simulation duration
        # This is where the user fulfills the population limit
        self.year_input = int(input("Enter a number of years:"))
        # The program runs on a monthly basis, so years converted to months and proceeds
        self.month_input = self.year_input * 12
        # Initialise the rabbit list by inheriting it from the other group
        # self.rabbit_list = Breeding.self.function.self.rabbit_list
        self.dead_rabbits = []
        self.alive_rabbits = []
        self.alive_per_month_male = []
        self.alive_per_month_female = []

    def simulation_rate(self):
        # while ascending month hasn't passed the total month input, this method will print one month per second
        ascending_month = 0
        while ascending_month != self.month_input:
            time.sleep(1)
            ascending_month += 1
            print(f"Month {ascending_month}")
            # Here we will print the len of the list from the male and female rabbit Classes

            # alive_population(self)

            print(f" the number of male rabbits alive is {len(self.alive_per_month_male)}")
            print(f" the number of female rabbits alive is {len(self.alive_per_month_female)}")

            # for rabbit in self.rabbit_list:
            #     index[i] += 1  # Where i is the variable for age in their list
            #     if index[i] == 60:
            #         self.dead is True

            # Input the code from Group 3 that is responsible for breeding

        if ascending_month == self.month_input:
            # total_rabbits = len(male dict/class) + len(female dict/class)
            print("the total number of alive rabbits: 1000 (example value)")

            print(f" The total number of dead rabbits is: {len(self.dead_rabbits)}")

    def rabbit_alive_status(self):
        # this function
        for rabbit in self.rabbit_list:
            if self.dead is False:
                self.alive_rabbits.append(rabbit)
            elif self.dead is True:
                self.dead_rabbits().append(rabbit)

    def rabbit_gender_status(self):
        for rabbit in self.rabbit_list:
            if self.sex == "M":
                self.alive_per_month_male.append(rabbit)
            elif self.sex == "F":
                self.alive_per_month_female.append(rabbit)


initiator = Enclosure()
initiator.simulation_rate()
