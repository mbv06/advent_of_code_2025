from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def max_joltage(number) -> str:
    maxj, nmaxj = "/", "/"  # ord("/") < ord("0")
    max_element = len(number) - 1
    for i, n in enumerate(number):
        if i != max_element and n > maxj:
            maxj = n
            nmaxj = "0"
        elif n > nmaxj:
            nmaxj = n
    return maxj + nmaxj


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def process_backets(backets):
    amount = 0
    for b in backets.splitlines():
        res = max_joltage(b)
        print(f"{b} => {res}")
        amount += int(res)

    return amount


if __name__ == '__main__':
    ri = read_input()
    print(process_backets(ri))
