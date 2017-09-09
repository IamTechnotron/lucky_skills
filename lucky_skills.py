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
        print(" 5. " + fonts.font_light('white') + "INSTRUCTIONS" + fonts.default())
        print(" 6. " + fonts.font_light('red') + "EXIT" + fonts.default())
        print()
        choice = int(input(">>> "))

    else:
        print(" 2. " + fonts.font_light('red') + "EXIT" + fonts.default())
        print()
        choice = int(input(">>> "))
        if choice == 2:
            choice = 6

    return choice


def resolve_menu():
    try:
        choice = menu()

        # New Game
        if choice == 1:
            if not path.isfile(war.dir_path + 'saved_game.txt'):
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

        # Instructions
        elif choice == 5:
            try:
                if not path.isfile(path.dirname(path.abspath(__file__)) + '/rules'):
                    print("Data Error")
                else:
                    with open(path.dirname(path.abspath(__file__)) + '/rules') as file:
                        for line in file:
                            war.io.typel(line, 0.1)
                print()
            except KeyboardInterrupt:
                print("\n\n* Keyboard Interrupt... *\n")
            input("Press any key to continue!")
            system('clear')
            resolve_menu()

        # Exit
        elif choice == 6:
            print("* Hope to see you soon *")
            sleep(2)
            system('clear')
            exit()

        else:
            print('This program haven\'t been programed with any operation for this input, sorry!')
            system('clear')
            resolve_menu()

    except KeyboardInterrupt:
        print("\n\n SEE YOU SOON... \n")
        sleep(2)
        system('clear')

if __name__:
    print(fonts.font_dark('green') + "\nPlease switch to full screen, if not already!\n" + fonts.default())
    sleep(3)
    resolve_menu()

