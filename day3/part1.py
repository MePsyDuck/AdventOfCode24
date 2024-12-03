import re


def main():
    result = 0

    with open('input.txt') as f:
        for line in f:
            result += mul(line)
    print(result)


def mul(inst):
    regex = r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)"
    result = 0

    for match in re.finditer(regex, inst):
        x = int(match.group('x'))
        y = int(match.group('y'))
        result += x * y

    return result


if __name__ == '__main__':
    main()
