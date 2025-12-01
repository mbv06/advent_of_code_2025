import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

INPUT_FILE = Path(__file__).parent / "input.txt"


def calculate_position(rotations, start=50):
    logger.info(f"The dial starts by pointing at {start}\n")
    pos = start
    key = 0
    for r in rotations:
        val = int(r[1:])
        if r[0] == "R":
            pos += val
        else:
            pos -= val

        pos = pos % 100
        logger.info(f"The dial is rotated {r} to pint at {pos}")

        if pos == 0:
            key += 1
    return key


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read().split("\n")
    return res


if __name__ == '__main__':
    rs = read_input()
    result = calculate_position(rs)
    print(f"The key is {result}")
