def main():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            grid.append([int(c) if c != '.' else -1 for c in line.strip()])

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s += trail_score(grid, i, j, 0)
    print(s)


def trail_score(grid, i, j, h):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        if h == 9 == grid[i][j]:
            return 1
        elif grid[i][j] == h:
            return (trail_score(grid, i + 1, j, h + 1) +
                    trail_score(grid, i - 1, j, h + 1) +
                    trail_score(grid, i, j + 1, h + 1) +
                    trail_score(grid, i, j - 1, h + 1))
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
