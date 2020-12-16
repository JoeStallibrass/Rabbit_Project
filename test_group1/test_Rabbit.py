from rabbit_project.Rabbit import Rabbit
from rabbit_project.Female_Rabbit import FemaleRabbit
from rabbit_project.Male_Rabbit import MaleRabbit

import unittest

class rabbit_test(unittest.TestCase):

    rabbit = Rabbit()

    def test_init(self):
        self.assertFalse(self.rabbit.dead)
        self.assertFalse(self.rabbit.mature)

    def test_aging(self):
        self.rabbit.aging()
        self.assertEquals(self.rabbit.age, 1)

    def test_death(self):
        self.rabbit.age = 59
        self.rabbit.death()
        self.assertFalse(self.rabbit.dead)

    def test_maturity(self):
        self.rabbit.age = 2
        self.rabbit.maturity()
        self.assertFalse(self.rabbit.mature)


class male_rabbit_test(unittest.TestCase):

    male_rabbit = MaleRabbit()

    def test_init(self):
        self.assertEqual(self.male_rabbit.sex, "M")

class female_rabbit_test(unittest.TestCase):
    female_rabbit = FemaleRabbit()

    def test_init(self):
        self.assertEqual(self.female_rabbit.sex, "F")
        self.assertFalse(self.female_rabbit.pregnant)




