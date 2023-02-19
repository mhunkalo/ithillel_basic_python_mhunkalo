def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    x1 = (-b + discriminant**0.5) / 2
    x2 = (-b - discriminant**0.5) / 2
    return x1, x2


def main():
    a = int(input('Input a '))
    b = int(input('Input b '))
    c = int(input('Input c '))
    x1, x2 = solve_quadratic_equation(a, b, c)
    print(f'x1 = {x1}, x2 = {x2}')


if __name__ == '__main__':
    main()