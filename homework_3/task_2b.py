num = input('Enter any three-digit number to find out the sum of its digits:')
num = int(num)
a = num % 10
b = num % 100 // 10
c = num // 100
print('sum:', a + b + c)
