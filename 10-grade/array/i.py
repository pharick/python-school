def main():
    n = int(input())
    arr = [0] * n

    a, b = 1, 1

    for i in range(n):
        arr[i] = a
        a, b = b, a + b

    print(*arr)


if __name__ == '__main__':
    main()
