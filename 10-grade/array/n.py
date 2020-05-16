from random import randint

def main():
    a, b, n = map(int, input().split())
    arr = [randint(a, b) for i in range(n)]

    max_n = -1

    for n in arr:
        if n > 0 and n % 2 == 0 and n > max_n:
            max_n = n

    print(*arr)
    print(max_n)


if __name__ == "__main__":
    main()
