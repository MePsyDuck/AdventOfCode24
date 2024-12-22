def main():
    codes = []

    with open('input.txt') as f:
        for line in f.readlines():
            codes.append(int(line.strip()))

    total = 0
    for code in codes:
        r = solve(code)
        # print(code, r)
        total += r

    print(total)


def solve(code):
    for i in range(2000):
        code = ((code * 64) ^ code) % 16777216
        code = ((code // 32) ^ code) % 16777216
        code = ((code * 2048) ^ code) % 16777216

    return code


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
