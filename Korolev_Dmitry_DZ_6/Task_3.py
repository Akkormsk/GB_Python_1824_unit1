import json
from itertools import zip_longest
from sys import exit

with open('users.csv', 'r', encoding='utf-8') as f_1:
    with open('hobby.csv', 'r', encoding='utf-8') as f_2:
        if sum(1 for i in f_2) > sum(1 for j in f_1):
            exit(1)
        f_1.seek(0)
        f_2.seek(0)
        names = map(lambda s: s.strip(), f_1.readlines())
        hobs = map(lambda s: s.strip(), f_2.readlines())
        res_dict = {k: v for k, v in zip_longest(names, hobs)}
with open('dict_file.txt', 'w', encoding='utf-8') as f_3:
    json.dump(res_dict, f_3)

with open('dict_file.txt', 'r', encoding='utf-8') as f_3:
    dict_test = json.load(f_3)
    print(dict_test)
