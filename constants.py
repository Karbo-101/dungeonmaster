# grundlegende Charakterwerte
MIN_HEALTH_START = 50

# Items
POTION_HP_REGAIN = 20
HIGH_POTION_HP_REGAIN = 50 

# NPCs
NPCS = ['Händler', 'Bürgermeister Fallenberg', 'Carlo der Schmied']

# Orte
orte = {
    'Players_house': {'North': 'Marktplatz', 'South': 'Taverne'},
    'Marktplatz': {'Players_house','Gasthaus'}
}
