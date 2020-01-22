def print_roman(n):
    digits = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
              ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
              ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
              ['', 'M', 'MM', 'MMM']]

    result = ''
    r = 0

    while n > 0:
        d = n % 10
        n //= 10
        result = digits[r][d] + result
        r += 1

    print(result)


def main():
    n = int(input())
    print_roman(n)


if __name__ == '__main__':
    main()