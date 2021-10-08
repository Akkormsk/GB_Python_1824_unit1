def secs_to_str(dur):
    min = 60
    hour = min*60
    day = hour*24
    if dur in range(1, min):
        return f'{dur} сек'
    elif dur in range(min, hour):
        return f'{dur//min} мин {dur%min} сек'
    elif dur in range(hour, day):
        return f'{dur//hour} час {(dur%hour)//min} мин {((dur%hour)%min)} сек'
    elif dur >= day:
        return f'{dur//day} дн {(dur%day)//hour} час {((dur%day)%hour)//min} мин {((dur%day)%hour)%min} сек'

duration = 400153
print(secs_to_str(duration))