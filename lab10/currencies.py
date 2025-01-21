currencies_list = {
        'австралийский доллар': 'AUD',
        'азербайджанский манат': 'AZN',
        'фунт стерлингов': 'GBP',
        'армянский драм': 'AMD',
        'белорусский рубль': 'BYN',
        'болгарский лев': 'BGN',
        'бразильский реал': 'BRL',
        'венгерский форинт': 'HUF',
        'вьетнамский донг': 'VND',
        'гонконгский доллар': 'HKD',
        'грузинский лари': 'GEL',
        'датская крона': 'DKK',
        'дирхам ОАЭ': 'AED',
        'американский доллар': 'USD',
        'евро': 'EUR',
        'египетский фунт': 'EGP',
        'индийская рупия': 'INR',
        'индонезийская рупия': 'IDR',
        'казахстанский тенге': 'KZT',
        'канадский доллар': 'CAD',
        'катарский риал': 'QAR',
        'киргизский сом': 'KGS',
        'китайский юань': 'CNY',
        'молдавский лей': 'MDL',
        'новозеландский доллар': 'NZD',
        'норвежская крона': 'NOK',
        'польский злотый': 'PLN',
        'румынский лей': 'RON',
        'специальные права заимствования': 'XDR',
        'сингапурский доллар': 'SGD',
        'таджикский сомони': 'TJS',
        'таиландский бат': 'THB',
        'турецкая лира': 'TRY',
        'туркменский манат': 'TMT',
        'узбекский сум': 'UZS',
        'украинская гривна': 'UAH',
        'чешская крона': 'CZK',
        'шведская крона': 'SEK',
        'швейцарский франк': 'CHF',
        'сербский динар': 'RSD',
        'южноафриканский рэнд': 'ZAR',
        'южнокорейская вона': 'KRW',
        'японская иена': 'JPY'
    }


def convert_currency_request(text):
    text = text.lower()
    for item in currencies_list:
        if text in item:
            return currencies_list[item]
    return 'Fail'


def print_currencies():
    currency_names = list(currencies_list.keys())
    for i in range(0, len(currency_names), 5):
        print(" | ".join(currency_names[i:i + 5]))


def check_the_currency(currency, data_cur):
    if currency == 'Fail':
        print('Такой валюты нет...')
        exit()
    value = round(1 / float(data_cur["rates"][currency]), 2)
    date = data_cur["date"]
    currency_name = next((name for name, code in currencies_list.items() if code == currency), '???')
    print(f'На момент {date}\n1 {currency}({currency_name}) = {value} RUB(рубль)')
