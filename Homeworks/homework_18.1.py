"""
ДЗ 18.1. Кожному iтератору i генератору по декоратору.

Генератори:
Напишіть генератор, якийповертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки,
які виникають в ході виконання функції.
"""


def even_numbers(n):
    """Docstring."""
    for i in range(0, n + 1, 2):
        yield i


# Приклад використання
for num in even_numbers(10):
    print(num)  # Виведе: 0, 2, 4, 6, 8, 10


def fibonacci(n):
    """Docstring."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# Приклад використання
for fib in fibonacci(20):
    print(fib)  # Виведе: 0, 1, 1, 2, 3, 5, 8, 13


class ReverseIterator:
    """Docstring."""

    def __init__(self, lst):
        """Docstring."""
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        """Docstring."""
        return self

    def __next__(self):
        """Docstring."""
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


# Приклад використання
rev_iter = ReverseIterator([1, 2, 3, 4, 5])
for item in rev_iter:
    print(item)  # Виведе: 5, 4, 3, 2, 1


class EvenNumbersIterator:
    """Docstring."""

    def __init__(self, n):
        """Docstring."""
        self.n = n
        self.current = 0

    def __iter__(self):
        """Docstring."""
        return self

    def __next__(self):
        """Docstring."""
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


# Приклад використання
even_iter = EvenNumbersIterator(10)
for num in even_iter:
    print(num)  # Виведе: 0, 2, 4, 6, 8, 10


def log_arguments_and_results(func):
    """Docstring."""
    def wrapper(*args, **kwargs):
        print(f'Arguments: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result
    return wrapper


@log_arguments_and_results
def add(a, b):
    """Docstring."""
    return a + b


# Приклад використання
add(3, 5)


def handle_exceptions(func):
    """Docstring."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Exeption: {e}')
    return wrapper


@handle_exceptions
def divide(a, b):
    """Docstring."""
    return a / b


# Приклад використання
divide(10, 2)  # Виведе: 5.0
divide(10, 0)  # Виведе: Виняток: division by zero
