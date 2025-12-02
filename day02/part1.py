from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def is_invalid(number):
    length = len(number)
    if length % 2 != 0:
        return False
    len2 = length // 2
    return number[:len2] == number[len2:]


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def process_ranges(id_ranges):
    amount = 0
    for r in id_ranges.split(","):
        start, end = r.split("-")
        for num in range(int(start), int(end) + 1):
            if is_invalid(str(num)):
                amount += num
    return amount


if __name__ == '__main__':
    ri = read_input()
    print(process_ranges(ri))

