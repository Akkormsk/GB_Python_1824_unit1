import pickle
import os
from Task_4 import new_fold
from collections import defaultdict


def fold_summary_write(fold):
    st = (1, 101, 1001, 10001, 100001)
    d = defaultdict(list)
    for m in range(1, len(st)):
        k = sum(1 for file in os.scandir(fold) if os.stat(file).st_size in range(st[m - 1], st[m]))
        v = list(
            {file.name.split(".")[-1] for file in os.scandir(fold) if os.stat(file).st_size in range(st[m - 1], st[m])})
        d[k] = v
    st_mod = [n - 1 for n in st[1:]]
    d_res = dict(zip(st_mod, d.items()))
    # print(d_res)
    with open('some_data_summary.json', 'wb') as f:
        pickle.dump(d_res, f)


if __name__ == '__main__':
    folder = 'some_data'
    new_fold(folder)
    fold_summary_write(folder)
