import re


def main():
    with open('input.txt') as f:
        print(mul(f.read()))


def mul(inst):
    regex = r"(?P<inst>mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don't\(\))"
    result = 0
    do = True

    for match in re.finditer(regex, inst):
        if match.groupdict()['inst']:
            if do:
                x = int(match.group('x'))
                y = int(match.group('y'))
                result += x * y
        elif match.groupdict()['do']:
            do = True
        else:
            do = False

    return result


if __name__ == '__main__':
    main()
