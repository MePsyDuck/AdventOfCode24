import math
from heapq import heappop, heappush


def main():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    score = solve(grid)
    print(score)


def solve(grid):
    start = find(grid, 'S')
    end = find(grid, 'E')
    pq = [(start, 0, (0, 1), [])]
    best_scores = {}
    best_paths = set()
    best_end_score = math.inf

    while pq:
        v, score, direction, path = heappop(pq)

        if score > best_scores.get((v, direction), math.inf):
            continue
        x, y = v
        if grid[x][y] == '#':
            continue
        if grid[x][y] == 'E':
            if score < best_end_score:
                best_paths = set(path[:])
                best_end_score = score
            elif score == best_end_score:
                for n in path:
                    best_paths.add(n)
            continue

        i, j = direction
        best_scores[(v, direction)] = score

        heappush(pq, ((x + i, y + j), score + 1, direction, path[:] + [v]))
        heappush(pq, (v, score + 1000, (j, -i), path))
        heappush(pq, (v, score + 1000, (-j, i), path))

    return len(best_paths) + 1


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
