from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def process_manifold(matrix):
    beams = {matrix[0].index("S"): 1}
    beams_amount = 1
    for i, n in enumerate(matrix[1:]):
        new_beams = defaultdict(int)
        for b, amount in beams.items():
            if n[b] != "^":
                new_beams[b] += amount
            else:
                beams_amount += amount
                new_beams[b - 1] += amount
                new_beams[b + 1] += amount
        beams = new_beams

    return beams_amount


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def to_matrix(mi: str):
    return [list(line) for line in mi.splitlines() if line]


def process_tachyon(diagram):
    matrix = to_matrix(diagram)
    return process_manifold(matrix)


if __name__ == '__main__':
    ri = read_input()
    print(process_tachyon(ri))
