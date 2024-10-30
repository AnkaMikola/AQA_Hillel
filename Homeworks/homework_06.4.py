"""here is a docstring."""
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = []
for i in range(1, 50):
    lst1.append(i)

# lst1 = [i for i in range(1, 50)]

even_sum = sum(num for num in lst1 if num % 2 == 0)
print(f'The sum of all the numbers in the list is {even_sum}.')
