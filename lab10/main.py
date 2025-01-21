from voice import currency_voice_assistant


def main():
    funcs = {
        '1': currency_voice_assistant,
        '0': exit
    }
    start = input('Выберите программу:\n'
                  '1: Запустить голосового помощника\n'
                  '0: Выход\n')
    return funcs[start]()


if __name__ == "__main__":
    main()
