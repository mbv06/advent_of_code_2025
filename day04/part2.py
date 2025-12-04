from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"

NEIGHBORS_CORD = (-1, 0, 1)
SYMBOL = "@"


def can_forklift(matrix, r, c, rows_max, cols_max):
    cnt = 0
    for dr in NEIGHBORS_CORD:
        for dc in NEIGHBORS_CORD:
            if dr == 0 and dc == 0:
                continue

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows_max and 0 <= nc < cols_max:
                if matrix[nr][nc] == SYMBOL:
                    cnt += 1

            if cnt >= 4:
                return False
    return True


def calculate_accessed_rolls(matrix):
    amount = 0
    rows = len(matrix)
    cols = len(matrix[0])
    changed = True
    while changed:
        changed = False
        for i, n in enumerate(matrix):
            for j, m in filter(lambda x: x[1] == SYMBOL, enumerate(n)):
                if can_forklift(matrix, i, j, rows, cols):
                    matrix[i][j] = "x"
                    changed = True
                    amount += 1
    return amount


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


def to_matrix(mi: str):
    return [list(line) for line in mi.splitlines() if line]


def process_diagram(diagram):
    matrix = to_matrix(diagram)
    return calculate_accessed_rolls(matrix)


if __name__ == '__main__':
    ri = read_input()
    print(process_diagram(ri))
