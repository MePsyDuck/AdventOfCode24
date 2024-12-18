import math
from heapq import heappop, heappush


def main():
    bytes = []

    with open('input.txt') as f:
        for line in f.readlines():
            x, y = map(int, line.strip().split(','))
            bytes.append((x, y))

    i = 0
    j = len(bytes)
    while i < j:
        mid = (i + j) // 2
        r = solve(bytes, mid)
        if r:
            if not solve(bytes, mid + 1):
                print(bytes[mid])
                return
            else:
                i = mid
        else:
            j = mid


def solve(bytes, falls):
    size = 71
    grid = [[1] * size for _ in range(size)]

    i = falls
    while i:
        x, y = bytes[i - 1]
        grid[y][x] = 0
        i -= 1

    pq = [((0, 0), 0)]
    best_scores = {}

    while pq:
        v, score = heappop(pq)
        if v == (len(grid) - 1, len(grid[0]) - 1):
            return True
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
    return False


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
(54, 44)