import os


def expand_config(path):
    with open('config.yaml') as f:
        for line in f.readlines():
            try:
                tree = line.strip().split('/')
                if len(tree[-1].split('.')) > 1:
                    new_file = open(f'{line.strip()}', 'w')
                    new_file.close()
                else:
                    os.makedirs(line.strip())
            except FileExistsError as e:
                print(e)


if __name__ == '__main__':
    config_path = os.path.join(os.getcwd(), 'config.yaml')
    expand_config(config_path)
