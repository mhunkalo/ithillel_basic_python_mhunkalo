n = input('Введіть слова з нижнім підкреслюванням:')

print( * map(str.capitalize, n.split('_')), sep = '')