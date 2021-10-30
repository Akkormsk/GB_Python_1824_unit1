def upd(args):
    num_i, new_num = args
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        lines = []
        i = 0
        for line in f:
            i += 1
            if i == int(num_i):
                lines.append(new_num)
                break
            else:
                lines.append(line)
        f.seek(0)
        f.writelines(lines)


if __name__ == "__main__":
    import sys
    upd(sys.argv[1:])
