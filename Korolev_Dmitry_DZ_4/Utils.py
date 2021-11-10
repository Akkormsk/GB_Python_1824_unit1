from requests import get, utils
from re import sub, search
from datetime import date, datetime
import urllib.request
import xml.dom.minidom as minidom

xml_url = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(curr):
    response = get(xml_url)
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


def currency_rates_dom(curr):
    xml_content = urllib.request.urlopen(xml_url).read()
    dom = minidom.parseString(xml_content)
    dom.normalize()
    elements = dom.getElementsByTagName('Valute')
    cur_dict = {}
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data.replace(',', '.')
        cur_dict[char_code] = value
    res = cur_dict.get(curr.upper())
    print(f'Данные на дату {datetime.now().date()}')
    print(f'Курс {curr.upper()} к рублю: {res}')
    return


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_rates(input('Введите код валюты на транслите: '), url)
    currency_rates_dom(input('Введите код валюты на транслите: '), url)
