task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in task_list:
    i_list = i.split(' ')
    print(f'Привет, {i_list[-1].capitalize()}!')