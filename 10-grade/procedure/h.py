def print_16(n):
    result = ''
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for i in range(4):
        d = n % 16
        result = digits[d] + result
        n //= 16

    print(result)


def main():
    n = int(input())
    print_16(n)


if __name__ == '__main__':
    main()
