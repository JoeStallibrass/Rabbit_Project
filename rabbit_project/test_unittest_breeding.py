import unittest

from Breeding import *


class TestBreeding(unittest.TestCase):

    rabbit_breeding = RabbitBreeding()


    def test_initialisation(self):
        self.assertFalse(self.rabbit_breeding)



