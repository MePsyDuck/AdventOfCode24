def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append([c for c in line.strip()])

    x, y = find_guard(grid)
    patrol(grid, x, y)

    count = 1
    for line in grid:
        count += line.count('X')
    print(count)


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return i, j


def patrol(grid, x, y):
    r = len(grid)
    c = len(grid[0])

    while True:
        # print('\n'.join([str(line) for line in grid]))
        if x < 0 or x >= c or y < 0 or y >= r:
            return

        direction = grid[x][y]

        if direction == '^':
            if x == 0:
                return
            elif grid[x - 1][y] == '#':
                grid[x][y] = '>'
            else:
                grid[x][y] = 'X'
                grid[x - 1][y] = '^'
                x = x - 1
        elif direction == 'v':
            if x == r - 1:
                return
            elif grid[x + 1][y] == '#':
                grid[x][y] = '<'
            else:
                grid[x][y] = 'X'
                grid[x + 1][y] = 'v'
                x = x + 1
        elif direction == '<':
            if y == 0:
                return
            elif grid[x][y - 1] == '#':
                grid[x][y] = '^'
            else:
                grid[x][y] = 'X'
                grid[x][y - 1] = '<'
                y = y - 1
        elif direction == '>':
            if y == c - 1:
                return
            elif grid[x][y + 1] == '#':
                grid[x][y] = 'v'
            else:
                grid[x][y] = 'X'
                grid[x][y + 1] = '>'
                y = y + 1


if __name__ == '__main__':
    main()
