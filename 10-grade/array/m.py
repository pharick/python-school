from random import randint


def digit_sum(n):
    result = 0
    n = abs(n)

    while n > 0:
        result += n % 10
        n //= 10

    return result


def main():
    a, b, n, k = map(int, input().split())

    arr = [randint(a, b) for i in range(n)]
    count = 0

    for i in range(n):
        if digit_sum(arr[i]) == k:
            count += 1

    print(*arr)
    print(count)


if __name__ == '__main__':
    main()
