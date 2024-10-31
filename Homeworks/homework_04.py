"""here is a docstring."""
adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the ....
shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained
to whitewash. ....
By the time Ben was fagged out, Tom had traded
the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it
with—and so on, and so on,
hour after hour. And when the middle of the
afternoon came, from being a
poor poverty, stricken boy in the .... morning,
Tom was literally
rolling in wealth."""

# ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим
чином, через помилку. Треба замінити кінець абзацу
на пробіл .replace("\n", " ")"""
print('-----Task 1-----')
adventures_of_tom_sawer = adventures_of_tom_sawer.replace('\n', ' ')
print(adventures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print('\n-----Task 2-----')
adventures_of_tom_sawer = adventures_of_tom_sawer.replace(' .... ', ' ')
print(adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('\n-----Task 3-----')
adventures_of_tom_sawer = adventures_of_tom_sawer.strip()
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('\n-----Task 4-----')
h_letter = adventures_of_tom_sawer.count('h')
print(h_letter)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('\n-----Task 5-----')
cap_letter = sum(1 for char in adventures_of_tom_sawer if char.isupper())
print(cap_letter)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('\n-----Task 6-----')
first_occ = adventures_of_tom_sawer.find('Tom')
second_occ = adventures_of_tom_sawer.find('Tom', first_occ + 1)
print(second_occ)

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
print('\n-----Task 7-----')
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split('.')
sentences = [sentence.strip() for sentence
             in adventures_of_tom_sawer_sentences]
print(sentences)

"""cleaned_list = [item for item in sentences if item and item.strip()]
print(sentences)"""

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('\n-----Task 8-----')
four_sen = sentences[3]
print(four_sen.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('\n-----Task 9-----')
sentences = adventures_of_tom_sawer_sentences
if any(sentence.startswith('By the time') for sentence in sentences):
    print("There is a sentence that starts with 'By the time'.")
else:
    print("There is no sentence that starts with 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення
з adwentures_of_tom_sawer_sentences.
"""
print('\n-----Task 10-----')
last_el = sentences[-2].strip()

last_el_new = last_el + '.'
sentences[-1] = last_el_new
"""print(sentences[-1])"""
word_count = len(last_el_new.split())
print(f'There is an amount of words in the last sentence: {word_count}.')
