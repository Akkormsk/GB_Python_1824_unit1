import os
import random
import shutil


def new_fold(folder):
    """
    создание 100 файлов с рандомным контентом не более 100000 байт
    """
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    formats = ['txt', 'png', 'css', 'xml', 'py', 'html', 'jpg']
    for _ in range(10 ** 2):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 250))
        with open(os.path.join(folder, f'{f_name}.{random.choice(formats)}'), 'ab') as f:
            for _ in range(random.randrange(400)):
                f.write(f_content)
    return


def fold_summary(folder):
    d = {k: 0 for k in ['100', '1000', '10000', '100000']}
    mem = []
    for f in os.scandir(folder):
        if os.stat(f).st_size in range(101):
            d['100'] += 1
        elif os.stat(f).st_size in range(101, 1001):
            d['1000'] += 1
        elif os.stat(f).st_size in range(1001, 10001):
            d['10000'] += 1
        else:
            d['100000'] += 1
    return d


if __name__ == '__main__':
    folder = 'some_data'
    new_fold(folder)
    print(fold_summary(folder))
