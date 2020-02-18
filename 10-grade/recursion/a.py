def binary(n):
    if abs(n) < 2:
        return n

    return str(binary(n // 2)) + str(n % 2)


def main():
    n = int(input())
    print(binary(abs(n)) if n > 0 else "-" + binary(abs(n)))


if __name__ == '__main__':
    main()
