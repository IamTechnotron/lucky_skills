from random import randint
from sys import stdout
import CustomIO
import fonts


class MagicCard:
    """
    The Home of all Magic-cards.
    Types of Magic card:
        >>  SHIELD      : Protects Health Point for 1 failing round (the very next round)
        >>  CANON       : Destroys opponent's Health even if you loose. Cost is 1 Attack Point.
        >>  MEDIPACK    : Gives a boost to Health to 2 points. (Player gets 1 as default)
        >>  VIRUS       : Gives a long lasting Destructing effect. Destroys computer's Health Point at the beginning
                          of each round. VIRUS is destroyed, once a round is lost.
                          But you need to spend 2 Attack Points for deploying 1 Virus.
        >>  INSURANCE   : Gives a long lasting Health Boost effect. Rejuvenates 1 Health Point, after
                          each consecutive winning round. Insurance is lost once a round is lost.
                          But Insurance consumes 1 Attack point as its premium.
    Max Number of cards that can be simultaneously be active = 1
    The data parameter for each methods takes up all the current user data.
    data is a list containing values of format:
                (0) < player name >
                (1) < health point >
                (2) < attack point >
                (3) < score >
                (4) < active magic_cards >
                (5) < all magic cards >
                (6) < win counter >
                (7) < rounds >
                (8) < Computer Health Point >
    """

    def __init__(self):
        """
        This is the constructor for the Class MagicCard.

        """
        self.card_list = ['SHIELD', 'CANON', 'MEDIPACK', 'VIRUS', 'INSURANCE']
        self.card_index = {'SHIELD': 0, 'CANON': 1, 'MEDIPACK': 2, 'VIRUS': 3, 'INSURANCE': 4}
        self.color_code = {'SHIELD': 'yellow', 'CANON': 'red', 'MEDIPACK': 'blue', 'VIRUS': 'purple',
                           'INSURANCE': 'aqua'}
        self.io = CustomIO.CustomIO()

    def display_card_resource(self, usr_data):
        """
        This function displays the current status of Magic Cards.
        Each card has a color code.
        :return:None
        """
        index = 0
        print(fonts.font_dark("green") + fonts.bold() + "MAGIC CARDS : ", end='')
        for card in self.card_list:
            print(fonts.font_dark(self.color_code[card]) + fonts.bold() + card + fonts.default() + ': %2d' %
                  (usr_data[5][index]), end='    ', flush=stdout)
            index += 1
        print()

    def gen_mc_normal(self, usr_data):
        """
        This function generate a magic card for the player.
        Magic cards are given to player after 3 consecutive wins.
        :return: The magic card generated!
        """

        number = randint(0, 6)
        number = number if number <= 4 else number - 2
        usr_data[5][number] += 1
        usr_data[6] = 0
        print("* You Got a", self.card_list[number])
        return usr_data

    def gen_mc_force(self, usr_data):
        """
        This function generates a Magic Card when ever the user wishes
        what's the catch?
        Simple, trade two other existing magic cards. :D
        And remember, the win_counter in reset after this.

        A few important points if you are trying to understand what are these lines of if-else and
        loops used here!
            >  using a loop we are iterating all the type of Magic Cards.
            >  break the loop once 2 cards are given
            >  don't show cards with card count 0
            >  choice1 and choice2 are 'list' variables, where 0th element is the Magic Card name
                and 1st element is the number of cards.
            >  choice1 takes one type of card, and
                choice2 takes another type of card; only when number of cards in choice1 is 1.
                if there are two cards for choice1, choice2 is not utilised.
            >  using a while loop to force player to give correct input.
            >  Once a correct input is provided, we generate a magic card as per user's choice.
        :return: None
        """
        # Find if there are any cards at-all or not
        total_number_of_cards = 0
        choice1 = [-1, 0]  # [card_index, numbers_to_be_trades]
        choice2 = [-1, 0]
        for number in usr_data[5]:
            total_number_of_cards += int(number)

        # If there are atleast 2 Magic Cards, carry on...
        if total_number_of_cards >= 2:
            print("\nEnter the number of cards you want to trade:"
                  "(\n0 to skip that card, or the number of cards you want(1 or 2)\n")

            index = 0
            for number in usr_data[5]:
                # Break the loop if two cards have been chosen.
                if choice1[1] == 2 or choice1[1] + choice2[1] == 2:
                    index += 1
                    break

                # Don't show a Magic Card with count 0
                if number == 0:
                    index += 1
                    continue

                if choice1[1] == 0:
                    choice1[0] = index
                    choice1[1] = int(input(fonts.font_dark(self.color_code[self.card_list[index]]) +
                                           self.card_list[index] + fonts.default() + ': '))

                    # Force the user to give correct input only.
                    # Add Dialog
                    while choice1[1] > 2 or choice1[1] < 0:
                        if choice1[1] > 2:
                            self.io.speech_tra("How nice of you to sacrifice more than 2 cards.", 2)
                            self.io.speech_tra("But you don\'t need to be so good!", 2)
                            self.io.speech_bill("Enter Correctly")
                            choice1[1] = int(input(fonts.font_light('aqua') + '>>> ' + fonts.default()))
                        else:
                            self.io.speech_tra("Stop trying my patience!", 1)
                            self.io.speech_tra("Enter Correctly:", 2)
                            choice1[1] = int(input(fonts.font_light('red') + '>>> ' + fonts.default()))
                else:
                    choice2[0] = index
                    choice2[1] = int(input(fonts.font_dark(self.color_code[self.card_list[index]]) +
                                           self.card_list[index] + fonts.default() + ': '))
                    while choice2[1] > 1:
                        self.io.speech_tra("Please! That won\'t work.", 2)
                        self.io.speech_tra("Enter Correctly:", 2)
                        choice2[1] = int(input(fonts.font_light('red') + '>>> ' + fonts.default()))
                index += 1

            if choice1[1] + choice2[1] == 2:
                self.io.speech_bill("Are you Sure? ")
                ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
                if ch.upper() == 'Y' or ch.upper() == 'YES' or ch.upper() == 'YUP':
                    usr_data[5][choice1[0]] -= choice1[1]
                    if choice1[1] <= 1:
                        usr_data[5][choice2[0]] -= choice2[1]
                    CustomIO.CustomIO().loading()
                    print()
                    usr_data = self.choose_card(usr_data, 2)

                elif ch.upper() == 'N' or ch.upper() == 'NO' or ch.upper() == 'NOPE':
                    # add dialog
                    self.io.speech_tra("None of your cards were touched. I knew you couldn't decide...", 2)

                else:
                    # add dialog
                    self.io.speech_tra("Say only what you are asked. Taking 'No' as your answer...", 1)

            else:
                self.io.speech_tra("You know, I'm not a fool! Please stop trying cheap tricks!", 1)
                self.io.speech_tra("I'm not going to ask you to enter correctly! Next time, remember this.", 2)
        else:
            self.io.speech_tra("Duh! You don\'t have enough cards to trade", 2)
        return usr_data

    def one_time_card(self, usr_data, card_no):
        """
        This module implements the usage of One-Time-Magics-Cards.
        There are two OTMCs : Canon and Medipack.
        They are like use-and-through cards, independent of any future rounds.

        :param usr_data: the list of current game data
        :param card_no: The Magic Card number; 1: Canon, 2: Medipack
        :return: a list of updated game data
        """
        print(fonts.font_dark(self.color_code[self.card_list[card_no]]) + fonts.underline() + fonts.bold() + '* ' +
              self.card_list[card_no] + ' is being deployed *' + fonts.default())
        # Canon Card
        if card_no == 1:
            if usr_data[8] > 0:
                usr_data[8] -= 1
                usr_data[5][1] -= 1
                usr_data[6] = 0

        # Medipack
        elif card_no == 2:
            if usr_data[1] <= 9:
                usr_data[1] += 1
                usr_data[2] -= 1
                usr_data[5][2] -= 1
                usr_data[6] = 0
            else:
                self.io.speech_bill("Health already at max. No need for a Medipack!")
        return usr_data

    def runtime_card_init(self, usr_data, card_no):
        """
            This module initialises Long-Time-Magic-Cards.
            LTMCs are of 3 types: Shield, Insurance and Virus.
            These are the cards that are played at one round, but it remains active till future rounds.
            This module is called upon, when the card is played.
            :param usr_data: a list of current game data
            :param card_no: The Magic Card number; 0: Shield, 3: Virus, 4: Insurance
            :return: a list of updated game data
            """
        if usr_data[4] != -1:
            self.io.speech_bill('You have a card active : ' +
                                fonts.font_dark(self.color_code[self.card_list[usr_data[4]]]) +
                                self.card_list[usr_data[4]])
            self.io.speech_bill('Are you sure you want to proceed? (say yes(y) or No(n): ')
            ch = input(fonts.font_light('aqua') + '>>> ' + fonts.default())
            if ch.upper() == 'Y' or ch.upper() == 'YES':
                usr_data[4] = -1
            else:
                self.io.speech_tra('Cant Decide eh?', 2)
                return usr_data

        if usr_data[4] == -1:
            # Shield
            if card_no == 0:
                usr_data[4] = 0

            # Virus
            elif card_no == 3:
                if usr_data[2] <= 1:
                    self.io.speech_bill("We cant do that! We don't have enough Attack Points.")
                else:
                    usr_data[4] = card_no
                    usr_data[2] -= 2

            # Insurance
            elif card_no == 4:
                if usr_data[2] < 1:
                    self.io.speech_bill("We cant do that! We don't have enough Attack Points.")
                else:
                    usr_data[4] = card_no
                    usr_data[2] -= 1
        return usr_data

    def runtime_card_deploy(self, usr_data, card_no=None):
        """
        This module is called upon when ever an LTMCs are set to take effect.

        :param usr_data: a list of current game data
        :param card_no: The Magic Card number; 0: Shield 3: Virus, 4: Insurance
        :return: a list of updated game data
        """
        if card_no is None:
            card_no = usr_data[4]
        print(fonts.font_dark(self.color_code[self.card_list[card_no]]) + fonts.underline() + fonts.bold() + '* ' +
              self.card_list[card_no] + ' is being deployed *' + fonts.default())

        # Shield
        if card_no == 0:
            usr_data[1] += 1

        # Virus
        elif card_no == 3:
            if usr_data[8] > 0:
                usr_data -= 1

        # Insurance
        elif card_no == 4:
            if usr_data[2] < 1:
                self.io.speech_bill("We can\'t pay the Premium. We don't have enough Attack Points.")
                self.io.speech_tra("Haha, you lost your Insurance Card didn\'t you? Oh! pittyful Humans! ")
                usr_data[4] = -1
            elif usr_data[1] == 10:
                self.io.speech_bill("Yay, full life boost! Come on now, lets finish this game!", 0)
            else:
                usr_data[2] -= 1
                if usr_data[1] < 10:
                    usr_data += 1
        return usr_data

    def check_cards_if_any(self, usr_data):
        """
        Checks if Player has any Magic Card at all or not
        :param usr_data: the list of current game data
        :return: 0 is no Magic Card is present, else 1.
        """

        if [n for n in usr_data[5] if n >= 1]:
            return 1
        else:
            return 0

    def choose_card(self, usr_data, act=1):
        """
            This module lets the player choose a magic card from this collection.
            :param usr_data: the list of current game data
            :param act: if the user wants to activate 1, else 0
            :return: modified data, activated
            """
        dialog = randint(1, 2)
        if dialog == 1:
            self.io.speech_tra("Enter the card you want: (Ignore case. I can spell!)", 1)
            usr_card = input(fonts.font_light('red') + '>>> ' + fonts.default()).upper()
        else:
            self.io.speech_bill("Which card should we take?")
            usr_card = input(fonts.font_light('aqua') + '>>> ' + fonts.default()).upper()

        if usr_card in self.card_list:
            usr_data[5][self.card_index[usr_card]] += 1
            # add a dialog : Yay, we got what we needed.

            if act == 1:
                if self.card_index[usr_card] in [0, 3, 4]:
                    usr_data = self.runtime_card_init(usr_data, self.card_index[usr_card])
                else:
                    usr_data = self.one_time_card(usr_data, self.card_index[usr_card])

            else:
                self.io.speech_tra("You got your card. Enjoy as long as you can", 1)
            usr_data[6] = 0
        else:
            self.io.speech_tra("Sorry, you can't make your own Magic card!", 2)
            self.io.speech_tra("Stop fooling around....", 1)

        return usr_data
'''
# test
data = ['avik', 5, 6, 1000, 3, [0, 1, 1, 0, 2], 0, 5, 9]
mc = MagicCard()
mc.display_card_resource(data)
data = mc.gen_mc_force(data)

print()
# mc.gen_mc_normal()
mc.display_card_resource(data)
print()
mc.gen_mc_normal(data)
mc.display_card_resource(data)
'''