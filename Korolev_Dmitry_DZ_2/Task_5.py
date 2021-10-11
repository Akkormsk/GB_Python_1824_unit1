import random
price_list = []
for i in range(20):
    price_list.append(round(random.random() * 100, 2))
for price in price_list:
    rub = int(price//1)
    kop = str(round(price%1*100))
    if len(kop) == 1:
        kop = '0' + kop
    print(f'{rub} руб {kop} коп')
print(id(price_list), price_list)
price_list.sort()
print(id(price_list), price_list)
new_list = list(reversed(price_list))
print(id(new_list), new_list)
print([new_list[i] for i in range(5)])