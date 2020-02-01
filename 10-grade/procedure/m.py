def num_system(number, base):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

    result = ''
    negative = number < 0
    number = abs(number)

    while number > 0:
        d = number % base
        result = digits[d] + result
        number //= base

    return "-" + result if negative else result


def main():
    number, base = map(int, input().split())
    print(num_system(number, base))


if __name__ == '__main__':
    main()
