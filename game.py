import time
from player import Player
class Game:
    def __init__(self, name):
        self.name = name
        self.game_duration = None

    def get_name(self):
        return self.name
    
    def meassure_game_time(self):
        t = time.time()
    
    def create_start_screen(self):
        print()
        print('##########################################################')
        print('Welcome to ' + self.get_name())
        print('##########################################################')
        
    
    def save_game(self):
        print('Game saved')

    def load_game(self):
        pass 
    
    def run_game(self):
        while True:
            question = input('> Wollen Sie spielen? ')
            if question == 'y':
                while True:
                    self.create_game_screen()
            else:
                break 
# Places



if __name__ == '__main__':
    dm = Game('Dungeon Master')
    Game.run_game(dm)