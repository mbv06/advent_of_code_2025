from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def is_invalid(password):
    pass_len = len(password)
    half_len = pass_len // 2
    s = set(password)
    slen = len(s)

    step = slen  # first step cannot be lower than amount of unique digits
    start, end = step, step * 2
    seq = password[:step]
    while step <= half_len:
        step = end - start
        if seq == password[start:end]:
            if end == pass_len:
                return True
            start += step
            end += step
        else:
            step += 1
            seq = password[:step]
            start, end = step, step * 2

    return False


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
