import functools


def main():
    designs = []

    with open('input.txt') as f:
        for line in f.readlines():
            if ',' in line:
                patterns = set(line.strip().split(', '))
            elif line.strip():
                designs.append(line.strip())

    print(solve(patterns, designs))


def solve(patterns, designs):
    @functools.cache
    def is_possible(design):
        if not design:
            return True
        if design in patterns:
            return True
        i = 1
        while i <= len(design):
            if design[:i] in patterns and is_possible(design[i:]):
                return True
            i += 1
        return False

    return sum(is_possible(design) for design in designs)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
