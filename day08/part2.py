from itertools import combinations
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # path compensation
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # smaller to bigger
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def dist2(p1: list[int], p2: list[int]) -> int:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return dx * dx + dy * dy + dz * dz


def solve_junctions(text: str):
    lines = [l for l in text.splitlines() if l.strip()]
    points = [list(map(int, l.split(","))) for l in lines]

    n = len(points)

    pairs = sorted(combinations(range(n), 2), key=lambda ij: dist2(points[ij[0]], points[ij[1]]))

    dsu = DSU(n)
    comps = n
    for u, v in pairs:
        if dsu.union(u, v):
            comps -= 1
            if comps == 1:
                # first
                x1 = points[u][0]
                x2 = points[v][0]
                return x1 * x2

    return None


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve_junctions(ri))
