from os import system, path
from random import randint
from time import sleep
import MagicCards
import attribute
import fonts
import CustomIO


class War:
    """
        This is the War Ground
        There's nothing more to describe.
        Here most of the things are done, by calling different functions and modules.
    """

    def __init__(self):
        """
                This is the constructor for the War Class.
                This initialises:
                usr_data: this is the list containing all the user data. all are initialised with default values'
                index       value                default
                (0)     < player name >     Bill Zuckerberg
                (1)     < health point >            5
                (2)     < attack point >            0
                (3)     < score >                   0
                (4)     < active magic_cards >  1 SHIELD
                (5)     < all magic cards >    1 MEDIPACK
                (6)     < win counter >             0
                (7)     < rounds >                  0
                (8)     < Computer Health Point>    7
                (9)     < Invalid Inputs>          []

                dir_path: the path where all the files are saved at - //home/user/Document/Lucky_Skills
                :return : None
        """
        self.usr_data = ['Bill Zuckerberg', 5, 3, 100, 0, [0, 0, 1, 0, 0], 0, 0, 9, []]
        self.dir_path = '/' + path.expanduser('~') + '/Documents/Lucky_Skills/'
        self.mc = MagicCards.MagicCard()
        self.io = CustomIO.CustomIO()
        self.hp = attribute.Attribute(1)
        self.chp = attribute.Attribute(8)
        self.ap = attribute.Attribute(2)
        self.usr_input = -1
        self.tra_input = 0

    def set_stage(self):
        """
            This sets the stage for  the Battle.
            Creates a directory 'Lucky_Skills' at:
               '/home/current-user/Documents/'
            If the path already exists, do nothing.

            Then it checks if stat.txt exists in the directory or not.
            If it doesn't exits, creates one, with the following content
                No-one < Place-holder for Player - name >
                0      < Place-holder for Player - high score >

        :return: None
        """

        if not path.isdir(self.dir_path):
            system('mkdir ' + self.dir_path)

    def play_story(self, intro=0):

        try:
            system('clear')
            # Play Intro:
            if intro == 1:
                if not path.isfile(path.dirname(path.abspath(__file__)) + '/intro'):
                    print("Data Error")
                    sleep(1)
                    exit()
                else:
                    with open(path.dirname(path.abspath(__file__)) + '/intro') as file:
                        for line in file:
                            if line[0] == '*':
                                print(line, end='')
                                sleep(randint(0, 1))
                                continue
                            sleep(1)

                            if line[0] == '.':
                                system('clear')

                            elif line[0] == '>':
                                ch = input()
                                if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                                    continue
                                elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                                    print("sorry I bothered you!.... ")
                                    sleep(1)
                                    print("Connection Terminated by other user!")
                                    exit()
                                else:
                                    print("Connection Error")
                                    exit()
                            else:
                                self.io.typel(line, 0.1)

            system('clear')
        except KeyboardInterrupt:
            print("\n\n* Keyboard Interrupt... *\n")
            print("* MOVING ON TO DISPLAYING STORY *")

        try:
            # Play Story
            if not path.isfile(path.dirname(path.abspath(__file__)) + '/story'):
                print("Data Error")
            else:
                with open(path.dirname(path.abspath(__file__)) + '/story') as file:
                    for line in file:

                        if line[0] == '>':
                            ch = input()
                            if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                                continue
                            elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                                print("sorry I bothered you!.... ")
                                print("Connection Terminated by other user!")
                            else:
                                print("Connection Error")
                        else:
                            self.io.typel(line, 0.1)
            system('clear')
        except KeyboardInterrupt:
            print("\n\n* Keyboard Interrupt... *\n")
            print("* MOVING ON TO DISPLAYING INSTRUCTIONS *")

        try:
            # Play Rules
            if intro == 1:
                if not path.isfile(path.dirname(path.abspath(__file__)) + '/rules'):
                    print("Data Error")
                else:
                    with open(path.dirname(path.abspath(__file__)) + '/rules') as file:
                        for line in file:
                            self.io.typel(line, 0.1)
            print()
        except KeyboardInterrupt:
            print("\n\n* Keyboard Interrupt... *\n")
            print("* God save you... you just skipped Instructions... *")

    def display_resource(self):
        """
            Displays the current resource list:
            Magic cards, Health Point and Attack Point and Score
            :return: None
        """

        # Bar 1
        print(fonts.bar_dark('white'))
        self.io.print_spaces(90)
        print(fonts.default())
        print()

        # Player Name
        print('  ', end='')
        print(fonts.font_dark('aqua') + fonts.bold() + "PLAYER      : " + fonts.default(), end='')
        print(self.usr_data[0].upper())

        # Magic Cards
        print('  ', end='')
        self.mc.display_card_resource(self.usr_data)

        # Player Health Point
        print('  ', end='')
        self.hp.value_bar(self.usr_data)

        # Break
        self.io.print_spaces(8)
        print('|', end='')
        self.io.print_spaces(8)

        # Computer Health Point
        self.chp.value_bar(self.usr_data)
        print()

        # Attack Point
        print('  ', end='')
        self.ap.value_bar(self.usr_data)

        # Break
        self.io.print_spaces(8)
        print('|', end='')
        self.io.print_spaces(8)

        # Score
        print(fonts.font_light('purple') + fonts.bold() + fonts.underline() + 'SCORE: ', self.usr_data[3])
        print(fonts.default())

        # Any active Magic Card
        if int(self.usr_data[4]) >= 0:
            # print(fonts.bar_light('grey'), ' ' + fonts.default() + '  ', end='')
            print(fonts.font_dark(self.mc.color_code[self.mc.card_list[self.usr_data[4]]]) + fonts.underline() +
                  fonts.bold() + '* ' + self.mc.card_list[self.usr_data[4]], '*' + fonts.font_dark('grey') +
                  ' is active!' +
                  fonts.default())
            # print(fonts.bar_light('grey'), ' ', end='')

        # Bar 2 (zebra)
        self.io.zebra_bar('grey', 'white', 96)
        print('\n')

    def inputs(self):
        """
        This function checks for a correct input from user and TRA!
        :return: None
        """

        # User input
        self.usr_input = int(input(fonts.font_dark('green') + "Your Chance: " + fonts.default()))

        while self.usr_input > 19 or self.usr_input <= 0:
            print(fonts.bar_dark('red') + '* Please enter correctly *' + fonts.default())
            self.usr_input = int(input(fonts.font_dark('green') + "Your Chance: " + fonts.default()))

        while self.usr_input in self.usr_data[9]:
            print(fonts.font_dark('red') + '* Number Locked *' + fonts.default())
            self.usr_input = int(input(fonts.font_dark('green') + "Your Chance: " + fonts.default()))

        self.usr_data[9].append(self.usr_input - 1)
        self.usr_data[9].append(self.usr_input)
        self.usr_data[9].append(self.usr_input + 1)

        if self.usr_data[7] >= 3:
            self.usr_data[9].pop(0)
            self.usr_data[9].pop(1)
            self.usr_data[9].pop(2)

        # computer input
        tra_input_temp = int(randint(1, 90) % 20) or randint(1, 19)
        while self.tra_input == tra_input_temp:
            tra_input_temp = int(randint(1, 90) % 20) or randint(1, 19)

        self.tra_input = tra_input_temp
        self.io.speech_tra('I took %d' % self.tra_input, 1)

    def battle(self):
        """
            The main battle is fought here.
            This module is called by new_round module.
            # Check who wins & take measures
            add more dialogs here
            1. check for any active card
            if yes do action
            2. If the user wins, ask for his action if his attack point > 3
            whether he wants to attack or pass.
            if he passes, Attack point + 1
            if he attacks, asks for the attack strength
            Attack point - strength and computer health point - Strength
            if his AP <= 3: prompt he can't attack
            Increase the win_counter.
            check if the counter is 3 or not.
            If 3, launch magic card generation.
            3. If player looses user HP - 1
                win_counter = 0
            :return: None
            """

        self.inputs()
        usr_input = self.usr_input
        tra_input = self.tra_input
        # when user looses
        if tra_input > usr_input:

            self.io.speech_tra('haha, I won this round...', 1)
            if self.usr_data[4] == 0:
                self.io.speech_bill('Hold Your horses... My have my Shield Card...', 1)
                self.io.speech_tra('Damn you, Humaaan!', 1)
                self.usr_data[4] = -1

            elif self.usr_data[4] != 0:
                self.io.speech_bill('We lost our active  Magic Card! :(  and 1 Health Point!')
                if self.usr_data[1] > 0:
                    self.usr_data[1] -= 1
                else:
                    print(fonts.bold() + fonts.bar_light('red') + "* YOU ARE DEAD! *" + fonts.default())
                self.usr_data[4] = -1
            # reset the win-counter
            self.usr_data[6] = 0

        # when user wins
        elif tra_input < usr_input:
            self.io.speech_tra('Damn it. I will win next round.', 1)
            self.usr_data[6] += 1
            self.usr_data[3] += 100
            if self.usr_data[2] > 3:
                self.io.speech_bill('Should we attack?')
                ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
                if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                    self.usr_data[2] -= 1
                    self.usr_data[8] -= 1
                    self.usr_data[3] += 50
                    self.io.speech_bill('Heyo TRA, here goes your life point! Haha!', 0)
                    if self.usr_data[1] > 5:
                        self.io.speech_bill('You know what TRA, I\'m loving this game!', 0)
                        self.io.speech_tra('Don\'t fly too high, Zuckerberg!', 1)
                elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                    self.io.speech_bill('Great idea! Let\'s this round and increase the Attack point')
                    self.io.speech_bill('I\'ll pass this round!', 0)
                    if self.usr_data[2] < 10:
                        self.usr_data[2] += 1
                    else:
                        print("* Attack Point is already Full *")
                else:
                    self.io.speech_bill('Damn, again that Time Machine Glitched!')
                    self.io.speech_bill('Sorry didn\'t got you!. Anyway, passing this round!')
                    if self.usr_data[2] < 10:
                        self.usr_data[2] += 1
                    else:
                        print("* Attack Point is already Full *")

            else:
                self.io.speech_bill('Damn, our Attack point is too low to attack!')
                self.usr_data[2] += 1

            if self.usr_data[4] == 3 or self.usr_data[4] == 4:
                self.io.speech_bill("But wait, the round is still left! Wait till the Magic Card kicks in...")
                self.io.speech_tra("Hey, wait... your Magic Card effect is still left, isn't it?", 2)
                self.io.speech_bill("Hell Yeah!", 0)
                self.mc.runtime_card_deploy(self.usr_data)

        # Mach draw.
        else:
            self.io.speech_bill('See TRA, we are so much alike. we even think the same!', 0)
            self.io.speech_tra('Oh! Shut up!', 1)
            if self.usr_data[4] == 3 or self.usr_data[4] == 4:
                self.io.speech_tra('Come on, play you shit card! what are you waiting for?', 1)
                self.io.speech_bill('You asked for it...', 0)
                self.mc.runtime_card_deploy(self.usr_data, self.usr_data[4])
            elif self.usr_data[4] == 0:
                self.io.speech_bill('We lost our Shield Card! Bad Luck!')
                self.usr_data[4] = -1
            self.usr_data[6] = 0

        # Grant a MC if Win_count = 3 and a bonus score boost
        if self.usr_data[6] == 3:
            self.mc.gen_mc_normal(self.usr_data)
            self.io.speech_bill('Score Bonus... +300 for continuous 3 wins!')
            self.usr_data[3] += 300

    def save_game(self):
        """
            This saves the current game.
            It creates the file saved_game.txt at the directory.
            saved_game.txt format:
            < player name >
            < health point >
            < attack point >
            < score >
            < active magic_cards >
            < all magic cards >
            < win counter >
            < rounds >
            They are stored in a list called 'usr_data'

            :return: None
        """
        if not path.isfile(self.dir_path + 'saved_game.txt'):
            system('touch ' + self.dir_path + 'saved_game.txt')

        with open(self.dir_path + 'saved_game.txt', 'w') as file:
            for value in self.usr_data:
                value = str(value) + '\n'
                file.write(value)

    def high_score(self):
        """
        If game_stats exists, compare with game data and store it, if needed!
        If game_stats doesn't exist, store the data unconditionally!
        The data is stored in the following format:
        Score~Name
        Top-5 scores are stored!
        :return: None
        """
        if not path.isfile(self.dir_path + 'game_stats.txt'):
            system('touch' + self.dir_path + 'game_stats.txt')
        l = []
        with open((self.dir_path + 'game_stats')) as file:
            for line in file:
                s, n = line.split('~')
                l.append((s, n))
        l.append((self.usr_data[3], self.usr_data[0]))
        l.sort()
        end = len(l) if len(l) > 5 else 5
        index = 0
        with open((self.dir_path + 'game_stats'), 'w') as file:
            for line in l[0:end]:
                file.write(line[index][0] + '~' + line[index][1] + '\n')
            index += 1

    def resume(self):
        """
            This helps to resume a previously saved game.
            Restores the saved values from the file saved_game.txt to the current game.

            :return: the list user data if the game can be resumed.
        """
        print(" * Please wait, resuming game... *")
        sleep(5)
        index = 0
        if path.isfile(self.dir_path + 'saved_game.txt'):
            with open(self.dir_path + 'saved_game.txt') as file:
                for line in file:
                    if index == 0:
                        self.usr_data[index] = line[0:-1]
                    elif index == 5 or index == 9:
                        l = [int(x) for x in line if x not in ['[', ']', ',', ' ', '\n']]
                        self.usr_data[index] = l
                    else:
                        self.usr_data[index] = int(line[:-1])
                    index += 1
        else:
            print("* There is no saved file. Can't resume game. *")
            print("* Starting a new game! *")
            self.usr_data = ['Bill Zuckerberg', 6, 3, 100, 0, [0, 0, 1, 0, 0], 0, 0, 7]

        while self.usr_data[1] != 0 or self.usr_data[8] != 0:
            self.new_round()
        if self.usr_data[8] == 0:
            system('clear')
            print('YOU WON')
        elif self.usr_data[1] == 0:
            system('clear')
            print("YOU LOOSE")

    def new_round(self):
        """
            Stores the High Score if the score is greater than High Score in game_stats.txt file.
            Asks if wants to save the game or not. (3s time-limit) (default ans: Yes)
            If yes, performs the following:
                > calls save_game module.

            Asks for if the user wants to exit or not (3s time-limit) (default ans: No)

            If not exited, then sets up the stage for a new round!
                > Clears up the screen.
                > Calls for resource module to print resources.
                > calls for battle module for battle.

            :return: None
        """

        system('clear')
        self.display_resource()

        # Ask if user wants to activate any MC or not
        # if yes, take action
        if [n for n in self.usr_data[5] if n >= 2]:
            self.io.speech_bill("[Should we generate a magic card? Then we can't activate any other card this round")
            ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
            if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                self.io.speech_bill('I want a magic card no!', 0)
                self.mc.gen_mc_force(self.usr_data)
            elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                self.io.speech_bill('Okay!')
            else:
                self.io.speech_bill('[Bill: There might have been an transmission error in the Time Line.'
                                    'Didn\'t got you! skipping it!')

        elif self.mc.check_cards_if_any(self.usr_data):
            print(fonts.font_light('aqua') + '[Bill: Wanna activate any of our Magic Cards?]' + fonts.default())

            ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
            if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                self.usr_data = self.mc.choose_card(self.usr_data, 1)
            elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                self.io.speech_bill('Okay!')
            else:
                self.io.speech_bill('[Bill: There might have been an transmission error in the Time Line.'
                                    'Didn\'t got you!]')
        self.battle()

        # check if health is 1
        # if yes, activate Medipack if any
        # if no medipack, prompt no medipack, and ask to activate  Insurance (default is yes)

        # If round%3 == 0, Computer's Health rejuvenates. and let the uer know that
        # Used a few different cases to let the user know that same thing! fancy eh!
        if self.usr_data[7] % 3 == 0 and self.usr_data[7] > 2:

            if self.usr_data[8] < 10:
                self.usr_data[8] += 1
                dialog = randint(1, 4)
            else:
                print("* Computer's Health is already Full, So no increment is made *")
                dialog = 0

            if dialog == 1:
                self.io.speech_tra('Yo Suckerberg, my life boosts at this point.', 1)
                self.io.speech_bill('You can\'t win like this. I will. Just to prove you are wrong.', 0)
            elif dialog == 2:
                self.io.speech_tra('Hey Bill, my life point gets a boost at this point. :D', 2)
                self.io.speech_bill('Great! But let\'s hope that helps you!', 0)
            elif dialog == 3:
                self.io.speech_tra('Yo man.. yes! I was waiting for this. Exxxxxtra life points...', 1)
                self.io.speech_bill('You can\'t win like this. I will. Just to prove you are wrong.', 0)
            elif dialog == 4 and self.usr_data[7] > 3:
                self.io.speech_tra('Your demise is near... mine health got boosted, again.', 1)
                self.io.speech_bill('Come on, get real. the game has just begun!', 0)

        # prompt to save game
        self.io.speech_bill('Hey, lets make a check point here.')
        self.io.speech_bill('What do you say?')
        ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
        if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
            # Deploy more dialogs
            self.io.speech_bill('Great idea!')
            self.save_game()

        elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
            # Deploy more dialogs
            self.io.speech_bill('Great! Lets move on!')
            # self.io.speech_bill('Wow, humans of past were soo cool. So let\'s bring that Machine to senses.')

        else:
            self.io.speech_bill('God damn this Time Machine. Sorry din\'t got that. Saving Anyway.')
            self.save_game()
        sleep(3)

        self.io.speech_bill('Would you like to quit? is yes, press y/Y with in 3 sec!')
        print('>>> ', end='')
        exc = self.io.timer_input()
        if exc == 'y' or exc == 'Y':
            self.save_game()
            self.io.speech_bill("Hope to see you soon!")
            exit()

    def new_game(self):
        """

        :return:
        """
        self.io.speech_bill("Whats your name?")
        name = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
        self.usr_data[0] = name

        self.set_stage()
        while self.usr_data[1] != 0 or self.usr_data[8] != 0:
            self.new_round()
        if self.usr_data[8] == 0:
            system('clear')
            print('YOU WON')
        elif self.usr_data[1] == 0:
            print("YOU LOOSE")
        self.high_score()
