from random import randint


def main():
    a, b, n = map(int, input().split())

    arr = [randint(a, b) for i in range(n)]
    even, odd = 0, 0

    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print(*arr)
    print(even, odd)


if __name__ == '__main__':
    main()
