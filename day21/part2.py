import functools
from collections import Counter

numeric = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['-1', '0', 'A']]
directional = [['-1', '^', 'A'], ['<', 'v', '>']]


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
    paths = shortest_presses(numeric, code)
    for i in range(25):
        new_paths = Counter()

        for path in paths:
            sub_paths = shortest_presses(directional, path)
            for sub_path in sub_paths:
                sub_paths[sub_path] *= paths[path]
            new_paths.update(sub_paths)

        paths = new_paths

    return sum(len(k) * v for k, v in paths.items())


def shortest_presses(keypad, code):
    non_key = find_node(keypad, '-1')
    start = find_node(keypad, 'A')
    paths = Counter()

    for c in code:
        end = find_node(keypad, c)
        r = step(start, end, non_key)
        paths[r] += 1
        start = end
    return paths


def find_node(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


@functools.cache
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


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
