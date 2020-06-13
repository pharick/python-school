def min_3(arr):
    min1, min2, min3 = 10000, 10000, 10000

    for n in arr:
        if n < min1:
            min3, min2, min1 = min2, min1, n
        elif n < min2:
            min3, min2 = min2, n
        elif n < min3:
            min3 = n

    return min1, min2, min3


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*min_3(arr))

if __name__ == '__main__':
    main()