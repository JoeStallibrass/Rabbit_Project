import json
from rabbit_project.Fox import Fox


class MaleFox(Fox):

    # inherits from fox class
    def __init__(self):
        super().__init__()
        self.sex = "M"
        self.available = True
