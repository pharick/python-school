from math import sqrt


def divs_sum(n):
    result = 1

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result += i + n // i

    return result


def is_perfect(n):
    return n == divs_sum(n)


def main():
    n = int(input())
    print('YES' if is_perfect(n) else 'NO')
            


if __name__ == '__main__':
    main()
