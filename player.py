import pickle 
import constants as con  
from enums import Klasse, Rasse 

class Player:
    def __init__(self, name, klasse, rasse, level, hp_current, hp_max):
        self.name = name
        self.klasse = klasse
        self.rasse = rasse 
        self.level = level
        self.hp_current = hp_current
        self.hp_max = hp_max

    def get_player_name(self):
        return self.name
    
    def take_potion(self, potion):
        if self.hp_current + potion >= self.hp_max:
            self.hp_current = self.hp_max
        else:
            self.hp_current = self.hp_current + potion

    def take_damage(self, damage):
        if self.hp_current - damage <= 0:
            self.hp_current = 0
            print('Player died!')
        else:
            self.hp_current = self.hp_current - damage
    
    
    def print_info(self):
        print(self.name)
        print(self.klasse)
        print(self.rasse)
        print("level = " + str(self.level))
        print("hp_current= " + str(self.hp_current))

if __name__=='__main__': 
    tungdil = Player('Tungdil', Klasse.Krieger, Rasse.Mensch, 1, con.MIN_HEALTH_START, con.MIN_HEALTH_START)
    path = '/Users/karbo/Documents/dungeonmaster'
    with open('tungdil.pickle', 'wb') as f:
        pickle.dump(tungdil, f)
    print('Datei geschrieben')
    with open('tungdil.pickle', 'rb') as f:
        p2 = pickle.load(f)

    p2.print_info()
    p2.take_damage(40)
    p2.print_info()
    p2.take_potion(con.POTION_HP_REGAIN)
    p2.print_info()
