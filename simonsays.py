import random
import time
import os
import threading
import pyautogui

color_list = ["B", "G", "R", "Y", "P"]
emoji_list = ["🔵​", "🟢", "🔴", "🟡", "🟣", "❌"]

player_list = []
player_emoji_list = []
simon_list = []
simon_emoji_list = []
player_word = "" 
time_limit = 1


def get_input_with_timeout(timeout):
    player_word = None

    def get_input():
        nonlocal player_word
        player_word = input("Insert the sequence: ").upper()

    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    input_thread.join(timeout)

    if input_thread.is_alive():
        return None
    return player_word


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print(f"\n\n*********************************************************************")
    print(f"**                            WELCOME TO                           ** ")
    print(f"**********************        SIMON SAYS       ********************** ")
    print(f"**                                                                 ** ")
    print(f"*********************************************************************\n\n")
    print("                          This is a memory game")
    print("             Observe what Simon says and repeat the sequence\n")

    input('                      PRESS ENTER TO PLAY!!!!!')
    print('                     ---------------------------                      \n\n\n   ')


menu()
in_game = True
while in_game:
    time.sleep(1.5)  
    random_word = random.choice(color_list)

    
    if random_word == "B":
        simon_emoji_list.append(emoji_list[0])
    elif random_word == "G":
        simon_emoji_list.append(emoji_list[1])
    elif random_word == "R":
        simon_emoji_list.append(emoji_list[2])
    elif random_word == "Y":
        simon_emoji_list.append(emoji_list[3])
    else:
        simon_emoji_list.append(emoji_list[4])

    print('SIMON SAYS: ', ''.join(simon_list) + random_word, "\n\n")
    time.sleep(2)
    clean_screen()

    clean_screen()
    time_limit = 5  

    def simulate_enter():
        time.sleep(0.5)  
        pyautogui.press('enter')

    thread = threading.Thread(target=simulate_enter)
    thread.start()

    input("     ")

    player_word = get_input_with_timeout(time_limit)

    if player_word is None:  
        print("\n\n               ¡¡¡¡¡¡ TOO SLOW !!!!!")
        in_game = False
        break

    clean_screen()

    simon_list.append(random_word)
    simon_word = ''.join(simon_list)
    player_list.append(player_word[len(player_word) - 1:])

    if simon_word != player_word:
        in_game = False
    if len(player_list) == 10:
        break

if len(player_list) == 10 and player_word == simon_word:
    print("\n\n                  THIS IS THE CORRECT SEQUENCE:\n")
    print("                          ", ''.join(simon_emoji_list))
    print("\n                      THIS WAS YOUR SEQUENCE:\n")
    if not player_word:
        player_emoji_list.append(emoji_list[5])  
    else:
        for i in player_word:
            if i == "B":
                player_emoji_list.append(emoji_list[0])
            elif i == "G":
                player_emoji_list.append(emoji_list[1])
            elif i == "R":
                player_emoji_list.append(emoji_list[2])
            elif i == "Y":
                player_emoji_list.append(emoji_list[3])
            elif i == "P":
                player_emoji_list.append(emoji_list[4])
            else:
                player_emoji_list.append(emoji_list[5])  

    print("                          ", ''.join(player_emoji_list), "\n")
    print("\n                          ¡¡¡¡ YOU WIN !!!!\n")
else:
    print("\n\n                   THIS IS THE CORRECT SEQUENCE:\n")
    print("                          ", ''.join(simon_emoji_list))
    print("\n                       THIS WAS YOUR SEQUENCE:\n")

    if not player_word or player_word is None:
        player_emoji_list.append(emoji_list[5])  
    else:
        for i in player_word:
            if i == "B":
                player_emoji_list.append(emoji_list[0])
            elif i == "G":
                player_emoji_list.append(emoji_list[1])
            elif i == "R":
                player_emoji_list.append(emoji_list[2])
            elif i == "Y":
                player_emoji_list.append(emoji_list[3])
            elif i == "P":
                player_emoji_list.append(emoji_list[4])
            else:
                player_emoji_list.append(emoji_list[5])  

    print("                          ", ''.join(player_emoji_list), "\n")
    print("\n                        ¡¡¡¡ YOU FAIL !!!!\n")
