def main():
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    grid2 = [[c for c in line] for line in grid]

    price = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            plant = grid[i][j]
            p = plots(grid, plant, i, j)
            if p:
                s = count_sides(grid2, p, plant)
                price += len(p) * s
                print(plant, s)

    print(price)


def plots(grid, p, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return []
    if grid[i][j] == '#':
        return []
    if grid[i][j] == p:
        grid[i][j] = '#'
        t = [(i, j)]
        t.extend(plots(grid, p, i + 1, j))
        t.extend(plots(grid, p, i - 1, j))
        t.extend(plots(grid, p, i, j + 1))
        t.extend(plots(grid, p, i, j - 1))
        return t
    return []


def count_sides(grid, plot, plant):
    sides = 0
    for x, y in plot:
        has_north = safe_get(grid, x - 1, y) == plant
        has_south = safe_get(grid, x + 1, y) == plant
        has_east = safe_get(grid, x, y + 1) == plant
        has_west = safe_get(grid, x, y - 1) == plant
        has_north_west = safe_get(grid, x - 1, y - 1) == plant
        has_north_east = safe_get(grid, x - 1, y + 1) == plant
        has_south_west = safe_get(grid, x + 1, y - 1) == plant
        has_south_east = safe_get(grid, x + 1, y + 1) == plant

        if not has_north and not has_east: sides += 1
        if not has_north and not has_west: sides += 1
        if not has_south and not has_east: sides += 1
        if not has_south and not has_west: sides += 1
        if has_north and has_east and not has_north_east: sides += 1
        if has_north and has_west and not has_north_west: sides += 1
        if has_south and has_east and not has_south_east: sides += 1
        if has_south and has_west and not has_south_west: sides += 1

    return sides


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
