def main():
    rules = dict()
    updates = []

    with open('input.txt') as f:
        for line in f:
            if line:
                if '|' in line:
                    x, y = line.strip().split('|')
                    if int(x) not in rules:
                        rules[int(x)] = set()
                    rules[int(x)].add(int(y))
                elif line.strip():
                    updates.append([int(i) for i in line.strip().split(',')])
    total = 0
    for req in updates:
        if is_ordered(req, rules):
            total += req[len(req) // 2]

    print(total)


def is_ordered(req, rules):
    pages_so_far = set()
    for page in req:
        if page in rules:
            ruleset = rules[page]
            if any(rule in pages_so_far for rule in ruleset):
                return False
        pages_so_far.add(page)
    return True


if __name__ == '__main__':
    main()
