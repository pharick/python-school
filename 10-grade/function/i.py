from math import sqrt


def divs_sum(n):
    result = 1

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result += i + n // i

    return result


def main():
    a, b = map(int, input().split())
    count = 0

    for i in range(a, b + 1):
        d = divs_sum(i)

        if i <= b and divs_sum(d) == i and i < d:
            print('(', i, ',', d, ')', sep='', end=' ')
            count += 1

    if count == 0:
        print(0)


if __name__ == '__main__':
    main()
