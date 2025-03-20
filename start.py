from utils import android_connection, global_utils
import logging
import info
import hand_cards
import time
import config
import turn
import clear_tmp
import sys
import mana
import argparse
import os
import random
def click_possible_button(screenshot):
    possible_buttons_folder = os.path.join(config.project_path, 'images', 'possible')
    # global_utils.click([580, 1280])
    # global_utils.click([580, 1290])
    
    if(random.random() > 0.8):
        global_utils.click([580, 970])
    
    for filename in os.listdir(possible_buttons_folder):
        file_path = os.path.join(possible_buttons_folder, filename)
        global_utils.find_and_click(file_path, screenshot)
    
    if(global_utils.search(config.project_path+'\\images\\possible\\end3.jpg', screenshot)[0]):
        print("find end")
        global_utils.click([520, 1500])
    return


def click_play_button(screenshot,screenshot_dimensions):

    if(global_utils.search(config.project_path+'\\images\\play_button.png', screenshot)[0]):
        global_utils.click([520, 1500])
        global_utils.click([580, 1550])
        time.sleep(2)
        # global_utils.click([780, 1500])
        # global_utils.click([750, 1550])
        # time.sleep(1)
        global_utils.click([450, 1560])
        time.sleep(5)
        global_utils.find_and_click(config.project_path+'\\images\\play_button.png', screenshot)
        time.sleep(20)
        
    global_utils.find_and_click(
        config.project_path+'\\images\\next_button.png', screenshot)
    
    global_utils.find_and_click(
        config.project_path+'\\images\\turns\\collect_rewards.png', screenshot)
    
    return turn.get_turn(screenshot, screenshot_dimensions, False)

def main(turns):
    
    logging.info("* concede in turns:" + str(turns))

    
    counter = 0
    
    while 1:
        
        # print(f"* concede in turns: {turns}")
        
        screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
        screenshot_dimensions = screenshot.shape
        
        start_time = time.time()
        
        click_possible_button(screenshot)
        player_turn = click_play_button(screenshot,screenshot_dimensions)
        
        # While turn not found
        while 1:
            # counter+=1
            screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            screenshot_dimensions = screenshot.shape
            
            player_turn = click_play_button(screenshot,screenshot_dimensions)
            if player_turn > 0 :
                break
            if time.time() - start_time > 5:
                _mana = mana.get_mana(screenshot, screenshot_dimensions)
                if(_mana > 0) :
                    time.sleep(3)

                    # player_turn = _mana
                    break
                else:
                    click_possible_button(screenshot)
                    print("Loop took too long, breaking out of loop")
                


        # When we get the turn, we look for the other information (mana, hand cards, fields, cards in the field)
        play_info = info.get_info(
            counter, screenshot, screenshot_dimensions, player_turn)

        # Play cards
        # last_move = hand_cards.play_cards(play_info, last_move)
        
        if player_turn == 2 :
            global_utils.click([450, 200])
        if(random.random() > 0.8):
            global_utils.click([450, 200])

        if player_turn >= turns:
            # Auto concede
            time.sleep(5)
            global_utils.click([119, 1484])
            time.sleep(3)
            global_utils.click([290, 1165])

        
        
        if mana.get_mana(screenshot, screenshot_dimensions) > 0 :
            time.sleep(1)
            hand_cards.play_random_cards()
            time.sleep(2)
            hand_cards.play_random_cards()
            time.sleep(2)
            hand_cards.play_random_cards()
            time.sleep(2)
            global_utils.click([850, 1500])
            time.sleep(1)
            global_utils.click([790, 1490])
            time.sleep(1)
            global_utils.click([790, 1490])

        else:
            global_utils.click([800, 1520])
            
        counter += 1
        
        #if False:
        clear_tmp.clear()

    
    
parser = argparse.ArgumentParser(description='Run the main function with a parameter.')
parser.add_argument("turns", type=int, default=8, help="Initial turns value.")
args = parser.parse_args()
    
if __name__ == "__main__":
    
    logging.basicConfig(filename=config.project_path+'\\log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    android_connection.connect()
    
    main(args.turns)