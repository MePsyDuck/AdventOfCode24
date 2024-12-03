from collections import Counter


def part1():
    l1 = []
    l2 = []
    with open('input.txt') as f:
        for line in f:
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))

    l1 = sorted(l1)
    l2 = sorted(l2)
    dist = 0
    for a, b in zip(l1, l2):
        dist += abs(b - a)

    print(dist)


def part2():
    l1 = []
    l2 = []
    with open('input.txt') as f:
        for line in f:
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))

    c = Counter(l2)
    siml = 0
    for a in l1:
        siml += a*c[a]

    print(siml)


if __name__ == '__main__':
    part1()
    part2()
