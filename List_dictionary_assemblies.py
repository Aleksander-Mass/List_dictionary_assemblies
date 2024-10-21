# Задача:
# Даны несколько списков, состоящих из строк

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишите список созданный при помощи сборки состоящий из длин
# строк списка first_strings, при условии, что длина строк не менее 5 символов.

# 1. Создание списка first_result:
# Задача заключается в создании списка, содержащего длины строк из списка first_strings, при этом длина строк
# должна быть не менее 5 символов. Мы можем использовать list comprehension для этого:

first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей)
# одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# 3. В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение
# будет строка-длина строки. Значения строк будут перебираться из объединённых вместе
# списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

###   весь код решения:

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Решение:
# 1. Список с длинами строк длиной не менее 5 символов из first_strings
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список кортежей слов одинаковой длины
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# 3. Словарь, где ключ-значение - строка и её длина, если длина строки чётная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результата
print(first_result)  # => [10, 8, 8]
print(second_result) # => [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors',
                        # 'Computer'), ('Variable', 'Computer')]
print(third_result)  # => {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4,
                         # 'Computer': 8}