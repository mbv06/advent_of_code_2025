from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve(text: str) -> int:
    *blocks, trees =  text.split("\n\n")
    present_sizes = [b[3:].count("#") for b in blocks]
    variants_size = len(present_sizes)

    amount = 0
    for t in trees.splitlines():
        x, y, *table = (int(x) for x in t.replace("x", ' ').replace(":", '').split())
        if x*y < sum(present_sizes[i] * j for i, j in enumerate(table)):
            continue
        elif variants_size <= (x // 3 * y // 3):
            amount += 1
        else:
            print(f"Fix me {x}x{y} {table}")

    print("Well some joke...")

    return amount


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve(ri))
