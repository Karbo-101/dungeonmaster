# Game constants
GAME_NAME = 'Dungeon Master'
PLAYER_START_PLACE = 'Players_house'

# Character actions
actions = {
    'MOVE', 'TALK', 'TAKE', 'USE', 'ATTACK', 'ESCAPE'
}
# grundlegende Charakterwerte
MIN_HEALTH_START = 50

# NPC und Orte
npcs = {
     'Taverne': {'Wirt', 'Söldner'},
     'Marktplatz': {'Schmied', 'Händler'}
}

# Items
POTION_HP_REGAIN = 20
HIGH_POTION_HP_REGAIN = 50 

# Orte
orte = {
    'Players_house': {'North': 'Marktplatz', 'South': {'Taverne'}},
    'Marktplatz': {'Players_house','Gasthaus'}
}
