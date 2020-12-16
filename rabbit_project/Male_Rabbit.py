# very similar to base rabbit class but has an assigned sex as male

## As a user I want the male rabbits to mate an unlimited number of times."

from Rabbit import Rabbit


class MaleRabbit(Rabbit):

    # inherits from rabbit class
    def __init__(self):
        super().__init__()
        self.sex = "M"
        self.available = True




