from itertools import combinations
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def square_on_decart(p: tuple) -> int:
    p1, p2 = p[0], p[1]
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


def solve(text: str) -> int:
    coordinates = [list(map(int, l.split(","))) for l in text.splitlines()]

    return max(map(square_on_decart, combinations(coordinates, 2)))


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve(ri))
