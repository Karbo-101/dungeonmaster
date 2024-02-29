# Game constants
GAME_NAME = 'Dungeon Master'

# grundlegende Charakterwerte
MIN_HEALTH_START = 50

# Items
POTION_HP_REGAIN = 20
HIGH_POTION_HP_REGAIN = 50 

# NPCs
NPCS = {'Wirt'}

# Orte
orte = {
    'Players_house': {'North': 'Marktplatz', 'South': {'Taverne': {'Wirt'}}},
    'Marktplatz': {'Players_house','Gasthaus'}
}
