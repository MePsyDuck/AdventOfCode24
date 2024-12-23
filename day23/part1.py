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
    triples = set()

    for k, v in graph.items():
        if k.startswith('t'):
            for n1 in graph[k]:
                for n2 in graph[n1]:
                    if k in graph[n2]:
                        triples.add(frozenset([k, n1, n2]))
    return len(triples)


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    if end_time - start_time < 1:
        print(f"{(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"{end_time - start_time:.6f} seconds")
