def type_logger(func):
    def wrapper(*args):
        func(*args)
        print(f'Результат функции {func.__name__}: {func(*args)},  тип значения: {type(func(*args))}')
        for n in args:
            print(f'Аргумент {n}: тип {type(n)}')
        print()

    return wrapper


def type_logger_masked(func):
    def wrapper(*args, **kwargs):
        log_d = {}
        for arg in args:
            log_d[arg] = type(arg)
        for kwarg in kwargs.values():
            log_d[kwarg] = type(kwarg)
        func(*args, **kwargs)
        # print(log_d)

    return wrapper


@type_logger
def calc_cube(n):
    return n ** 3


@type_logger
def f_sum(n, m=5):
    return n + m


@type_logger_masked
def f_mult(n, m, l):
    print(n * m * l)


if __name__ == '__main__':
    calc_cube(3)
    f_sum(4, 5)
    f_mult(4, l=5, m=6)
