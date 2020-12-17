from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
from rabbit_project.Enclosure import *
from rabbit_project.Breeding import *
import unittest

class rabbit_test(unittest.TestCase):

    enclosure = Enclosure()

    # starting pair
    # check that list has one male and one female on initialisation
    def test_starting_pair_test(self):
        self.enclosure.starting_pair()
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
    def test_mating_cool_down(self):
        self.enclosure.starting_pair()

        for i in range(len(self.enclosure.rabbit_list)):
            if self.enclosure.rabbit_list[i].sex == "M":
                male_rabbit = self.enclosure.rabbit_list[i]

        self.enclosure.simulation_rate()
        while self.enclosure.ascending_month <= 5:


            if self.enclosure.ascending_month == 3:
                self.assertTrue(male_rabbit.available)
            if self.enclosure.ascending_month == 4:
                self.assertFalse(male_rabbit.available)

    # # Count of Alive and Dead
    def test_alive_dead_count(self):
        self.enclosure.simulation_rate()

        self.assertTrue(self.enclosure.rabbit_list)
        self.assertTrue(self.enclosure.dead_rabbits)



