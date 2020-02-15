from math import sqrt


def divs_sum(n):
    result = 1

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result += i + n // i

    return result


def main():
    a, b = map(int, input().split())

    print("YES" if divs_sum(a) == b and a == divs_sum(b) else "NO")


if __name__ == '__main__':
    main()
