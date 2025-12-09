from itertools import combinations
from math import prod
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

    def union(self, a: int, b: int):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return  # same head

        # smaller to bigger
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def dist2(p1: list[int], p2: list[int]):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return dx * dx + dy * dy + dz * dz


def solve_junctions(text: str, count: int = 1000) -> int:
    lines = [l for l in text.splitlines() if l.strip()]
    points = [list(map(int, l.split(","))) for l in lines]

    n = len(points)

    pairs = sorted(combinations(range(n), 2), key=lambda ij: dist2(points[ij[0]], points[ij[1]]))

    dsu = DSU(n)

    for u, v in pairs[:count]:
        dsu.union(u, v)

    sizes = sorted((dsu.size[i] for i in range(n) if dsu.parent[i] == i), reverse=True)

    return prod(sizes[:3])


def read_input(input_file=INPUT_FILE):
    with open(input_file) as fi:
        res = fi.read()
    return res


if __name__ == '__main__':
    ri = read_input()
    print(solve_junctions(ri))
