from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
from rabbit_project.Enclosure import *
from rabbit_project.Rabbit import *
from rabbit_project.Breeding import *
import unittest

class GenTesting(unittest.TestCase):
    male_rabbit = MaleRabbit()
    female_rabbit = FemaleRabbit()
    breeding = RabbitBreeding

    def test_male_available(self):
        # A test that checks whether the male rabbits are capable of mating.
        # here we need something that checks if the male is available and if it's more than three months old
        self.assertEqual(self.male_rabbit.sex, 'M')
        self.assertTrue(self.male_rabbit.mature)
        self.assertTrue(self.male_rabbit.available)
        # A test that checks whether the female rabbits are capable of becoming pregnant.
        # we need a method that checks if the female is no pregnant and is not on cooldown period and is mature

    def test_female_pregnant(self):

        self.assertEqual(self.female_rabbit.sex, 'F')
        self.assertTrue(self.female_rabbit.mature)
        self.assertFalse(self.female_rabbit.pregnant)

    # A test that shows that they have mated

    def test_meting_true(self):
        self.assertTrue(self.new_rabbit_list)