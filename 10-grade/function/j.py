from math import sqrt


def digits_sum(n):
    result = 0

    while n > 0:
        result += n % 10
        n //= 10

    return result


def main():
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        s = digits_sum(i)

        is_suit = True
        for j in range(2, 10):
            if digits_sum(i * j) != s:
                is_suit = False
                break

        if is_suit:
            print(i, end=" ")
            


if __name__ == '__main__':
    main()
