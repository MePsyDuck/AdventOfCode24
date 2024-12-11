import functools


def main():
    with open('input.txt') as f:
        print(sum([blink(int(stone), 75) for stone in f.read().split(' ')]))


@functools.cache
def blink(stone, times):
    if times == 0:
        return 1
    if stone == 0:
        return blink(1, times - 1)
    else:
        s = len(str(stone))
        if s % 2 == 0:
            power = 10 ** (s // 2)
            left = stone // power
            right = stone % power
            return blink(left, times - 1) + blink(right, times - 1)
        else:
            return blink(stone * 2024, times - 1)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
