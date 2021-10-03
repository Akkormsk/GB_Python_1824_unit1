def secs_to_str(dur):
    secs = int(dur)
    mins = int(dur/60)
    hours = int(dur/60/60)
    days = int(dur/60/60/24)

    if days:
        d = dur // (60*60*24)
        h = (dur - d * (60*60*24))//(60*60)
        m = (dur - d * (60*60*24) - h * (60*60))//60
        s = dur - d * (60*60*24) - h * (60*60) - m * 60
        return f'{d} дн {h} час {m} мин {s} сек'
    elif hours:
        h = dur // (60*60)
        m = (dur - h * (60*60))//60
        s = dur - h * (60*60) - m * 60
        return f'{h} час {m} мин {s} сек'
    elif mins:
        m = dur // 60
        s = dur - m * 60
        return f'{m} мин {s} сек'
    elif secs:
        return f'{secs} сек'

# duration = 400153
# print(secs_to_str(duration))