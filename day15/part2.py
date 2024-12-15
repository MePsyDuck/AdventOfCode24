def main():
    grid = []
    moves = ''
    with open('input.txt') as f:
        for line in f.readlines():
            if '#' in line:
                line = line.strip()
                line = line.replace('#', '##')
                line = line.replace('O', '[]')
                line = line.replace('.', '..')
                line = line.replace('@', '@.')
                grid.append(list(line))
            elif line:
                moves += line.strip()

    solve(grid, moves)
    gps = find_coords_sum(grid)
    print(gps)


def solve(grid, moves):
    x, y = find_robot(grid)

    direction = {'>': (0, 1), 'v': (1, 0), '^': (-1, 0), '<': (0, -1)}

    for m in moves:
        dx, dy = direction[m]
        if dy != 0:
            move_y(grid, x, y, dy)
        else:
            if can_move_x(grid, x + dx, y, dx):
                move_x(grid, x + dx, y, dx)
                grid[x][y], grid[x + dx][y] = grid[x + dx][y], grid[x][y]
                x += dx
    print1(grid)


def move_y(grid, x, y, dy):
    j = y + dy
    while grid[x][j] in '[]':
        j += dy

    if grid[x][j] == '.':
        while j != y:
            grid[x][j], grid[x][j - dy] = grid[x][j - dy], grid[x][j]
            j -= dy
        y += dy


def can_move_x(grid, x, y, dx):
    c = grid[x][y]
    if c == '#':
        return False
    if c == '.':
        return True

    dy = {'[': 1, ']': -1}
    return can_move_x(grid, x + dx, y, dx) and can_move_x(grid, x + dx, y + dy[c], dx)


def move_x(grid, x, y, dx):
    c = grid[x][y]

    if c in '[]':
        dy = {'[': 1, ']': -1, '.': 0}
        move_x(grid, x + dx, y, dx)
        move_x(grid, x + dx, y + dy[c], dx)
        grid[x][y], grid[x + dx][y] = grid[x + dx][y], grid[x][y]
        grid[x][y + dy[c]], grid[x + dx][y + dy[c]] = grid[x + dx][y + dy[c]], grid[x][y + dy[c]]


def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j


def find_coords_sum(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                total += i * 100 + j

    return total


def print1(grid):
    for line in grid:
        print(''.join(line))


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
