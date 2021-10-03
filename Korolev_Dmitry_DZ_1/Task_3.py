for i in range(1, 101):
    if i in range(11, 15):
        end = 'ов'
    else:
        last_n = int(str(i)[-1])
        if last_n == 1:
            end = ''
        elif last_n in range(2, 5):
            end = 'а'
        else:
            end = 'ов'

    print(f'{i} процент{end}')