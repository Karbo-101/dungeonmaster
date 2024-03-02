from game import Game 
from player import Player
import constants as con 
from enums import Klasse, Rasse 


def main():
    g = Game(con.GAME_NAME)
    tungdil = Player('Tungdil', con.PLAYER_START_PLACE)
    print('You are playing ' + tungdil.get_player_name())
    print('You can MOVE to ' + str(tungdil.get_places_to_move()))
    #print(tungdil.get_current_place())
   #print('You can MOVE to ' + str(tungdil.get_places_to_move()))



if __name__=='__main__':
    main()