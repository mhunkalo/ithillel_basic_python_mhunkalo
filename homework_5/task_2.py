def triangle_square_and_perimeter(a, b):  # returns 2 values
    s = (a * b) / 2
    c = (a**2 + b**2) ** 0.5
    p = a + b + c
    return s, p


leg_1, leg_2 = int(input('Input length of leg')), int(input('Input length of following leg'))
s, p = triangle_square_and_perimeter(leg_1, leg_2)
print('Square =', s)
print('Perimeter =', p)
