# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# ​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

from random import randint

listnum = []
for i in range(randint(3, 10)): 
    listnum.append(randint(0, 20))

print(f'Сгенерированный список: {listnum}')

uniclist = list(filter((lambda i: listnum.count(i) == 1), listnum))

print(f'Список уникальных элементов: {uniclist}')