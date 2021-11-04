max_n = 15


def odd_to_n_ye(max_n):
    for n in range(1, max_n + 1, 2):
        yield n


a = odd_to_n_ye(max_n)
b = (n for n in range(1, max_n + 1, 2))
pass
