import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

INPUT_FILE = Path(__file__).parent / "input.txt"


def calculate_position(rotations, start=50):
    curr_p = start
    key = 0
    logger.info(f"The dial starts by pointing at {start}\n")
    for r in rotations:
        start_p = curr_p
        val = int(r[1:])
        if r[0] == "R":
            pos = curr_p + val
        else:
            pos = curr_p - val

        curr_p = pos % 100

        # calculate rotations
        zeroed = abs(pos // 100)
        if r[0] == "L":
            if start_p == 0:  # 0 and L1 = -1 - // wasn't on zero
                zeroed -= 1
            elif curr_p == 0:  # 50 and L250 = -200
                zeroed += 1

        if zeroed == 0:
            logger.info(f"The dial is rotated {r} to point at {curr_p}")
        else:
            key += zeroed
            logger.info(
                f"The dial is rotated {r} to point at {curr_p}; during this rotation, it points at 0 - {zeroed} times)")
    return key


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read().split("\n")
    return res


if __name__ == '__main__':
    rs = read_input()
    result = calculate_position(rs)
    print(f"The key is {result}")
