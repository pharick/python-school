def print_8(n):
    result = ''

    for i in range(10):
        d = n % 8
        result = str(d) + result
        n //= 8

    print(result)


def main():
    n = int(input())
    print_8(n)


if __name__ == '__main__':
    main()
