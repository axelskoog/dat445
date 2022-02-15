#!/usr/bin/env python3

# !DISCLAIMER!
# Do NOT submit this code as your own. Submissions will be tested for
# plagiarism, and if you are deemed guilty of it, your ability to pass
# this course will be slim.

import sys

from os import EX_OSERR as EXIT_FAILURE
from os import EX_OK as EXIT_SUCCESS
from os import _exit

sys.dont_write_bytecode = True

import matrix as mt  # noqa: E402
from matplotlib import pyplot as plt  # noqa: E402


def usage(arg0) -> int:
    print(f'Usage: {arg0} <file> <degree>')
    return EXIT_FAILURE


def poly(a: list[float], x: float) -> float:
    return sum([a[r]*pow(x,r) for r in range(len(a))])


def regression(x: list, y: list, n: int) -> list[float]:
    xp = mt.powers(x, 0, n)
    yp = mt.powers(y, 1, 1)
    xpt = mt.transpose(xp)

    a = mt.matmul(mt.invert(mt.matmul(xpt, xp)), mt.matmul(xpt, yp))
    a = [r[0] for r in a]

    return a


def main(argc: int, argv: list[str]) -> int:
    arg0 = argv.pop(0)
    argc -= 1

    if argc < 2:
        return usage(arg0)

    n = int(argv[1])
    m = mt.transpose(mt.loadtxt(argv[0]))

    x = m[0]
    y = m[1]

    minx = min(x)
    maxx = max(x)

    r = regression(x, y, n)

    step = 2/10
    nstep = int((maxx-minx) / step)

    plt.plot(x, y, 'ro')

    x = mt.linspace(x[0], x[-1], nstep)
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
