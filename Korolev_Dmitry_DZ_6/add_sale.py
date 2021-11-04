def add(args):
    prog, sale = args
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(sale + '\n')


if __name__ == "__main__":
    import sys

    add(sys.argv)
