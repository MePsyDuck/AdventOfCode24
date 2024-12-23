from collections import defaultdict


def main():
    network = defaultdict(set)

    with open('input.txt') as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            network[a].add(b)
            network[b].add(a)

    print(solve(network))


def solve(graph):
    parties = []

    for k, v in graph.items():
        for party in parties:
            if all(k in graph[p] for p in party):
                party.add(k)
        for p in v:
            parties.append({k, p})

    largest = []
    for p in parties:
        if len(p) > len(largest):
            largest = p

    return ','.join(sorted(largest))


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
