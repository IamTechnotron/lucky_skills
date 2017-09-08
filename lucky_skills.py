#!/usr/bin/env python3

from os import path, system
from time import sleep
import War
import fonts

war = War.War()

war.set_stage()


def menu():
    system('clear')
    print("+----------------------------+")
    print("|" + fonts.bar_dark('red') + fonts.bold() + fonts.font_dark('grey') +
          "        LUCKY SKILLS        " + fonts.default() + "|")
    print("+----------------------------+\n")
    print(" 1. " + fonts.font_light('green') + "NEW GAME" + fonts.default())
    if path.isfile(war.dir_path + 'saved_game.txt'):
        print(" 2. " + fonts.font_light('yellow') + "LOAD SAVED GAME" + fonts.default())
        print(" 3. " + fonts.font_light('blue') + "HIGH SCORE" + fonts.default())
        print(" 4. " + fonts.font_dark('purple') + "STORY" + fonts.default())
        print(" 5. " + fonts.font_light('red') + "EXIT" + fonts.default())
        print()
        choice = int(input(">>> "))

    else:
        print(" 2. " + fonts.font_light('blue') + "HIGH SCORE" + fonts.default())
        print(" 3. " + fonts.font_dark('purple') + "STORY" + fonts.default())
        print(" 4. " + fonts.font_light('red') + "EXIT" + fonts.default())
        print()
        choice = int(input(">>> "))
        if choice >= 2:
            choice += 1

    return choice


def resolve_menu():

    choice = menu()

    # New Game
    if choice == 1:
        if path.isdir(war.dir_path):
            print("Entering story mode...")
            war.play_story(1)
        war.new_game()

    # Load Saved Game
    elif choice == 2:
        war.resume()

    # High Score
    elif choice == 3:
        if not path.isfile(war.dir_path + 'stats'):
            print("No High Score as of now!")
        else:
            system('clear')
            print('Score\t\tName')
            with open((war.dir_path + 'game_stats')) as file:
                for line in file:
                    s, n = line.split('~')
                    print(s + '\t\t' + n)
        print('\n\n')
        input("Press any key to continue!")
        system('clear')
        resolve_menu()


    # Story
    elif choice == 4:
        war.play_story()
        print('\n\n')
        input("Press any key to continue!")
        system('clear')
        resolve_menu()

    # Exit
    elif choice == 5:
        print("* Hope to see you soon *")
        exit()

    else:
        print('I haven\' programed any option for this input, sorry!')
        system('clear')
        resolve_menu()

print(fonts.font_dark('green') + "\nPlease switch to full screen, if not already!\n" + fonts.default())
sleep(3)
resolve_menu()
