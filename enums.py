from enum import Enum
 
class Klasse(Enum):
    Krieger = 1
    Kleriker = 2
    Magier = 3
    Druide = 4


class Rasse(Enum):
    Mensch = 1
    Elf = 2
    Tiefling = 3
    Druide = 4

class GameState(Enum):
    running = 1
    paused = 2