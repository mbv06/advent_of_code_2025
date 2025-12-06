from functools import reduce
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"

import operator

OPS = {'+': operator.add, '*': operator.mul, }


def calculate_grand_total(worksheet):
    data = []
    lines = worksheet.splitlines()
    for opl in lines[:-1]:
        data.append(list(map(int, opl.split())))

    res = 0
    operations = (op for op in lines[-1].split())
    for i, op in enumerate(operations):
        res += reduce(OPS[op], [d[i] for d in data])

    return res


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(calculate_grand_total(ri))
