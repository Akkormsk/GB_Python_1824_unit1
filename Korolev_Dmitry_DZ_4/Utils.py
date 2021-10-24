from requests import get, utils
from re import sub, search
from datetime import date


def currency_rates(curr):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    text_list = content.split('<Valute')
    date_pos = search('Date', text_list[0])
    date_str = list(map(int, ((text_list[0][date_pos.span()[1] + 2:date_pos.span()[1] + 12]).split('.'))))
    date_date = date(day=date_str[0], month=date_str[1], year=date_str[2])
    val_list = []
    val_num = []
    for cur in text_list[1:]:
        cur_list = cur.split('><')
        val_num.append(cur_list[2][9:-10])
        val_num.append(sub(',', '.', cur_list[5][6:-7]))
        val_list.append(val_num)
        val_num = []
    val_dict = {k: n for [k, n] in val_list}
    res = val_dict.get(curr.upper())
    if res.isdecimal:
        float(res)
        print(f'Данные на дату {date_date}')
        print(f'Курс {curr.upper()} к рублю: {res}')
        return

if __name__ == '__main__':
    currency_rates(input('(*) Введите код валюты на транслите: '))