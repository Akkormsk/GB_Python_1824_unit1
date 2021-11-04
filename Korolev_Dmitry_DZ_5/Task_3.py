from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Василий', 'Николай', 'Евлампий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen(list_t, list_k):
    if len(list_t) < len(list_k):
        list_k = list_k[:len(list_t)]
    for (t, k) in zip_longest(list_t, list_k):
        yield (t, k)


tk = my_gen(tutors, klasses)
# доказательство генератора
print(tk)
pass
