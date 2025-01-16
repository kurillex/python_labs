from part1_api import *
from part2_json import *
from funcs import *


def main():
    funcs = {
        '1': get_weather_api,
        '2': get_steam_api,
        '0': exit
    }
    start = input('Выберите программу:\n'
                  '1: Api погоды в СПб\n'
                  '2: Api steam\n'
                  '0: Выход\n')
    return funcs[start]()


if __name__ == "__main__":
    main()