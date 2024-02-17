
class Game():
    def __init__(self, name):
        self.name = name

print('Welcome to Dungeon Master')

while True:
    question = input('> Wollen Sie spielen? ')

    if question == 'y':
        print('start')
    else:
        break 