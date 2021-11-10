def val_checker(cb_func):
    def my_decorator(my_func):
        def wrapper(*args, **kwargs):
            if not cb_func(*args, **kwargs):
                raise ValueError('Input positive number')
            return my_func(*args, **kwargs)
        return wrapper

    return my_decorator


@val_checker(lambda x: x > 0)
def calc_cube(n):
    return n ** 3


if __name__ == '__main__':
    print(calc_cube(5))
