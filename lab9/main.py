from fsite import create_app


def main():
    switch = {'1': create_app, '0': exit}
    num = input('1: Flask\n'
                '0: Выход\n')

    switch.get(num)()


if __name__ == '__main__':
    main()
