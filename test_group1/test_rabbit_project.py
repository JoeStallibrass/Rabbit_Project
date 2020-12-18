from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
from rabbit_project.Enclosure import *
from rabbit_project.Breeding import *
from rabbit_project.Rabbit import *
import unittest

class rabbit_test(unittest.TestCase):
    enclosure = Enclosure()
    breeding = RabbitBreeding(enclosure)
    male_rabbit = MaleRabbit()
    female_rabbit = FemaleRabbit()
    rabbit = Rabbit()

    # Sex user story
    def test_male_available(self):
    # A test that checks whether the male rabbits are capable of mating.
    # here we need something that checks if the male is available and if it's more than three months old
        self.assertEqual(self.male_rabbit.sex, 'M')
        self.assertTrue(self.male_rabbit.mature)
        self.assertTrue(self.male_rabbit.available)
    def test_female_pregnant(self):
    # A test that checks whether the female rabbits are capable of becoming pregnant.
    # we need a method that checks if the female is no pregnant and is not on cooldown period and is mature
        self.assertEqual(self.female_rabbit.sex, 'F')
        self.assertTrue(self.female_rabbit.mature)
        self.assertFalse(self.female_rabbit.pregnant)
    # review
    def test_mating_true(self):
    # A test that shows that they have mated
    # we need to check if the there was a birth and added to the list

        self.assertNotEqual(len(self.breeding.new_rabbit_list), len(self.breeding.rabbit_list))
    # needs help and review
    #Simulation time limit user story
    # The simulation run time matches the user's input.
    # The limit is embedded in the simulation rate method.
    # Current population each month
    # A test to make sure the current population per month is accurate
    def test_current_population(self):
        self.assertEqual(len(self.breeding.new_rabbit_list), len(self.enclosure.rabbit_list))
    # A test to make sure the current month is accurate
    #Manual Testing
    # Offspring
    # There is a random number of offspring between 1 and 14.
    def test_offspring(self):
        self.assertLessEqual(self.breeding.max_num_babies, 15)

    # A 50% chance for each offspring to be male or female.
    def sex_probability(self):
        self.assertEqual(self.breeding.ratio_male_female, 0.5)

    # RABBIT MATURITY
    # D.O.D.
    # It passes the unit test where the rabbit reaches the mark of three months.
    # It also passes the test where the rabbit is marked as mature at three months is true.
    # The feature works and is embedded into the main code.
    def test_rabbit_mature(self):
        self.assertGreaterEqual(self.rabbit.mature, 3)
        self.assertTrue(self.rabbit.mature)

    # SIMULATION RATE
    # D.O.D.
    # The simulation method prints the current month per method.
    ## maybe manual testing?

    # FEMALE UNAVAILABILITY WINDOW
    # D.O.D.
    # A test that shows the female rabbit being unavailable every other month.
    # A test that shows that the female rabbit can only become pregnant when it is available.
    def test_female_unavailability_window(self):
        self.assertFalse(self.female_rabbit.pregnant)
        self.assertTrue(self.female_rabbit.mature)

    # starting pair
    # check that list has one male and one female on initialisation
    def test_starting_pair_test(self):


        self.enclosure.starting_rabbits()
        male = 0
        female = 0
        for rabbit in self.enclosure.rabbit_list:
            if rabbit.sex == "M":
                male += 1
            if rabbit.sex == "F":
                female += 1

        self.assertEqual(male, 1)
        self.assertEqual(female, 1)


    # male mating capability
    # checks that breeding is set to True when one male is available
    def test_breeding_check_true(self):
        # check that breeding is true when there is at least one available male rabbit
        self.assertTrue(self.breeding.breed_check())
    def test_breeding_check_false(self):
        # check that breeding is false when there are no available male rabbits
        self.assertFalse(self.breeding.breed_check())

    # # male rabbit mating cool down
    # def test_mating_cool_down(self):
    #     self.enclosure.starting_rabbits()
    #
    #     for i in range(len(self.enclosure.rabbit_list)):
    #         if self.enclosure.rabbit_list[i].sex == "M":
    #             male_rabbit = self.enclosure.rabbit_list[i]
    #
    #     self.enclosure.simulation_start()
    #     while self.enclosure.ascending_month <= 5:
    #
    #
    #         if self.enclosure.ascending_month == 3:
    #             self.assertTrue(self.male_rabbit.available)
    #         if self.enclosure.ascending_month == 4:
    #             self.assertFalse(self.male_rabbit.available)

    # # Count of Alive and Dead
    def test_alive_dead_count(self):
        self.enclosure.simulation_start()

        self.assertTrue(self.enclosure.rabbit_list)
        self.assertTrue(self.enclosure.dead_rabbits)



