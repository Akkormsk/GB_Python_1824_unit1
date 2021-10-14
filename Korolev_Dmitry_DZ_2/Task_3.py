import re
task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
n=0
for i in enumerate(task_list[:]):
    obj = re.search('\d+', i[1])
    if obj:
        if len(obj.group()) == 1:
            num_list = list(task_list[i[0]+n])
            num_list.insert(-1, '0')
            task_list[i[0]+n] = ''.join(num_list)
            task_list[i[0] + n] = f'"{task_list[i[0]+n]}"'
        # task_list.insert(i[0]+n, '"')
        # task_list.insert(i[0]+2+n, '"')
        # n = n+2

print(' '.join(task_list))
