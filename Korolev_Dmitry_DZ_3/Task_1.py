dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate_adv(num):
    res = str(dictionary.get(num.lower())).capitalize() if num.istitle() else dictionary.get(num)
    return res


print(num_translate_adv('Six'))
