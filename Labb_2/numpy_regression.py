#!/usr/bin/env python3

# !DISCLAIMER!
# Do NOT submit this code as your own.
# Submissions will be checked for plagiarism.
# Offenders will not be able to pass the course.

import sys

from os import EX_OSERR as EXIT_FAILURE
from os import EX_OK as EXIT_SUCCESS
from os import _exit

sys.dont_write_bytecode = True

import numpy as np  # noqa: E402
from matplotlib import pyplot as plt  # noqa: E402


def usage(arg0) -> int:
    print(f'Usage: {arg0} <file> <degree>')
    return EXIT_FAILURE


def powers(lst: list, a: int, b: int) -> np.ndarray:
    return np.array([[base**i for i in range(a, b+1)] for base in lst])


def poly(a: list[float], x: float) -> float:
    return sum([a[r]*pow(x,r) for r in range(len(a))])


def regression(x: list, y: list, n: int) -> np.ndarray:
    xp = powers(x, 0, n)
    yp = powers(y, 1, 1)
    xpt = xp.transpose()

    a = np.matmul(np.linalg.inv(np.matmul(xpt, xp)), np.matmul(xpt, yp))
    a = a[:, 0]

    return a


def main(argc: int, argv: list[str]) -> int:
    arg0 = argv.pop(0)
    argc -= 1

    if argc < 2:
        return usage(arg0)

    n = int(argv[1])
    m = np.transpose(np.loadtxt(argv[0]))

    x = m[0]
    y = m[1]

    minx = min(x)
    maxx = max(x)

    r = regression(x, y, n).tolist()

    step = 2/10
    nstep = int((maxx-minx) / step)

    plt.plot(x, y, 'ro')

    x = np.linspace(x[0], x[-1], abs(nstep)).tolist()
    y = [poly(r, f) for f in x]

    plt.plot(x, y)
    try:
        plt.show()
    except KeyboardInterrupt:
        pass
    finally:
        return EXIT_SUCCESS


if __name__ == "__main__":
    try:
        sys.exit(main(len(sys.argv), sys.argv))
    except Exception as err:
        print(err)
        _exit(EXIT_FAILURE)
