def main():
    total = {00: 0, 10: 0, 1: 0, 11: 0, 99: 0}
    with open('input.txt') as f:
        for line in f.readlines():
            p, v = line.strip().split(' ')
            px, py = map(int, p[2:].split(','))
            vx, vy = map(int, v[2:].split(','))
            quadrant = solve(px, py, vx, vy)
            total[quadrant] += 1

    print(total)
    print(total[00] * total[1] * total[10] * total[11])


def solve(px, py, vx, vy):
    sec = 100
    c = 101
    r = 103
    hc = c // 2
    hr = r // 2

    npx = (px + (vx * sec)) % c
    npy = (py + (vy * sec)) % r

    if hc == npx or hr == npy:
        return 99

    return 10 * (npx > hc) + (npy > hr)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
