import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(q, fl):
    """
    :param q: количество шуток
    :param fl: 1 - если допущены повторения, 0 - если не допущены
    :return: список шуток
    """
    joke_list = []
    for i in range(q):
        joke = []
        for group in nouns, adverbs, adjectives:
            index = random.randrange(0, len(group))
            new_joke = group[index] if fl else group.pop(index)
            joke.append(new_joke)
        print(nouns, adverbs, adjectives)
        joke = ' '.join(joke)
        joke_list.append(str(joke))
    return joke_list


print(get_jokes(3, fl=0))
