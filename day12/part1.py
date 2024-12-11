def main():
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    grid2 = [[c for c in line] for line in grid]

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            plant = grid[i][j]
            a = area(grid, plant, i, j)
            if a != 0:
                p = perimeter(grid2, set(), plant, i, j)
                s += a * p
                # print(plant, a, p)

    print(s)


def area(grid, p, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] == '#':
        return 0
    if grid[i][j] == p:
        grid[i][j] = '#'
        return 1 + area(grid, p, i + 1, j) + area(grid, p, i - 1, j) + area(grid, p, i, j + 1) + area(grid, p, i, j - 1)
    else:
        return 0


def perimeter(grid, v, p, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 1
    if (i, j) in v:
        return 0
    if grid[i][j] == p:
        v.add((i, j))
        return (perimeter(grid, v, p, i + 1, j) +
                perimeter(grid, v, p, i - 1, j) +
                perimeter(grid, v, p, i, j + 1) +
                perimeter(grid, v, p, i, j - 1))
    else:
        return 1


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
