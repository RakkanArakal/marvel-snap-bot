from utils import global_utils, android_connection
import os
import cv2
import config
import random
import logging
import cp_calc
import time
import pyautogui


# Given a screenshot of the hand cards, returns a list of the detected cards
def get_my_hand_cards(screenshot, screenshot_dimensions, counter, show_image):
    start = global_utils.start_timer()
    file_name = config.project_path+"\\tmp\\hand_cards_" + str(counter)+".png"
    my_cards = screenshot[config.card_hand['x']:screenshot_dimensions[0] -
                          config.card_hand['y'], 0:screenshot_dimensions[1]]
    cv2.imwrite(file_name, my_cards)
    haystack = file_name
    found_cards = []
    for card_folder in os.listdir(config.data_folder):
        card_folder_path = config.data_folder+"\\"+card_folder
        for card_haystack in os.listdir(card_folder_path):
            card_needle = card_folder_path+"\\"+card_haystack
            card_location = pyautogui.locate(
                card_needle, haystack, grayscale=True, confidence=0.1)
            if card_location:
                already_in_cards_array = False
                for found_card in found_cards:
                    if found_card[0] == card_folder:
                        already_in_cards_array = True
                if not already_in_cards_array:
                    card_to_add = [card_folder, [
                        card_location[0], card_location[1]]]
                    found_cards.append(card_to_add)
    if show_image:
        cv2.imshow("My cards", my_cards)
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_my_hand_cards", end-start)
    return found_cards


# Outputs the hand cards
def log_hand_cards(hand_cards):
    logging.info("Hand_cards: ")
    for hand_card in hand_cards:
        logging.info(hand_card[0])


# Try every card
def try_to_play_every_card(cards, fields):
    for card in cards:
        for field in fields.keys():
            global_utils.click([284, 46])
            global_utils.drag(
                [card[1][0]+20, card[1][1]+1200], fields[field]['move_to'])
            global_utils.click([284, 46])


# Play a card to a certain field
def play_a_card_to_a_field(card_position, field):
    global_utils.click([284, 46])
    global_utils.drag([card_position[0]+20, card_position[1]+1200], field)
    global_utils.click([284, 46])


# Play every card in hand to every possible field
def play_random_cards():
    selected_fields = random.sample([0, 1, 2], 1)
    selected_cards = random.sample([0, 1, 2, 3, 4, 5, 6], 1)
    for field in selected_fields:
        logging.info('* selected_fields : ' + str(field))
        for card in selected_cards:
            logging.info('* selected_cards : ' + str(card))
            global_utils.drag(config.possible_cards[card], config.possible_fields[field])
            # time.sleep(1)
            # global_utils.drag(config.possible_cards[card], config.possible_fields[field])
            # time.sleep(0.1)

            
    # global_utils.click([770, 1500])
    # global_utils.click([450, 200])
    
    # global_utils.click([850, 1500])
    # time.sleep(1)
    # global_utils.click([790, 1490])
    


# Play a certain card in hand to every possible field
def play_a_card_to_every_field(card_position):
    for possible_field in config.possible_fields:
        if len(card_position) > 0:
            global_utils.click([284, 46])
            global_utils.drag(
                [card_position[0]+20, card_position[1]+1200], possible_field)
            global_utils.click([284, 46])
            time.sleep(0.2)


# Make a turn play
def play_cards(play_info, last_move):
    # If we have mana to play
    if play_info['mana'] > 0:
        # Get the best possible card and the field to play
        play_to_make = cp_calc.calc_play(play_info)
        # Check if we are trying to make the same play
        if last_move[1] != play_to_make[1] and last_move[2] != play_to_make[2]:
            # If we know the card and there's a field to play
            if play_to_make[0] == 1 and len(play_info['active_fields']) > 0:
                # Play the card
                play_a_card_to_a_field(
                    play_to_make[1], play_to_make[2])
                # Save the last_move
                last_move = play_to_make
            elif play_to_make[0] == 1:
                play_a_card_to_every_field(play_to_make[1])
                play_random_cards()
            else:
                play_random_cards()
        else:
            play_a_card_to_every_field(play_to_make[1])
            play_random_cards()
    else:
        global_utils.click([755, 1487])
    return last_move
