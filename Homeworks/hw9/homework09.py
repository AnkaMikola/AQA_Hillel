"""
Homework 9.1.

Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework09.py
На оцінку впливає як якість тестів, так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

"""
Task 1.

Написати функцію, яка обчислює суму двох чисел.
"""
print('\n-----Task 1-----')


def add_numbers(a, b):
    """add_numbers."""
    return a + b


result = add_numbers(3, 5)
print(result)

"""
Task 2.

Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('\n-----Task 2-----')


def calculate_average(numbers):
    """calculate_average."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


numbers = [5, 4, 76, 345, 756, 44]
average = calculate_average(numbers)
print(average)

"""
Task 3.

Написати функцію, яка приймає рядок та повертає його
у зворотному порядку.
"""
print('\n-----Task 3-----')


def reverse_string(s1):
    """reverse_string."""
    return s1[::-1]


result = reverse_string('Python course')
print(result)

"""
Task 4.

Написати функцію, яка приймає список слів
та повертає найдовше слово у списку.
"""
print('\n-----Task 4-----')


def find_longest_word(words_list):
    """find_longest_word."""
    if not words_list:
        return None
    return max(words_list, key=len)


words = ['bmw', 'audi', 'toyota', 'subaru',
         'mercedes', 'volkswagen', 'renault']
longest_word = find_longest_word(words)
print(f'The longest word is: {longest_word}.')

"""
Task 5.

Написати функцію, яка приймає два рядки та повертає
індекс першого входження другого рядка у перший рядок,
якщо другий рядок є підрядком першого рядка,
та -1, якщо другий рядок не є підрядком першого рядка.
"""
print('\n-----Task 5-----')


def find_substring(str1, str2):
    """find_substring."""
    return str1.find(str2)


str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7


str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1
