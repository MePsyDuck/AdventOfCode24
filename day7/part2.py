import time


def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append([c for c in line.strip()])

    obs = patrol(grid)
    print(obs)


def find_guard(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j


def get_next_position(x, y, direction):
    if direction == 'N':
        return x - 1, y
    elif direction == 'S':
        return x + 1, y
    elif direction == 'W':
        return x, y - 1
    elif direction == 'E':
        return x, y + 1


def is_out_of_bounds(x, y, rows, cols):
    return x < 0 or x >= rows or y < 0 or y >= cols


def patrol(grid):
    r, c = len(grid), len(grid[0])
    rotated = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    ox, oy = find_guard(grid)
    visited = set()

    obs = 0
    direction = 'N'
    x, y = ox, oy

    while True:
        visited.add((x, y))
        nx, ny = get_next_position(x, y, direction)

        if is_out_of_bounds(nx, ny, r, c):
            break

        if grid[nx][ny] == '#':
            direction = rotated[direction]
        else:
            old = grid[nx][ny]
            grid[nx][ny] = '#'
            if (nx, ny) not in visited and is_looping(grid, ox, oy):
                obs += 1
            grid[nx][ny] = old
            x, y = nx, ny

    return obs


def is_looping(grid, x, y):
    r, c = len(grid), len(grid[0])
    rotated = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    direction = 'N'
    path = [[set() for _ in range(c)] for _ in range(r)]

    while True:
        path[x][y].add(direction)
        nx, ny = get_next_position(x, y, direction)

        if is_out_of_bounds(nx, ny, r, c):
            return False

        if grid[nx][ny] == '#':
            direction = rotated[direction]
        else:
            if direction in path[nx][ny]:
                return True
            x, y = nx, ny


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
