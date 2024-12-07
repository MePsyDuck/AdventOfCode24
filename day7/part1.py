def main():
    eqns = []

    with open('input.txt') as f:
        for line in f:
            test_value, exp = line.strip().split(':')
            exp = [int(eq.strip()) for eq in exp.split(' ') if eq.strip()]
            eqns.append((int(test_value), exp))

    sum = 0
    for eqn in eqns:
        if can_be_true(eqn):
            sum += eqn[0]
    print(sum)


def can_be_true(eqn):
    test_value, exp = eqn

    return bfs(exp, 0, test_value, exp[0])


def bfs(exp, index, target, partial):
    if index == len(exp) - 1:
        return partial == target
    if partial > target:
        return False

    return bfs(exp, index + 1, target, partial + exp[index + 1]
            or bfs(exp, index + 1, target, partial * exp[index + 1])
            or bfs(exp, index + 1, target, int(str(partial) + str(exp[index + 1]))))


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
