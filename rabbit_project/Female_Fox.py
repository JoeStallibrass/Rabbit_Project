
from rabbit_project.Fox import Fox
import json
class FemaleFox(Fox):

    # inherits from Fox class
    # initialises with pregnant = False
    def __init__(self):
        super().__init__()
        self.sex = "F"
        self.pregnant = False