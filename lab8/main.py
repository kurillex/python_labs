from part1_cut_400x400 import cut_the_square
from video_point import find_the_point


def main():
    funcs = {
        '1': cut_the_square,
        '2': find_the_point,
        '0': exit
    }
    start = input('Выберите программу:\n'
                  '1: Вырезать область 400х400\n'
                  '2: Отслеживание метки на видео\n'
                  '0: Выход\n')
    return funcs[start]()


if __name__ == "__main__":
    main()