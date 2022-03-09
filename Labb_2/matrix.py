
# !DISCLAIMER!
# Do NOT submit this code as your own.
# Submissions will be checked for plagiarism.
# Offenders will not be able to pass the course.

from typing import *
from operator import mul
import sys

sys.dont_write_bytecode = True


def as_int(n: float) -> float | int:
    return int(n) if n.is_integer() else n


def transpose(m: list[list]) -> list[list]:
    return list(map(list, zip(*m)))


def powers(bases: list, a: int, b: int) -> list[list]:
    r = range(a, b+1)
    return [[pow(base, i) for i in r] for base in bases]


def dot(v1: list, v2: list) -> Union[int, float]:
    return sum(map(mul, v1, v2))


def minor(m: list[list], i: int, j: int) -> list[list]:
    return [[e for y,e in enumerate(r) if y != j] for x,r in enumerate(m) if x != i]


def det(a: list[list]) -> Union[int, float]:
    m = len(a)
    n = len(a[0]) if a else 0
    if m == 0 or n == 0:
        raise ValueError("dim(a) == 0")
    if m != n:
        raise ValueError("m != n")
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    r = range(m)
    return sum([((-1)**i) * a[0][i] * det(minor(a, 0, i)) for i in r])


def eye(n: int) -> list[list]:
    ij = range(n)
    return [[int(i == j) for i in ij] for j in ij]


def cofactor(m: list[list]) -> list[list]:
    rowr = range(len(m))
    colr = range(len(m[0]))
    return [[(-1)**(i+j)*det(minor(m, i, j)) for j in colr] for i in rowr]


def adj(m: list[list]) -> list[list]:
    return transpose(cofactor(m))


def matmul(a: list[list], b: list[list]) -> list[list]:
    if a and len(a[0]) == len(b):
        bt = transpose(b)
        return [[dot(row, col) for col in bt] for row in a]
    return []


def scale(a: list[list], s: float) -> list[list]:
    return [[as_int(e*s) for e in r] for r in a]


def invert(M: list[list]) -> list[list]:
    mdet = det(M)
    if mdet:
        return scale(adj(M), 1/mdet)
    else:
        raise ValueError("det(M) is 0")


def loadtxt(filename: str) -> list[list]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [[float(n) for n in line.split()] for line in f]


def linspace(start, stop, n):
    if n < 1:
        return []
    h=(stop-start)/(n-1)
    return [stop] if n == 1 else [start+h*i for i in range(n)]
