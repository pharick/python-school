def max_digit(n):
    if n == 0:
        return 0

    return max(n % 10, max_digit(n // 10))


def main():
    n = int(input())
    print(max_digit(n))


if __name__ == '__main__':
    main()
