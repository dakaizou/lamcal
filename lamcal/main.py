from lamcal.bool import *
from lamcal import util


if __name__ == '__main__':
    print(util.translate_bool(
        l_or(l_true)(l_false)
    ))