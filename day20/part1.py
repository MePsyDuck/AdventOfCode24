from collections import defaultdict, deque


def main():
    grid = []

    with open('input.txt') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    print(solve(grid))


def solve(grid):
    start = find_node(grid, 'S')
    end = find_node(grid, 'E')
    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'

    rows, cols = len(grid), len(grid[0])
    shortest, path = find_path(grid, start, end)
    cheat_paths = defaultdict(int)
    visited = set()

    for i, j in path:
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (ni, nj) not in visited and grid[ni][nj] == '#':
                visited.add((ni, nj))
                if 0 <= ni + di < rows and 0 <= nj + dj < cols and grid[ni + di][nj + dj] == '.':
                    saved = find_shortest_dist(grid, (i, j), (ni + di, nj + dj)) - 2
                    if saved >= 100:
                        cheat_paths[saved] += 1

    return sum(cheat_paths.values())


def find_node(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


def find_shortest_dist(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque([(start[0], start[1], 0)])

    while queue:
        i, j, dist = queue.popleft()
        if (i, j) == end:
            return dist
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and grid[ni][nj] != '#':
                queue.append((ni, nj, dist + 1))

    return -1


def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque([(start[0], start[1], 0)])
    path = []

    while queue:
        i, j, dist = queue.popleft()
        if (i, j) == end:
            return dist, path
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and grid[ni][nj] != '#':
                path.append((ni, nj))
                queue.append((ni, nj, dist + 1))

    return -1, path


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
