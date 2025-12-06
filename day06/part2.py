from functools import reduce
from pathlib import Path
import operator

INPUT_FILE = Path(__file__).parent / "input.txt"

OPS = {'+': operator.add, '*': operator.mul, }


def fixed_data(lines):
    # Check length of all strings and fix if IDE removed trailing space
    length = max(map(len, lines))
    *data, operations = (l.ljust(length) for l in lines)
    return data, operations, length


def calculate_grand_total(worksheet):
    data, operations, length = fixed_data(worksheet.splitlines())
    operands = []
    res = 0

    for i in range(length)[::-1]:
        if num := "".join(l[i] for l in data).strip():
            operands.append(int(num))
            if ops := operations[i].strip():
                op = OPS[ops]
                res += reduce(op, operands)
                operands = []

    return res


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(calculate_grand_total(ri))
