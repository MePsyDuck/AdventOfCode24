def main():
    robots = []
    with open('input.txt') as f:
        for line in f.readlines():
            p, v = line.strip().split(' ')
            px, py = map(int, p[2:].split(','))
            vx, vy = map(int, v[2:].split(','))
            robots.append((px, py, vx, vy))

    solve(robots)


def solve(robots):
    c = 101
    r = 103

    elapsed = 1
    while True:
        grid = [[' '] * c for _ in range(r)]
        for px, py, vx, vy in robots:
            npx = (px + (vx * elapsed)) % c
            npy = (py + (vy * elapsed)) % r
            grid[npy][npx] = '*'

        if any('***********' in ''.join(row) for row in grid):
            print(elapsed)
            print('\n'.join(''.join(row) for row in grid))
            break
        elapsed += 1


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
