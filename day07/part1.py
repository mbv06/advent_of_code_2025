from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def process_manifold(matrix) -> int:
    beams = [matrix[0].index("S")]
    splits = 0
    for i, n in enumerate(matrix[1:]):
        new_beams = set()
        for c in beams:
            if n[c] == "^":
                splits += 1
                new_beams.add(c - 1)
                new_beams.add(c + 1)
            else:
                new_beams.add(c)

        beams = new_beams

    return splits


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def to_matrix(mi: str):
    return [list(line) for line in mi.splitlines() if line]


def process_tachyon(diagram: str):
    matrix = to_matrix(diagram)
    return process_manifold(matrix)


if __name__ == '__main__':
    ri = read_input()
    print(process_tachyon(ri))
