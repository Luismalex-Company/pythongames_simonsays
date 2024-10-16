import random
import time
import os


color_list=["B","G","R","Y","P"]
emoji_list=["🔵​","🟢","🔴","🟡","🟣", "❌"]

player_list=[]
player_emoji_list = []
simon_list=[]
simon_emoji_list = []
player_word="" #input
time_limit = 1



def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# show line on screen

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
in_game=True
while  in_game==True:     
    print("SIMON SAYS!\n")#hay que modificar esta línea
    time.sleep(2)  # wait 2 seconds
    random_word= random.choice(color_list)
    #append colors in simon_emoji_list
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

    print(''.join(simon_list)+random_word, "\n\n")
    time.sleep(0.75)
    clean_screen()
   
    input("Press Enter to start your input...")
    clean_screen()
    start_time = time.time()
    while True:
        current_time = time.time()
        time_difference =current_time - start_time
        if time_difference > time_limit:
            break
        player_word = input("Insert the sequence: ").upper().strip()

    clean_screen()
    simon_list.append(random_word)
    simon_word=''.join(simon_list)
    player_list.append(player_word[len(player_word)-1:])
    
    if simon_word!=player_word:
        in_game=False
    if len(player_list) == 5:
        break

    


if len(player_list) == 5:
    print("\n\n                  THIS IS THE CORRECT SEQUENCE:\n")
    print("                          ",''.join(simon_emoji_list))
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
            elif i == '': 
                player_emoji_list.append(emoji_list[5])
            else: 
                player_emoji_list.append(emoji_list[5])

    print("                          ",''.join(player_emoji_list),"\n")
    print("\n                               YOU WIN\n")
else:
    
    print("\n\n                   THIS IS THE CORRECT SEQUENCE:\n")
    print("                          ",''.join(simon_emoji_list))
    print("\n                       THIS WAS YOUR SEQUENCE:\n")
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
            elif i == '': 
                player_emoji_list.append(emoji_list[5])
            else: 
                player_emoji_list.append(emoji_list[5])

        print("\n                             YOU FAIL\n")

    print("                          ",''.join(player_emoji_list),"\n")
            
