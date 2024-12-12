def main():
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    grid2 = [[c for c in line] for line in grid]

    price = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            plant = grid[i][j]
            a = area(grid, plant, i, j)
            if a != 0:
                p = set()
                perimeter(grid2, set(), plant, i, j, p)
                s = sides(grid2, p, plant)
                price += a * s
                print(plant, a, s)

    print(price)


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


def perimeter(grid, v, p, i, j, pm):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        pm.add((i, j))
        return
    if (i, j) in v:
        return
    if grid[i][j] == p:
        v.add((i, j))
        perimeter(grid, v, p, i + 1, j, pm)
        perimeter(grid, v, p, i - 1, j, pm)
        perimeter(grid, v, p, i, j + 1, pm)
        perimeter(grid, v, p, i, j - 1, pm)
        return
    pm.add((i, j))


def sides(grid, p, plant):
    sh = set()
    sv = set()
    for x, y in p:
        h = set()
        v = set()
        i = x
        while (i, y) in p:
            v.add((i, y))
            i -= 1
        i = x
        while (i, y) in p:
            v.add((i, y))
            i += 1

        j = y
        while (x, j) in p:
            h.add((x, j))
            j += 1
        j = y
        while (x, j) in p:
            h.add((x, j))
            j -= 1
        if len(h) == 1:
            if safe_get(grid, x - 1, y) == plant or safe_get(grid, x + 1, y) == plant:
                sh.add(frozenset(h))
        else:
            sh.add(frozenset(h))
        if len(v) == 1:
            if safe_get(grid, x, y - 1) == plant or safe_get(grid, x, y + 1) == plant:
                sv.add(frozenset(v))
        else:
            sv.add(frozenset(v))
    print([list(x) for x in sh])
    print([list(x) for x in sv])
    return len(sh) + len(sv)


def safe_get(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y]
    return None


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
