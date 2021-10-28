from sys import getsizeof as gso
from time import perf_counter as pc


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
result = []

# в лоб, нагрузка на ресурсы n*n шагов
start = pc()
for n in src:
    if src.count(n) < 2:
        result.append(n)
print(result)
print(pc()-start)

# нагрузка на ресурсы n шагов
start = pc()
result_2 = []
tmp = set()
for num in src:
    if num not in tmp:
        tmp.add(num)
        result_2.append(num)
    else:
        tmp.discard(num)
print(result)
print(pc()-start)
