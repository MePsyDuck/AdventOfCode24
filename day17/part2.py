import multiprocessing as mp


def main():
    reg_b = 0
    reg_c = 0
    program = []

    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('Register A'):
                continue
            elif line.startswith('Register B'):
                reg_b = int(line[11:])
            elif line.startswith('Register C'):
                reg_c = int(line[11:])
            elif line.startswith('Program'):
                program = [int(i) for i in line[9:].split(',')]

    parallel_solver(reg_b, reg_c, program)
    # for i in range(1 << 32):
    #     if solve(i, reg_b, reg_c, program):
    #         print(i)
    #         break
    #     if i % 10000 == 0:
    #         print(i)


def solve_task(start, end, reg_b, reg_c, program, stop_flag):
    for i in range(start, end):
        if stop_flag.is_set():
            break
        if solve(i, reg_b, reg_c, program):
            print(f"Solution found: {i}")
            stop_flag.set()
            break
        if i % 1000000 == 0:
            print(f"Checked up to {i} in range ({start}, {end})")


def parallel_solver(reg_b, reg_c, program, num_processes=mp.cpu_count()):
    total_range = 1 << 32
    chunk_size = total_range // num_processes
    stop_flag = mp.Event()
    processes = []

    for p in range(num_processes):
        start = p * chunk_size
        end = (p + 1) * chunk_size if p < num_processes - 1 else total_range
        process = mp.Process(target=solve_task, args=(start, end, reg_b, reg_c, program, stop_flag))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


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

    j = 0
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
            if j == len(program):
                return True
            if program[j] != operand % 8:
                return False
            j += 1
        elif opcode == 6:
            reg_b = reg_a // (2 ** operand)
        elif opcode == 7:
            reg_c = reg_a // (2 ** operand)
        i += 2

    return j == len(program)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
