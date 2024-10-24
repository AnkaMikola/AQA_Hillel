"""here is a docstring."""
# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string

norway_text = ('Automatisering akselererer %syeblikket '
               'da roboter vil erobre planeten v%sr. (%s)') % ('ø', 'å', 'Æ')
print(norway_text)

# #1 string with format() call
symbol1 = 'ø'
symbol2 = 'å'
symbol3 = 'Æ'
not_norway_text = ('Automatisering akselererer {0}yeblikket da'
                   ' roboter vil erobre planeten v{1}r.'
                   ' ({2})').format(symbol1, symbol2, symbol3)
print(not_norway_text)

# #2 f-string
another_not_norway_text = (f'Automatisering akselererer {symbol1}yeblikket da'
                           f' roboter vil erobre planeten v{symbol2}r.'
                           f' ({symbol3})')
print(another_not_norway_text)
