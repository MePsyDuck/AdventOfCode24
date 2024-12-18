import math
from heapq import heappop, heappush


def main():
    size = 71
    grid = [[1] * size for _ in range(size)]
    sim = 1024

    with open('input.txt') as f:
        for line in f.readlines():
            if not sim:
                break
            sim -= 1
            x, y = map(int, line.strip().split(','))
            grid[y][x] = 0

    # out = solve(grid, 0, 0, set())
    out = solve2(grid)
    print(out)


def solve(grid, x, y, v):
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        return 0
    if (x, y) in v:
        return math.inf
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return math.inf
    if not grid[x][y]:
        return math.inf

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    v.add((x, y))
    m = math.inf
    for dx, dy in d:
        m = min(solve(grid, x + dx, y + dy, v) + 1, m)
    v.remove((x, y))
    return m


def solve2(grid):
    pq = [((0, 0), 0)]
    best_scores = {}

    while pq:
        v, score = heappop(pq)
        if score >= best_scores.get(v, math.inf):
            continue
        x, y = v
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            continue
        if not grid[x][y]:
            continue
        best_scores[v] = score
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            heappush(pq, ((x + dx, y + dy), score + 1))
    return best_scores[(len(grid) - 1, len(grid[0]) - 1)]


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
