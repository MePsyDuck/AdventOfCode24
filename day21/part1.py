from collections import deque


def main():
    codes = []

    with open('input.txt') as f:
        for line in f.readlines():
            codes.append(line.strip())

    total = 0
    for code in codes:
        r = solve(code)
        print(code, r)
        total += int(code[:-1]) * r

    print(total)


def solve(code):
    numeric = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['-1', '0', 'A']]
    directional = [['-1', '^', 'A'], ['<', 'v', '>']]

    shortest_num = shortest_presses(numeric, code)
    shortest_dir = shortest_presses(directional, shortest_num)
    shortest_dir = shortest_presses(directional, shortest_dir)
    return len(shortest_dir)


def shortest_presses(keypad, code):
    non_key = find_node(keypad, '-1')
    path = ''
    start = find_node(keypad, 'A')

    for c in code:
        end = find_node(keypad, c)
        r = step(start, end, non_key)
        path += r
        start = end
    return path


def find_node(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


def step(start, end, invalid):
    ti, tj = end
    si, sj = start
    di = ti - si
    dj = tj - sj
    vert = 'v' * di + '^' * -di
    horiz = '>' * dj + '<' * -dj
    if dj > 0 and (ti, sj) != invalid:
        return vert + horiz + 'A'
    if (si, tj) != invalid:
        return horiz + vert + 'A'
    if (ti, sj) != invalid:
        return vert + horiz + 'A'


def bfs(grid, start, end, invalids):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'), (0, -1, '<')]
    visited = set()
    visited.add(invalids)
    queue = deque([(start, '')])

    while queue:
        (i, j), path = queue.popleft()
        if (i, j) == end:
            return path + 'A'
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for di, dj, sym in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                queue.append(((ni, nj), path + sym))

    return None


def dfs(grid, start, end, invalids):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'), (0, -1, '<')]
    visited = set()
    visited.add(invalids)
    stack = [(start, '')]

    while stack:
        (i, j), path = stack.pop()
        if (i, j) == end:
            return path + 'A'
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for di, dj, sym in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                stack.append(((ni, nj), path + sym))

    return None


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
