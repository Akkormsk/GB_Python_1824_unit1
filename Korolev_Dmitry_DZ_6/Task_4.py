import json
from sys import exit

names_2 = []
names_3 = []
hobs = []
my_list = ['Имена', 'Фамилии', 'Отчества', 'Увлечения']
list_list = [[],[],[]]
with open('users.csv', 'r', encoding='utf-8') as f_1:
    with open('hobby.csv', 'r', encoding='utf-8') as f_2:
        if sum(1 for i in f_2) > sum(1 for j in f_1):
            exit(1)
        f_1.seek(0)
        f_2.seek(0)
        for line in f_1:
            name = line.split(',')
            list_list[0].append(name[1])
            list_list[1].append(name[0])
            list_list[2].append(name[2].strip())
        for line in f_2:
            hob = map(lambda s: s.strip(), line.split(','))
            hobs.extend(hob)
        list_list.append(hobs)
        list_list = map(tuple, list_list)
        res_dict = {k: v for k, v in zip(my_list, list_list)}
with open('dict_file_4.txt', 'w', encoding='utf-8') as f_3:
    json.dump(res_dict, f_3)

with open('dict_file_4.txt', 'r', encoding='utf-8') as f_3:
    dict_test = json.load(f_3)
    print(dict_test)
