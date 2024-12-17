def main():
    reg_a = 0
    reg_b = 0
    reg_c = 0
    program = []

    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('Register A'):
                reg_a = int(line[11:])
            elif line.startswith('Register B'):
                reg_b = int(line[11:])
            elif line.startswith('Register C'):
                reg_c = int(line[11:])
            elif line.startswith('Program'):
                program = [int(i) for i in line[9:].split(',')]

    out = solve(reg_a, reg_b, reg_c, program)
    print(','.join(map(str, out)))


def solve(reg_a, reg_b, reg_c, program):
    def get_combo(literal):
        if literal == 4:
            return reg_a
        elif literal == 5:
            return reg_b
        elif literal == 6:
            return reg_c
        else:
            return literal

    out = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = get_combo(program[i + 1])

        if opcode == 0:
            reg_a = reg_a // (2 ** operand)
        elif opcode == 1:
            reg_b = reg_b ^ program[i + 1]
        elif opcode == 2:
            reg_b = operand % 8
        elif opcode == 3:
            if reg_a != 0:
                i = program[i + 1]
                i -= 2
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
        elif opcode == 5:
            out.append(operand % 8)
        elif opcode == 6:
            reg_b = reg_a // (2 ** operand)
        elif opcode == 7:
            reg_c = reg_a // (2 ** operand)
        i += 2

    return out


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
