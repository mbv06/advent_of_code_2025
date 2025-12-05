from pathlib import Path
from typing import Iterable

INPUT_FILE = Path(__file__).parent / "input.txt"


class Range:
    start: int
    end: int

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, n: int) -> bool:
        return self.start <= n < self.end

    def __len__(self) -> int:
        return self.end - self.start

def merge_ranges(ranges: list[Range]) -> list[Range]:
    if not ranges:
        return []

    ranges = sorted(ranges, key=lambda x: x.start)
    merged: list[Range] = [ranges[0]]

    for r in ranges[1:]:
        last = merged[-1]

        if r.start <= last.end:
            last.end = max(last.end, r.end)
        else:
            merged.append(r)

    return merged

def process_ranges(lines):
    fresh_ranges = []
    for l in lines.splitlines():
        start, end = l.split("-")
        fresh_ranges.append(Range(int(start), int(end) + 1))
    return fresh_ranges


def process_database(diagram):
    range_lines, id_lines = diagram.split("\n\n")
    fresh_fruits = process_ranges(range_lines)
    merged_fruits = merge_ranges(fresh_fruits)
    return sum(len(ff) for ff in merged_fruits)


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(process_database(ri))
