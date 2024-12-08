from collections import defaultdict


def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append([c for c in line.strip()])

    print(find_antinodes(grid))


def find_antinodes(grid):
    r = len(grid)
    c = len(grid[0])

    freqs = defaultdict(list)
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '.':
                freqs[grid[i][j]].append((i, j))

    antinodes = set()
    for freq in freqs:
        nodes = freqs[freq]
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]
                dx = x2 - x1
                dy = y2 - y1
                nx1 = x1 - dx
                nx2 = x2 + dx
                ny1 = y1 - dy
                ny2 = y2 + dy
                if inbounds(nx1, ny1, r, c) and grid[nx1][ny1] != freq:
                    grid[nx1][ny1] = '#'
                    antinodes.add((nx1, ny1))
                if inbounds(nx2, ny2, r, c) and grid[nx2][ny2] != freq:
                    grid[nx2][ny2] = '#'
                    antinodes.add((nx2, ny2))

    return len(antinodes)


def inbounds(x, y, r, c):
    return 0 <= x < r and 0 <= y < c


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
