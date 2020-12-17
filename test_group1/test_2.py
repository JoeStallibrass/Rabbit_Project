from rabbit_project.Female_Rabbit import *
from rabbit_project.Male_Rabbit import *
from rabbit_project.Enclosure import *
from rabbit_project.Breeding import *

class breeding_test(unittest.TestCase):

    breeding = RabbitBreeding()

    def test_init(self):
        self.assertFalse(self.breeding.new_rabbit_list)
        self.assertTrue(self.breeding.rabbit_list)

    def test_breeding_check_true(self):
        # check that breeding is true when there is at least one available male rabbit
        self.assertTrue(self.breeding.breed_check())

    def test_breeding_check_false(self):
        # check that breeding is false when there are no available male rabbits
        self.assertFalse(self.breeding.breed_check())

    def test_check_age(self):
        # initialise with one pregnant rabbit
        self.assertFalse(self.breeding.rabbit.pregnant)
        # initialise with a not preg rabbit - 50/50 chance of pregnancy to be tested manually
        # if rabbit not mature, nothing happens
        self.assertFalse(self.breeding.rabbit.pregnant)
        # possibly check if there are dead rabbits?

    def test_give_birth(self):
        self.breeding.give_birth()
        self.assertTrue(self.breeding.new_rabbit_list)

    def test_new_population(self):
        self.assertGreaterEqual(self.breeding.new_rabbit_list, self.breeding.rabbit_list)