def cube_str():
    return [n**3 for n in range(1, 1000, 2)]

def summ_dev_7(my_str):
    summ = 0
    for num in my_str:
        num_summ = sum([int(x) for x in str(num)])
        term = num_summ if num_summ % 7 == 0 else 0
        summ += term
    return summ

def str_plus(my_str):
    for i, num in enumerate(my_str):
        num += 17
        my_str[i] = num
    return my_str

# print(cube_str())
# print(summ_dev_7(cube_str()))
# print(summ_dev_7(str_plus(cube_str())))

