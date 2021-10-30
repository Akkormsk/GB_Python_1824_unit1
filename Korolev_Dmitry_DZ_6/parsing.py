import json
from sys import exit
import os


def parsing(args):
    program, names_p, hobs_p, res_p = args
    names_p = os.path.join(os.getcwd(), names_p)
    hobs_p = os.path.join(os.getcwd(), hobs_p)
    res_p = os.path.join(os.getcwd(), res_p)
    hobs = []
    my_list = ['Имена', 'Фамилии', 'Отчества', 'Увлечения']
    list_list = [[], [], []]
    with open(names_p, 'r', encoding='utf-8') as f_1:
        with open(hobs_p, 'r', encoding='utf-8') as f_2:
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
            res_dict = {k: v for k, v in zip(my_list, list_list)}

    with open(res_p, 'w', encoding='utf-8') as f_3:
        json.dump(res_dict, f_3)


if __name__ == '__main__':
    with open('dict_file_5.txt', 'r', encoding='utf-8') as f_3:
        dict_test = json.load(f_3)
        print(dict_test)
