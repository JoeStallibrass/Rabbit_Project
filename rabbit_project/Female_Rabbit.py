# takes from base rabbit class but adds pregnancy boolean

from rabbit_project.Rabbit import Rabbit


class FemaleRabbit(Rabbit):

    # inherits from rabbit class
    # initialises with pregnant = False
    def __init__(self):
        super().__init__()
        self.sex = "F"
        self.pregnant = False



