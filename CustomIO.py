from time import sleep
from random import randint
from sys import stdout, stdin
from select import select
import fonts


class CustomIO:
    """
        This Class is used for a customised input and output functions.

    """

    def __init__(self):
        pass

    def typel(self, text='', delay=-1.0):
        """
            This function prints a given text with a delay between each letters
            making it appear like it is being typed.
            The typing speed can be adjusted by changing the 'delay' value.
            :param text : The text to be printed
            :param delay: The printing interval between to letters; if user does not provide any,
                      an random delay is generated for each letter
            :return     : None (at return no New-Line is created!)
        """
        for letter in text:
            if delay == -1:
                delay = (1 / randint(2, 5) - 0.1) or 0.1
            print(letter, end='', flush=stdout)
            sleep(delay)

    def timer_input(self, wait=5):
        """
            This functions waits for a user input for a given period of time.
            :param wait: the waiting time required for input; default is 5 seconds
            :return    : the value entered (if any)
            """
        if select([stdin], [], [], wait)[0]:
            return stdin.readline().strip()

    def loading(self):
        self.typel('* LOADING', 0.3)
        sleep(1)
        self.typel('...', 0.3)
        print(' *')

    def print_spaces(self, length):
        """
            Prints spaces for a given length.
            Note : No new-line is created.
            :param length: The length of spaces needed.
            :return: None
        """
        for x in range(0, length):
            print(' ', end='', flush=stdout)

    def speech_bill(self, text, secure=1):
        """
            This method prints the speechs of Bill Zuckerberg.
            :param secure: Whether he speaks by secure channel yo you(1, default) or directly to TRA (0)
            :param text: His Speech.
            :return: None
        """
        if secure:
            print(fonts.font_light('aqua') + '[Bill: ', end='')
            self.typel(' ' + text + ']')
            print(fonts.default())
        elif secure == 0:
            print(fonts.font_dark('aqua') + fonts.bold() + 'Bill : ', end='')
            self.typel(' ' + text)
            print(fonts.default())

    def speech_tra(self, text, face=1):
        """
                This method prints the speech of TRA
                :param face: 1: T-Rex personality, 2: Angel Personality
                :param text: His Speech.
                :return: None
                """
        if face == 1:
            print(fonts.font_light('red') + fonts.bold() + 'T-REX: ', end='')
            self.typel(' ' + text, 0.1)
            print(fonts.default())
        if face == 2:
            print(fonts.font_light('yellow') + fonts.bold() + 'ANGEL: ', end='')
            self.typel(' ' + text, 0.1)
            print(fonts.default())

    def zebra_bar(self, color1, color2, lenght):

        for x in range(0, int(lenght/10)):
            print(fonts.bar_dark(color1) + '     ', end='' + fonts.default())
            print(fonts.bar_dark(color2) + '     ', end='' + fonts.default())
        print()
        #print(fonts.bar_light('grey'), ' ' + fonts.default(), end='')
        for x in range(0, int(lenght/10)):
            print(fonts.bar_dark(color2) + '     ', end='' + fonts.default())
            print(fonts.bar_dark(color1) + '     ', end='' + fonts.default())