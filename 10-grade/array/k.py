from random import randint


def main():
    a, b, n = map(int, input().split())

    arr = [randint(a, b) for i in range(n)]
    count = 0

    for i in range(n):
        if arr[i] >= 100 and arr[i] <= 999 and arr[i] % 5 > 0:
            count += 1

    print(*arr)
    print(count)


if __name__ == '__main__':
    main()
