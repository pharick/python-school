def even_digits(n):
    if n == 0:
        return 0

    return even_digits(n // 10) + (1 if n % 10 % 2 == 0 else 0)


def main():
    n = int(input())
    print(even_digits(n))


if __name__ == '__main__':
    main()