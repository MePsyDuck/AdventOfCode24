def part1():
    safe = 0
    with open('input.txt') as f:
        for line in f:
            report = [int(level) for level in line.split()]
            if is_safe(report):
                safe += 1

    print(safe)


def is_safe(report):
    if len(report) < 2:
        return True

    if report[0] > report[1]:
        return check_decreasing_safe(report)
    elif report[0] < report[1]:
        return check_increasing_safe(report)
    else:
        return False


def check_increasing_safe(report):
    last = report[0]
    for current in report[1:]:
        if current <= last or current - last > 3:
            return False
        last = current

    return True


def check_decreasing_safe(report):
    last = report[0]
    for current in report[1:]:
        if current >= last or last - current > 3:
            return False
        last = current

    return True


if __name__ == '__main__':
    part1()
