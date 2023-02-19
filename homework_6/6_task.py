def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def main():
    x = float(input("Enter number: "))
    print(sign(x))


if __name__ == '__main__':
    main()
