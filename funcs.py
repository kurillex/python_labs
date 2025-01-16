import json


def response_analysis(response):
    if response.status_code == 200:
        print('Everything is OK!')
        #write_json(response.json())
    else:
        print(response)


def translate_text(text):
    translator = Translator(to_lang="ru")
    translation = translator.translate(text)
    return translation


def write_json(data):
    with open(input('Ссылка на сохранение json: \n'), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

