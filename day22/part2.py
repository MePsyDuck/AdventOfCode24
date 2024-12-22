from collections import defaultdict


def main():
    with open('input.txt') as f:
        codes = map(int, f.readlines())

    print(solve(codes))


def solve(codes):
    super_dict = defaultdict(int)

    for code in codes:
        old_price = code % 10
        sliding_seq = []
        seqs_vs_price = defaultdict(int)

        for j in range(2000):
            code = ((code * 64) ^ code) % 16777216
            code = ((code // 32) ^ code) % 16777216
            code = ((code * 2048) ^ code) % 16777216

            current_price = code % 10
            change = current_price - old_price
            sliding_seq.append(change)
            old_price = current_price

            if j >= 3:
                seq = tuple(sliding_seq)
                if seq not in seqs_vs_price:
                    seqs_vs_price[seq] = current_price
                sliding_seq.pop(0)

        for seq, price in seqs_vs_price.items():
            super_dict[seq] += price

    return max(super_dict.values())


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
