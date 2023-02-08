text = input('Enter name, date of birth, date of death (in format Name*yyyy-mm-dd*yyyy-mm-dd):\n')
text = text.split('*')

a = text[1].split('-')
b = text[2].split('-')

print(f'\nName: {text[0]}\nAge: {int(b[0])-int(a[0])} years')