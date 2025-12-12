from functools import cache
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve(text: str) -> int:
    d = {k: v.split() for k, v in (l.split(": ") for l in text.splitlines())}

    @cache
    def ways(current: str, target: tuple[str, ...]) -> int:
        if current == "out":
            return len(target) == 0
        if current in target:
            target = tuple(x for x in target if x != current)

        return sum(ways(neighbor, target) for neighbor in d[current])

    res = ways("svr", ("dac", "fft"))
    return res


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve(ri))
