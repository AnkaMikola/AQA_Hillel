"""here is a docstring."""
alice_in_wonderland = (""""Would you tell me, please, which way"""
                       '''I ought to go from here?"'''
                       '\n"That depends a good deal on where you want'''
                       """to get to," said the Cat."""
                       """\n"I don't much care where —— " said Alice.\n"""
                       """"Then it doesn't matter which way """
                       '''you go," said the Cat.\n"'''
                       ''' —— so long as I get somewhere,"'''
                       """ Alice added as an explanation.\n"""
                       """"Oh, you're sure to do that," said the """
                       '''Cat, "if you only walk long enough."''')
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так,
# щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
sum = black_sea + azov_sea
print(sum)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_goods = 375291
warehouse1and2 = 250449
warehouse2and3 = 222950
warehouse3 = sum_goods - warehouse1and2
print(warehouse3)
warehouse1 = sum_goods - warehouse2and3
print(warehouse1)
warehouse2 = sum_goods - (warehouse3 + warehouse1)
print(warehouse2)

print(warehouse1 + warehouse2 + warehouse3)
print(sum_goods is (warehouse1 + warehouse2 + warehouse3))
# ------- I have a question here :)) Why false ??

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment = 1179
months = 18
cost = payment * months
print(cost)

# task 07
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
namber_a = 8019 / 8
print(namber_a)
namber_b = 9907 / 9
print(namber_b)
namber_c = 2789 / 5
print(namber_c)
namber_d = 7248 / 6
print(namber_d)
namber_e = 7128 / 5
print(namber_e)
namber_f = 19224 / 9
print(namber_f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274
pizza_m = 218
juice = 35
cake = 350
water = 21
bd_cost = pizza_big * 4 + pizza_m * 2 + juice * 4 + cake + water * 3
print(bd_cost)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pictures = 232
one_page = 8
page_am = pictures / one_page
print(page_am)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
distance_b = 1600 / 100
liter_per_100km = 9
tank_capacity = 48
gas_needed = distance_b * liter_per_100km
print(gas_needed)
answer1 = 48 / 9
print(answer1)
answer2 = distance / tank_capacity
print(answer2)
