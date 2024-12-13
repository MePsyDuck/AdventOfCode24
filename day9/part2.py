def main():
    with open('input.txt') as f:
        disk = [int(c) for c in f.read().strip()]

    nd = move(disk)
    # print(nd)
    print(checksum(nd))


def move(disk):
    new_disk = []

    i = 0
    j = len(disk) - 1
    while i < len(disk):
        if i % 2 == 0:
            for _ in range(disk[i]):
                new_disk.append(i // 2)
            i += 1
        elif j % 2 == 1:
            disk[j] = 0
            j -= 1
        else:
            while disk[i] > 0 and disk[j] > 0:
                new_disk.append(j // 2)
                disk[i] -= 1
                disk[j] -= 1

            if disk[i] == 0:
                i += 1
            else:
                j -= 1
    return new_disk


def checksum(disk):
    total = 0
    for i in range(len(disk)):
        total += disk[i] * i
    return total


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
