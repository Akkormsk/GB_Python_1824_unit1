def val_checker(cb_func):
    def my_decorator(my_func):
        def wrapper(*args, **kwargs):
            if not cb_func(*args, **kwargs):
                raise ValueError('Ошибка ввода. Введите положительное число')
            return my_func(*args, **kwargs)
        return wrapper

    return my_decorator


@val_checker(lambda x: x > 0)
def calc_cube(n):
    return n ** 3


if __name__ == '__main__':
    import sys

    try:
        print(calc_cube(int(sys.argv[1])))
    except (ValueError, SyntaxError) as e:
        print(e)
        print(f'Повторите ввод')
