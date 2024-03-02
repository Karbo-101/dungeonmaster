from game import Game 
from player import Player
import constants as con 
from enums import Klasse, Rasse 


def main():
    g = Game(con.GAME_NAME)
    g.run_game()
    tungdil = Player('Tungdil', Klasse.Krieger, Rasse.Mensch, 1, con.MIN_HEALTH_START, con.MIN_HEALTH_START)
    tungdil.print_info()


if __name__=='__main__':
    main()