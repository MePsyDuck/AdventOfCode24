def main():
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('Prize'):
                p = map(int, [c[2:] for c in line[7:].split(', ')])
                s = solve(p, a, b)
                total += s
            elif line.startswith('Button A'):
                a = map(int, [c[2:] for c in line[10:].split(', ')])
            elif line.startswith('Button B'):
                b = map(int, [c[2:] for c in line[10:].split(', ')])

    print(total)


def solve(p, a, b):
    px, py = p
    ax, ay = a
    bx, by = b

    i = by * px - bx * py
    j = ax * py - ay * px
    det = ax * by - ay * bx

    if det == 0 or i % det != 0 or j % det != 0:
        return 0

    A = 3 * i // det
    B = j // det

    return A + B


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
