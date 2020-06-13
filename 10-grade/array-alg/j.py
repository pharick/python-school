def reverse(arr, start, end):
    for i in range((end - start) // 2):
        j = -1 - len(arr) + end - i
        i = i + start
        arr[i], arr[j] = arr[j], arr[i]


def main():
    input()
    arr = list(map(int, input().split()))
    reverse(arr, 0, len(arr) // 2)
    reverse(arr, len(arr) - len(arr) // 2, len(arr))
    print(*arr)


if __name__ == '__main__':
    main()
