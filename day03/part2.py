from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"

REQ_DIGITS = 12


def max_joltage(number: str, req_digits=12, max_shift=2) -> str:
    elements = ["/"] * req_digits  # ord("/") < ord("0")
    shift = 0
    for r in range(req_digits):
        shifted = 0
        for i, n in enumerate(number[r + shift:r + max_shift + 1]):
            if n > elements[r]:
                elements[r] = n
                shifted = i
        shift += shifted
    return "".join(elements)


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def process_backets(backets):
    amount = 0
    lines = backets.splitlines()
    max_shift = len(lines[0]) - REQ_DIGITS
    for b in lines:
        res = max_joltage(b, REQ_DIGITS, max_shift)
        amount += int(res)

    return amount


if __name__ == '__main__':
    ri = read_input()
    print(process_backets(ri))
