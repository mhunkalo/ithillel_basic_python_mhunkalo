#a
def interchange_values(a, b):
    c = a
    a = b
    b = c
    return (a, b)
print(interchange_values(2, 3))
#b
a = 2
b = 3
a, b  = b, a
print(a,b)
#c
a = 2
b = 3
a = a + b
b = a - b
a = a - b
print(a,b)

