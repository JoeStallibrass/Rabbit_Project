
from Rabbit import Rabbit
import json
class FemaleRabbit(Rabbit):

    # inherits from rabbit class
    # initialises with pregnant = False
    def __init__(self):
        super().__init__()
        self.sex = "F"
        self.pregnant = False


