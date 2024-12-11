def main():
    with open('input.txt') as f:
        stones = [int(c) for c in f.read().strip().split(' ')]

    for i in range(25):
        stones = blink(stones)
        # print(stones)
    print(len(stones))


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new_stones.append(int(s[:len(s)//2]))
            new_stones.append(int(s[len(s)//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
