# # Character actions
actions = {
    'MOVE', 'TALK'
}

orte = {
    'Players_house': {'North': 'Marktplatz', 'South': 'Taverne'},
    'Marktplatz': {'North': 'Players_house', 'EAST': 'Gasthaus'},
    'Taverne': {'North': 'Players_house',}
}


npcs = {
     'Taverne': {'Wirt', 'Söldner'},
     'Marktplatz': {'Schmied', 'Händler'}
}
# print(orte['Players_house']['NPC'])

#current_place = 'Players_house'
# for action in actions:
#     if action == 'MOVE':
#         print('you can ' + action + ' to ' + str(orte[current_place]) + '\n')

    
    # elif action == 'TALK':
    #     print('you can ' + action + ' to ' + str(orte[current_place]['NPC']) + '\n')



# print(orte[current_place])