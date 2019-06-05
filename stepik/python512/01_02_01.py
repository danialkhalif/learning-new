"""
[STEPIK]
Python: основы и применение https://stepik.org/512
01_02_01 Модель данных: объекты
"""

"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. 
Выведите количество различных объектов в этом списке.

Формат ожидаемой программы:

ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)

Примечание:
Количеством различных объектов называется максимальный размер множества объектов, в котором любые два объекта являются различными.

Рассмотрим пример:
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным

Тогда все различные объекты являют собой множество {1, 2, 3}﻿. Таким образом, количество различных объектов равно трём.
"""

objects = [
    1,
    2,
    3,
    2,
    3,
    [1, 'abc'],
    'abc'
    'a',
    'b',
    'c',
    {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 'abc',
    },
    (0, 1),
    (True, False),
    (False, True),
    False,
    'abc',
    'c',
    True,
    False,
    (False, True),
    [1, 'abc'],
    ['abc', 'cbc'],
    {1, 2, 3},
    [0, 1, 2],
    (0, 1),
]

_objects = [id(obj) for obj in objects]

print(len(set(_objects)))
