"""here is a docstring."""
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurrence in text
# bellow (total sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it


poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

lower_text = poem_text.lower()

vowel1 = lower_text.count('a')
vowel2 = lower_text.count('e')
vowel3 = lower_text.count('i')
vowel4 = lower_text.count('o')
vowel5 = lower_text.count('u')

print('\n-----Task 1-----\n')

TEMPLATE_horizontal_rule = '-----------------'
TEMPLATE_hat = '| vowel | count |'
TEMPLATE_vowel1 = '|   a   |  {0}   |'
TEMPLATE_vowel2 = '|   e   |  {0}   |'
TEMPLATE_vowel3 = '|   i   |  {0}   |'
TEMPLATE_vowel4 = '|   o   |  {0}   |'
TEMPLATE_vowel5 = '|   u   |   {0}   |'

print(TEMPLATE_horizontal_rule)
print(TEMPLATE_hat)
print(TEMPLATE_horizontal_rule)

print(TEMPLATE_vowel1.format(vowel1))
print(TEMPLATE_vowel2.format(vowel2))
print(TEMPLATE_vowel3.format(vowel3))
print(TEMPLATE_vowel4.format(vowel4))
print(TEMPLATE_vowel5.format(vowel5))

print(TEMPLATE_horizontal_rule)

# task 2

print('\n-----Task 2-----\n')
trans_table = str.maketrans('AaEeIiOoUu', 'ÀàÉéÍíÓóÚú')
changed_poem = poem_text.translate(trans_table)
print(changed_poem)
