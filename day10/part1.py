import ast
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def string_to_int(s: str) -> int:
    return int(s[::-1].replace('#', '1').replace('.', '0'), 2)


def bits_to_int(bits: tuple) -> int:
    return sum(1 << b for b in bits)


def parse(s: str) -> tuple[int]:
    v = ast.literal_eval(s)
    if isinstance(v, int):
        return (v,)
    return v


def solve(text: str) -> int:
    presses = 0
    for line in text.splitlines():
        args = line.split()
        tm = args[0]
        indicators = string_to_int(tm[1:tm.index("]")])
        buttons = [bits_to_int(parse(b)) for b in args[1:-1]]

        states = {0}
        while indicators not in states:
            presses += 1
            states = {x ^ b for x in states for b in buttons}
    return presses


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve(ri))
