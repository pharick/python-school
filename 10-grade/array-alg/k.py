def reverse(arr, start, end):
    for i in range((end - start) // 2):
        j = -1 - len(arr) + end - i
        i = i + start
        arr[i], arr[j] = arr[j], arr[i]


def main():
    input()
    arr = list(map(int, input().split()))
    k, m = map(int, input().split())
    reverse(arr, k - 1, m)
    print(*arr)


if __name__ == '__main__':
    main()
