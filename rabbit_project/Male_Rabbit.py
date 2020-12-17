
import json
from Rabbit import Rabbit


class MaleRabbit(Rabbit):

    # inherits from rabbit class
    def __init__(self):
        super().__init__()
        self.sex = "M"
        self.available = True




