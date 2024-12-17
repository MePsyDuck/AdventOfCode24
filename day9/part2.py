def main():
    with open('input.txt') as f:
        disk = [int(c) for c in f.read().strip()]
    checksum = defrag(disk)
    print(checksum)


def defrag(disk):
    backup = disk.copy()
    checksum = 0
    index = -1

    i = 0
    while i < len(disk):
        if i % 2 == 0:
            if disk[i] == 0:
                index += backup[i]
            else:
                checksum += (i // 2) * sum_integers(index, disk[i])
                index += disk[i]
        else:
            j = len(disk) - 1
            while j > i and disk[i] > 0:
                if 0 < disk[j] <= disk[i]:
                    checksum += (j // 2) * sum_integers(index, disk[j])
                    disk[i] -= disk[j]
                    index += disk[j]
                    disk[j] = 0
                else:
                    j -= 2
            index += disk[i]
        i += 1

    return checksum


def sum_integers(index, step):
    return (step * (index * 2 + step + 1)) // 2

if __name__ == '__main__':
    import time
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
