def show(args):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        start = 0
        stop = sum(1 for i in f)
        f.seek(0)
        if len(args) == 2:
            prog, start = args
        elif len(args) == 3:
            prog, start, stop = args
        for line in f.readlines()[int(start)-1:int(stop)]:
            print(line.strip())


if __name__ == "__main__":
    import sys

    show(sys.argv)
