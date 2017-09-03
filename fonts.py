def font_dark(color):
    code = {'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
            'purple': '\033[95m', 'aqua': '\033[36m', 'grey': '\033[37m'}
    return code[color]


def font_light(color):
    code = {'black': '\033[90m', 'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m', 'blue': '\033[94m',
            'purple': '\033[95m', 'aqua': '\033[96m', 'white': '\033[97m'}
    return code[color]


def bar_dark(color):
    code = {'grey': '\033[40m', 'red': '\033[41m', 'green': '\033[42m', 'yellow': '\033[43m', 'blue': '\033[44m',
            'purple': '\033[45m', 'aqua': '\033[46m', 'white': '\033[47m', 'black': '\033[48m'}
    return code[color]


def bar_light(color):
    code = {'grey': '\033[100m', 'red': '\033[101m', 'green': '\033[102m', 'yellow': '\033[103m', 'blue': '\033[104m',
            'purple': '\033[105m', 'aqua': '\033[106m', 'white': '\033[107m'}
    return code[color]


def bold():
    code = '\033[1m'
    return code


def underline():
    code = '\033[4m'
    return code


def default():
    code = "\033[0;00m"
    return code
