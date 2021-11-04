import json
import os
from Task_4 import new_fold


def fold_summary_write(folder):
    d = {k: 0 for k in ['100', '1000', '10000', '100000']}
    n_100 = n_1000 = n_10000 = n_100000 = 0
    set_list = [set() for _ in range(4)]
    for f in os.scandir(folder):
        if os.stat(f).st_size in range(101):
            set_list[0].add(f.name.split(".")[-1])
            n_100 += 1
            d['100'] = (n_100, list(set_list[0]))
        elif os.stat(f).st_size in range(101, 1001):
            set_list[1].add(f.name.split(".")[-1])
            n_1000 += 1
            d['1000'] = (n_1000, list(set_list[1]))
        elif os.stat(f).st_size in range(1001, 10001):
            set_list[2].add(f.name.split(".")[-1])
            n_10000 += 1
            d['10000'] = (n_10000, list(set_list[2]))
        else:
            set_list[3].add(f.name.split(".")[-1])
            n_100000 += 1
            d['100000'] = (n_100000, list(set_list[3]))
    with open('some_data_summary.json', 'w', encoding='utf-8') as f:
        json.dump(d, f)


if __name__ == '__main__':
    folder = 'some_data'
    new_fold(folder)
    fold_summary_write(folder)
