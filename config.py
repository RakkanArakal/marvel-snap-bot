adb_path = 'C:/Program Files/Netease/MuMu Player 12/shell'
project_path = 'C:\\Users\\Shulin\\Desktop\\github\\AutoBot\\marvel-snap-bot'
images_folder = project_path + '\\images'
fields_folder = images_folder + '\\fields'
mana_folder = images_folder + '\\mana'
turns_folder = images_folder + '\\turns'
data_folder = project_path + '\\data'
tmp_path = project_path + '\\tmp'
example_data_path = images_folder + '\\example_data'
tmp_image_without_bg_path = tmp_path + \
    '\\hand_cards_number_without_background.png'
tmp_hand_cards_number_path = tmp_path + '\\hand_cards_number.png'

global_adb_port = '127.0.0.1:16384'

first_field = {
    'name': 'First field',
    'x1': 610,
    'x2': 700,
    'y1': 100,
    'y2': 1500,
    'move_to': [198, 1036],
}
second_field = {
    'name': 'next_turn',
    'x1': 600,
    'x2': 720,
    'y1': 350,
    'y2': 350,
    'move_to': [455, 1036],
}
third_field = {
    'name': 'next_2_turns',
    'x1': 610,
    'x2': 700,
    'y1': 600,
    'y2': 90,
    'move_to': [711, 1036],
}
fields = {
    'first_field': first_field,
    'second_field': second_field,
    'third_field': third_field
}
card_hand = {
    'x': 1170,
    'y': 170
}
first_terrain_my_played_cards = {
    'x1': 80,
    'x2': 1450,
    'y1': 890,
    'y2': 380,
    'cards': {
        'first_card': [172, 906],
        'second_card': [270, 910],
        'third_card': [164, 1050],
        'forth_card': [270, 1046],
    },
}
second_terrain_my_played_cards = {
    'x1': 280,
    'x2': 1200,
    'y1': 890,
    'y2': 380,
    'cards': {
        'first_card': [437, 888],
        'second_card': [532, 888],
        'third_card': [424, 1036],
        'forth_card': [532, 1036],
    }
}
third_terrain_my_played_cards = {
    'x1': 600,
    'x2': 970,
    'y1': 890,
    'y2': 380,
    'cards': {
        'first_card': [695, 910],
        'second_card': [797, 912],
        'third_card': [703, 1053],
        'forth_card': [809, 1053],
    }
}
fields_my_played_cards = {
    'first_terrain_my_played_cards': first_terrain_my_played_cards,
    'second_terrain_my_played_cards': second_terrain_my_played_cards,
    'third_terrain_my_played_cards': third_terrain_my_played_cards
}
mana = {
    'x1': 400,
    'x2': 1285,
    'y1': 1440,
    'y2': 50,
}
turn = {
    'x1': 650,
    'x2': 0,
    'y1': 1440,
    'y2': 50,
}
possible_fields = [[198, 1136], [455, 1136], [711, 1136]]

# possible_cards = [[290, 1300], [441, 1300],
#                   [517, 1300], [700, 1300],
#                   [100, 1300]]

possible_cards = [[155, 1300], [255, 1300],
                  [355, 1300], [455, 1300],
                  [555, 1300], [655, 1300],
                  [755, 1300]]
