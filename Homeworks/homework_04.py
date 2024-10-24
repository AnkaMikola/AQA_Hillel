"""here is a docstring."""
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the
 .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but ....
 remained to whitewash. ....
By the time Ben was fagged out, Tom had traded
 the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної
# adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті
 випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('\n-----Task 1-----\n')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print('\n-----Task 2-----\n')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(' .... ', ' ')
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('\n-----Task 3-----\n')
adwentures_of_tom_sawer.strip()
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('\n-----Task 4-----\n')
h_letter = adwentures_of_tom_sawer.count('h')
print(h_letter)
print(f"The letter 'h' in the text occurs as many times as {h_letter}.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('\n-----Task 5-----\n')
words = adwentures_of_tom_sawer.split()
capitalized_words = [word for word in words if word[0].isupper()]
print('Capitalized words in the text:', len(capitalized_words))

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('\n-----Task 6-----\n')
target_word = 'Tom'
words = adwentures_of_tom_sawer.split()
count = 0

for index, word in enumerate(words):
    if word == target_word:
        count += 1
        if count == 2:
            print(f"The word '{target_word}' occurs for "
                  f'the second time at position:', index + 1)
            break

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print('\n-----Task 7-----\n')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з
 adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

# task 10
""" Виведіть кількість слів останнього
 речення з adwentures_of_tom_sawer_sentences.
"""
