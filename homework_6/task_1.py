def is_even(number):
    return number % 2 == 0 or number == 0


def main():
    if is_even(4):
        print('is even number')
    else:
        print('is not even number')


if __name__ == '__main__':
    main()