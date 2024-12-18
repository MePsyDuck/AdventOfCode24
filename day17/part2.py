def main():
    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('Program'):
                program = [int(i) for i in line[9:].split(',')]
    result = []
    solve(program, 0, len(program) - 1, result)
    print(min(result))


def solve(prg, last_a, j, result):
    """
    Generated via reverse engineering
    My input is : 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0
    Where each operation is
    2,4 : b = a % 8
    1,5 : b = b ^ 5
    7,5 : c = a // (2 ** b)
    4,3 : b = b ^ c
    1,6 : b = b ^ 6
    0,3 : a = a // 8
    5,5 : print b % 8
    3,0 : goto beginning if a!=0

    Reversing above operations (bottom to top) abd substituting values
        b = b ^ 6
        b = (b ^ c) ^ 6
        b = (b ^ (a // (2 ** b))) ^ 6
        b = ((b ^ 5) ^ (a // (2 ** (b ^ 5)))) ^ 6
        b = (((a % 8) ^ 5) ^ (a // (2 ** ((a % 8) ^ 5)))) ^ 6

    Simplifying above
        => b = (a % 8) ^ 5 ^ (a // (2 ** ((a % 8) ^ 5))) ^ 5
        => b = 3 ^ (a % 8) ^ (a // (2 ** ((a % 8) ^ 5)))

    Since we are printing b % 8, the program values should be equal to b % 8
        => 3 ^ (a % 8) ^ (a // (2 ** ((a % 8) ^ 5))) % 8 = program[j]

    The program will only halt if a = 0,
        => a // 8 = 0
        => initial value of 'a' is in range [0, 8)

    While we get the expected output, recursively call solve with new 'a' and j+1
    Using reverse of operation a = a // 8, new 'a' is in range [a * 8, a * 8 + 8)
    """
    for i in range(last_a, last_a + 8):
        if (3 ^ (i % 8) ^ (i // (2 ** ((i % 8) ^ 5)))) % 8 == prg[j]:
            if j == 0:
                result.append(i)
            else:
                solve(prg, i * 8, j - 1, result)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if end - start < 1:
        print(f"{(end - start) * 1000:.2f} milliseconds")
    else:
        print(f"{end - start:.6f} seconds")
