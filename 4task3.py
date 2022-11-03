lst_1 = list(input('Введите набор чисел: ').split())
lst_2 = list(input('Введите второй набор чисел: ').split())
lst_3 = lst_1 + lst_2
print('Количество различных чисел: ',len(set(lst_3)))