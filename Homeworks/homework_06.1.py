"""here is docstring."""

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

string = 'zdlkvnjzaklnvklszdvn`lkcnklz klz djisdj'

unique_sym_count = len(set(string))
print(f'Unique symbols amount: {unique_sym_count}.')
