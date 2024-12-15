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
    gps = find_coords(grid)
    print(gps)


def solve(grid, moves):
    x, y = find_robot(grid)

    direction = {'>': (0, 1), 'v': (1, 0), '^': (-1, 0), '<': (0, -1)}

    for m in moves:
        dx, dy = direction[m]
        i = x + dx
        j = y + dy
        while grid[i][j] == 'O':
            i += dx
            j += dy

        if grid[i][j] == '.':
            while i != x or j != y:
                grid[i][j], grid[i - dx][j - dy] = grid[i - dx][j - dy], grid[i][j]
                i -= dx
                j -= dy
            x += dx
            y += dy
        # print(m)
    # print1(grid)


def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j


def find_coords(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
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
