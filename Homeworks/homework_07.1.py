"""here is a docstring."""
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити або доповнити.
"""
print('\n-----Task 1-----')


def multiplication_table(number):
    """multiplication_table."""
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))
        # Increment the appropriate variable

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print('\n-----Task 2-----')


def add_numbers(a, b):
    """add_numbers."""
    return a + b


result = add_numbers(3, 5)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('\n-----Task 3-----')


def calculate_average(numbers):
    """calculate_average."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


numbers = [5, 4, 76, 345, 756, 44]
average = calculate_average(numbers)
print(average)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print('\n-----Task 4-----')


def reverse_string(s1):
    """reverse_string."""
    return s1[::-1]


result = reverse_string('Python course')
print(result)

# task 5
"""  Написати функцію, яка приймає список слів
та повертає найдовше слово у списку.
"""
print('\n-----Task 5-----')


def find_longest_word(words_list):
    """find_longest_word."""
    if not words_list:
        return None
    return max(words_list, key=len)


words = ['bmw', 'audi', 'toyota', 'subaru',
         'mercedes', 'volkswagen', 'renault']
longest_word = find_longest_word(words)
print(f'The longest word is: {longest_word}.')

# task 6
"""  Написати функцію, яка приймає два рядки
та повертає індекс першого входження другого рядка у перший рядок,
якщо другий рядок є підрядком першого рядка,
та -1, якщо другий рядок не є підрядком першого рядка."""
print('\n-----Task 6-----')


def find_substring(str1, str2):
    """find_substring."""
    index = str1.find(str2)
    return index


str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7


str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print('\n-----Task 7-----')
"""Порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""


def sum_of_even_numbers(lst):
    """приймає список, знаходить парні числа та повертає їхню суму."""
    return sum(num for num in lst if num % 2 == 0)


lst1 = list(range(1, 51))
even_sum = sum_of_even_numbers(lst1)
print(f'The sum of all the even numbers'
      f'in the range from 1 to 50 is {even_sum}.')

print('\n-----Task 8-----')
# Існує деяка інформація про автомобілі
# з кольором, роком випуску, об'ємом двигуна, типом автомобіля та ціною.
# Маємо критерії пошуку у вигляді кортежу (рік ≥, об'єм двигуна ≥, ціна ≤).
# Напишіть код, який допоможе нам отримати
# автомобілі, які відповідають критеріям пошуку.
# Автомобілі повинні бути відсортовані за зростанням ціни.
# Ми повинні вивести до п'яти (5) перших знайдених елементів

car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
}

search_criteria = (2017, 1.6, 36000)


def filter_cars(car_data, search_criteria):
    """To filter car_data by search_criteria."""
    year_min, engine_min, price_max = search_criteria
    filtered_cars = [
        (car, details)
        for car, details in car_data.items()
        if details[1] >= year_min and details[2] >= engine_min and details[4] <= price_max
    ]
    filtered_cars.sort(key=lambda x: x[1][4])
    return filtered_cars[:5]


search_criteria = (2017, 1.6, 36000)
matching_cars = filter_cars(car_data, search_criteria)

print(*matching_cars, sep='\n')

print('\n-----Task 9-----')
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]


def modify_people_records(records, new_record):
    """To modify list 'people_records'."""
    records.insert(0, new_record)

    records[1], records[5] = records[5], records[1]
    print('Modified list with swapped elements (1 <-> 5):')
    for record in records:
        print(record)

    # 3. Перевіряємо, чи всі люди з індексами 6, 10, 13 мають вік >= 30
    age_condition = all(records[i][2] >= 30 for i in [6, 10, 13])
    print('All people at indexes 6, 10, 13 have age >= 30:', age_condition)


new_record = ('New', 'Person', 30, 'Data Scientist', 'San Francisco')

modify_people_records(people_records, new_record)

print('\n-----Task 10-----')
"""
Дані у строці adventures_of_tom_sawer розбиті випадковим
чином, через помилку. Треба
1. замінити кінець абзацу на пробіл .replace("\n", " ")
2. Замініть .... на пробіл
3. Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked .... and sweated in the sun,
the retired artist sat on a barrel in the .... shade
close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded
the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it
with—and so on, and so on,
hour after hour. And when the middle of the afternoon came,
from being a poor poverty, stricken boy
in the .... morning, Tom was literally
rolling in wealth."""


def replace_newline(text):
    """Замінює кінець абзацу на пробіл."""
    return text.replace('\n', ' ')


def replace_dots(text):
    """Замінює '....' на пробіл."""
    return text.replace('....', ' ')


def normalize_spaces(text):
    """Замінює множинні пробіли на один пробіл."""
    return ' '.join(text.split())


text_processed = replace_newline(adventures_of_tom_sawer)
text_processed = replace_dots(text_processed)
text_processed = normalize_spaces(text_processed)

print(text_processed)
