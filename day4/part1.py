def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append(line.strip())
    print(search(grid))


def search(grid):
    r = len(grid)
    c = len(grid[0])

    count = 0

    def search_direction(x, y, index, direction):
        if x < 0 or x >= c or y < 0 or y >= r:
            return

        s = grid[x][y]
        new_x = x
        new_y = y
        if 'N' in direction:
            new_y = y - 1
        if 'S' in direction:
            new_y = y + 1
        if 'W' in direction:
            new_x = x - 1
        if 'E' in direction:
            new_x = x + 1

        if index == 0 and s == 'X':
            search_direction(new_x, new_y, index + 1, direction)
        if index == 1 and s == 'M':
            search_direction(new_x, new_y, index + 1, direction)
        if index == 2 and s == 'A':
            search_direction(new_x, new_y, index + 1, direction)
        if index == 3 and s == 'S':
            nonlocal count
            count += 1

    for i in range(r):
        for j in range(c):
            for d in ['N', 'S', 'W', 'E', 'NE', 'SE', 'SW', 'NW']:
                search_direction(i, j, 0, d)
    return count


if __name__ == '__main__':
    main()
