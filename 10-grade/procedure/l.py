def num_system(number, base):
    result = ''
    negative = number < 0
    number = abs(number)

    while number > 0:
        d = number % base
        result = str(d) + result
        number //= base

    return -int(result) if negative else int(result)


def main():
    number, base = map(int, input().split())
    print(num_system(number, base))


if __name__ == '__main__':
    main()
