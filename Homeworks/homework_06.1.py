"""here is docstring."""

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

some_symbols = input('Let your cat walk on your keyboard. Than press "Enter" ')

unique_sym_count = len(set(some_symbols))
print(f'Unique symbols amount: {unique_sym_count}.')
