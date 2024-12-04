def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append(line.strip())
    print(search(grid))


def search(grid):
    r = len(grid)
    c = len(grid[0])

    count = 0

    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if grid[i][j] == 'A':
                nw = grid[i - 1][j - 1]
                ne = grid[i - 1][j + 1]
                sw = grid[i + 1][j - 1]
                se = grid[i + 1][j + 1]

                for word in ['MS', 'SM']:
                    first, second = word
                    if first == nw == ne and second == sw == se:
                        count += 1
                    elif first == ne == se and second == sw == nw:
                        count += 1

    return count


if __name__ == '__main__':
    main()
