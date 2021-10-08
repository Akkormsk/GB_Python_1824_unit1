def cube_str():
    return [n ** 3 for n in range(1, 1000, 2)]


def summ_dev_7(my_str):
    sum_num = 0
    for num in my_str:
        sum_i = 0
        for i in str(num):
            sum_i += int(i)
        if sum_i % 7 == 0:
            sum_num += sum_i
    return sum_num


def summ_dev_7_mod(my_str):
    sum_num = 0
    for num in my_str:
        num += 17
        sum_i = 0
        for i in str(num):
            sum_i += int(i)
        if sum_i % 7 == 0:
            sum_num += sum_i
    return sum_num


print(cube_str())
print(summ_dev_7(cube_str()))
print(summ_dev_7_mod(cube_str()))
