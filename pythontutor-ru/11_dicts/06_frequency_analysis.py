"""
Дан текст: в первой строке записано количество строк в тексте, а затем сами строки.
Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.

Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче.
"""

words = {}
for _ in range(int(input())):
    for word in input().split():
        words[word] = words.get(word, 0) + 1

sorted_words = sorted(words.items(), key=lambda item: (-item[1], item[0]))

for item in sorted_words:
    print(item[0])

"""
Словарь содержит пары в формате ('is', 3), и мы применяем к нему функцию sorted, 
с ключом 'lambda item: (-item[1], item[0])'. 
-item[1] позволяет сортировать числа, минус позволяет делать это в порядке убывания, 
а item[0] позволяет сортировать пары с одинаковыми числами по алфавиту
"""

"""
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
"""
