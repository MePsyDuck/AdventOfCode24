def main():
    safe = 0
    with open('input.txt') as f:
        for line in f:
            report = [int(level) for level in line.split()]
            if is_safe(report):
                safe += 1

    print(safe)


def is_safe(report):
    if len(report) < 3:
        return True
    increasing = 0
    decreasing = 0
    last = report[0]
    for current in report[1:]:
        if current > last:
            increasing += 1
        elif current < last:
            decreasing += 1
        last = current

    if increasing > decreasing:
        return check_increasing_safe(report)
    else:
        return check_decreasing_safe(report)


def check_increasing_safe(report, allow_error=True):
    for i in range(1, len(report)):
        last = report[i - 1]
        current = report[i]

        if current <= last or current - last > 3:
            if allow_error:
                return check_increasing_safe(report[:i - 1] + report[i:], False) or check_increasing_safe(report[:i] + report[i+1:], False)
            else:
                return False

    return True


def check_decreasing_safe(report, allow_error=True):
    for i in range(1, len(report)):
        last = report[i - 1]
        current = report[i]

        if current >= last or last - current > 3:
            if allow_error:
                return check_decreasing_safe(report[:i - 1] + report[i:], False)or check_decreasing_safe(report[:i] + report[i+1:], False)
            else:
                return False

    return True


if __name__ == '__main__':
    main()
