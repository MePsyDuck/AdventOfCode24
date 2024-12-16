import math
from collections import deque
from heapq import heappop, heappush


def main():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    x, y = find(grid, 'S')
    # score = solve(grid, x, y, 0, (0, 1), list())
    # score = solve2(grid, x, y)
    score = solve3(grid)
    print(score)


def solve(grid, x, y, score, last_dir, v):
    if grid[x][y] == 'E':
        return score
    elif (x, y) in v:
        return math.inf
    elif grid[x][y] == '#':
        return math.inf
    else:
        v.append((x, y))
        i, j = last_dir
        same = solve(grid, x + i, y + j, score + 1, (i, j), v)
        clockwise = solve(grid, x + j, y - i, score + 1001, (j, -i), v)
        counterclockwise = solve(grid, x - j, y + i, score + 1001, (-j, i), v)
        v.remove((x, y))
        return min(same, clockwise, counterclockwise)


def solve2(grid, start_x, start_y):
    stack = deque([(start_x, start_y, 0, (0, 1), [])])
    min_score = math.inf

    while stack:
        x, y, score, last_dir, path = stack.pop()

        if (x, y) in path or grid[x][y] == '#':
            continue

        if grid[x][y] == 'E':
            min_score = min(min_score, score)
            continue

        path.append((x, y))

        i, j = last_dir
        next_moves = [
            (x + i, y + j, score + 1, (i, j)),
            (x + j, y - i, score + 1001, (j, -i)),
            (x - j, y + i, score + 1001, (-j, i))
        ]

        for nx, ny, nscore, ndir in next_moves:
            stack.append((nx, ny, nscore, ndir, path[:]))

        path.pop()

    return min_score


def solve3(grid):
    start = find(grid, 'S')
    end = find(grid, 'E')
    pq = [(start, 0, (0, 1))]
    best_scores = {}

    while pq:
        v, score, direction = heappop(pq)

        if score >= best_scores.get((v, direction), math.inf):
            continue
        x, y = v
        if grid[x][y] == '#':
            continue

        i, j = direction
        best_scores[(v, direction)] = score

        heappush(pq, ((x + i, y + j), score + 1, direction))
        heappush(pq, (v, score + 1000, (j, -i)))
        heappush(pq, (v, score + 1000, (-j, i)))

    return min(best_scores[(end, (0, 1))], best_scores[(end, (1, 0))], best_scores[(end, (0, -1))],
               best_scores[(end, (-1, 0))])


def find(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
