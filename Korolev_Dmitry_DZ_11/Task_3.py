class NotDigit(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    try:
        inp = input('Введетие число для добавления в список:')
        if inp == 'stop':
            break
        elif not inp.isdigit():
            raise NotDigit('Разрешенно вводить только числа, повторите ввод:')
    except NotDigit as e:
        print(e)
    else:
        my_list.append(inp)

print('Полученный список: ')
print(my_list)

