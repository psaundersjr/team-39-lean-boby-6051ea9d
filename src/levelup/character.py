from levelup.position import Position
from levelup.map import Map
from levelup.controller import *
class Character:
    name = ""

    def __init__(self, character_name):
        if character_name == "":
            character_name = DEFAULT_CHARACTER_NAME
        self.name = character_name
    
    def getName(self):
        return self.name