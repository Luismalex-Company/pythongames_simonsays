import random
import time
import os


color_list=["B","G","R","Y","P"]
emoji_list=["🔵​","🟢","🔴","🟡","🟣"]

player_list=[]
simon_list=[]
player_word="" #input



def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Mostrar la línea en pantalla
""" print("SIMON SAYS!")#hay que modificar esta línea
time.sleep(2)  # Esperar 1 segundo
random_word= random.choice(color_list)
print(''.join(simon_list),random_word)
time.sleep(3)
simon_list.append(random_word) """


in_game=True
while  in_game==True:     #simon_list==player_list or
    print("SIMON SAYS!")#hay que modificar esta línea
    time.sleep(2)  # Esperar 2 segundos
    random_word= random.choice(color_list)
    print(''.join(simon_list)+random_word)
    time.sleep(1)
    clean_screen()
   
    player_word = input("Insert the sequence: ").upper()
    simon_list.append(random_word)
    variable_hijaputa=str(simon_list)
    player_list.append(player_word)
    if variable_hijaputa!=player_word:
        in_game=False
    

print(simon_list)
            
