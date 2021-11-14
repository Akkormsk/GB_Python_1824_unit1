import os


# def expand_config(path):
#     with open('config.yaml') as f:
#         for line in f.readlines():
#             try:
#                 tree = line.strip().split('/')
#                 if len(tree[-1].split('.')) > 1:
#                     new_file = open(f'{line.strip()}', 'w')
#                     new_file.close()
#                 else:
#                     os.makedirs(line.strip())
#             except FileExistsError as e:
#                 print(e)

def expand_config(path):
    with open('config_2.yaml', encoding='utf-8') as f:
        args = ['', '', '', '', '', '', '']
        for line in f.readlines():
            if line.startswith(' '):
                tab_num = int(line.count(' ')/2)
                args = args[:tab_num - 1]
                args.append(line.strip())
            else:
                base_path = line.strip()
            try:
                file_path = os.path.join(base_path, *args)
                if '.' in str(args[-1]):
                    new_file = open(f'{file_path}', 'w')
                    new_file.close()
                else:
                    os.makedirs(file_path)
            except FileExistsError as e:
                print(e)


if __name__ == '__main__':
    config_path = os.path.join(os.getcwd(), 'config_2.yaml')
    expand_config(config_path)
