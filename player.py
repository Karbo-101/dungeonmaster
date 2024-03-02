import pickle 
import constants as con  
from enums import Klasse, Rasse 

class Player:
    def __init__(self, name, current_place):
        self.name = name
        self.current_place = current_place

    def get_places_to_move(self):
        return con.orte[self.current_place]
    
    def get_current_place(self):
        return self.current_place

    def get_player_name(self):
        return self.name
    def move_to(self, direction):
        pass 

    def get_actions(self):
        pass 

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


if __name__=='__main__': 
    tungdil = Player('Tungdil', con.PLAYER_START_PLACE)
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
