from currencies import convert_currency_request, check_the_currency
from funcs import get_info_from_response, get_api, recognize_text


def currency_voice_assistant():
    text = recognize_text()
    if text == 'Fail':
        print('Ошибка!!!')
        return 1

    response = get_api()

    data_cur = get_info_from_response(response)

    currency = convert_currency_request(text)

    check_the_currency(currency, data_cur)

