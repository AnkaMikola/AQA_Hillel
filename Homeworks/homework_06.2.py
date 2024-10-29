"""here is a docstring."""
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово
# без букви "h".

while True:
    word = input("Hi! Enter the word that contain letter 'h': ")
    if 'h' in word.lower():
        print("Thank you! You entered the word that contain letter 'h'.")
        break
    else:
        print("The word doesn't contain letter 'h'. Try again: ")
