from time import sleep
import fonts
import CustomIO


class Attribute:

    def __init__(self, index):
        self.index = index


    def value_bar(self, usr_data):

        if self.index == 1:
            print(fonts.font_dark('red') + fonts.bold() + 'HEALTH      :', end='' + fonts.default())
        elif self.index == 2:
            print(fonts.font_dark('yellow') + fonts.bold() + 'ATTACK      :', end='' + fonts.default())
        elif self.index == 8:
            print(fonts.font_light('blue') + fonts.bold() + 'COMPUTER HEALTH  :', end='' + fonts.default())
        if int(usr_data[self.index]) < 4:
            color1 = fonts.bar_dark('red')
            color2 = fonts.font_dark('red')
        elif 4 <= int(usr_data[self.index]) <= 7:
            color1 = fonts.bar_dark('blue')
            color2 = fonts.font_dark('blue')
        elif int(usr_data[self.index]) > 7:
            color1 = fonts.bar_dark('green')
            color2 = fonts.font_dark('green')
        else:
            color1 = fonts.default()
            color2 = fonts.default()

        print(color2, '( %d ) ' % int(usr_data[self.index]), end='')
        for x in range(0, int(usr_data[self.index])):
            print(color1, end='')
            print('=', end='')
        print(fonts.default(), end='')

        for x in range(int(usr_data[self.index]), 10):

            print(fonts.bold() + '-', end='')
        print(fonts.default(), end='')

'''
# test
health = Attribute()
health.value_bar()
'''
