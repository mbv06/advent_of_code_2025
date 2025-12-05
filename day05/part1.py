from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


class Range:
    start: int
    end: int

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, n: int) -> bool:
        return self.start <= n < self.end


def process_ranges(lines: str) -> list[Range]:
    fresh_ranges = []
    for l in lines.splitlines():
        start, end = l.split("-")
        fresh_ranges.append(Range(int(start), int(end) + 1))
    return fresh_ranges


def process_database(diagram):
    fresh_amount = 0
    range_lines, id_lines = diagram.split("\n\n")
    fresh_fruits = process_ranges(range_lines)
    for fruit_id in map(int, id_lines.splitlines()):
        if any(fruit_id in ff for ff in fresh_fruits):
            fresh_amount += 1

    return fresh_amount


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(process_database(ri))
