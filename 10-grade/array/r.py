from random import randint


def generate_list(n):
    return [i for i in range(1, n + 1)]


def mean(arr):
    return sum(arr) / len(arr) if len(arr) != 0 else 0


def shuffle(arr):
    for i in range(len(arr)):
        j = randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]


def main():
    n = int(input())
    arr = generate_list(n)
    shuffle(arr)
    print(*arr)


if __name__ == "__main__":
    main()
