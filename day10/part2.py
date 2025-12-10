import ast
from pathlib import Path

from z3 import Sum, sat, Optimize, IntVector

INPUT_FILE = Path(__file__).parent / "input.txt"


def parse(s) -> tuple[int]:
    v = ast.literal_eval(s)
    if isinstance(v, int):
        return (v,)
    return v


def solve(text):
    total = 0
    for line in text.splitlines():
        parts = line.split()
        buttons = [parse(b) for b in parts[1:-1]]
        joltages = tuple(map(int, parts[-1][1:-1].split(',')))

        opt = Optimize()
        bv = IntVector("xb", len(buttons))
        opt.add([xb >= 0 for xb in bv])  # button presses positive only

        # specify expression
        for i, v in enumerate(joltages):
            inv = [bv[j] for j, btn in enumerate(buttons) if i in btn]
            opt.add(Sum(inv) == v)

        total_presses = Sum(bv)
        opt.minimize(total_presses)

        if opt.check() != sat:
            raise Exception("Something went wrong")

        model = opt.model()
        total += model.eval(total_presses).as_long()

    return total


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve(ri))
