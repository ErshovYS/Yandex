# -*- coding: utf-8 -*-
'''
7 раков за 1 рубль
Покупатель покупает по одному раку в день.
Долг не должен превышать половину копейки.
Нужно написать алгоритм который мог бы использовать продавец, 
чтобы на входе иметь номер дня, а на выходе сумму, на которую нужно выставить счет.
Счет который получает клиент должен быть с точностью до копейки.

Добавить возможность изменения цены и количества раков
'''

def func(count, cost, num_day):
    if num_day > 1:
        my_mod = 0
        step = (cost/count * 100) % 1
        b = []
        for i in range(num_day-1):
            my_mod += step
            if my_mod > 0.5:
                my_mod = my_mod - 1
            if round(my_mod, 4) in b:
                break
            b.append(round(my_mod, 4))
        
        my_mod2 = b[(num_day-2) % (len(b))]/100
    else:
        my_mod2 = 0
    return "{0:.2f}".format(cost/count + my_mod2)

#for i in range(1, 100):
#    print(func(7, 1, i))
    
print(func(7, 1, 10000000005))