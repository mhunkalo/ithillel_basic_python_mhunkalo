def interchange_values(a, b):
    c = a
    a = b
    b = c
    return (a, b)
print(interchange_values(2, 3))
a, b  = b, a

