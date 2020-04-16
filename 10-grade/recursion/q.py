from math import sqrt


def is_simple(n, d=2):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % d == 0:
        return False

    if d < sqrt(n):
        return is_simple(n, d + 1)

    return True


def main():
    n = int(input())
    print("YES" if is_simple(n) else "NO")


if __name__ == '__main__':
    main()
