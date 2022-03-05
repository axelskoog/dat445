
# !DISCLAIMER!
# Do NOT submit this code as your own.
# Submissions will be checked for plagiarism.
# Offenders will not be able to pass the course.

from typing import Iterable, Generator
import re

rex = re.compile('[A-Za-z]+|[0-9]+|[^A-Za-z0-9\\s]')


# "s_" -> streaming

def s_tokenize(lines: Iterable[str]) -> Generator[str, None, None]:
    for line in lines:
        for token in re.finditer(rex, line):
            yield token.group().lower()


def s_countWords(d: dict[str, int], t: Iterable[str], stop: dict) -> None:
    for token in t:
        if not stop.get(token, False):
            try:
                d[token] = d[token] + 1
            except KeyError:
                d[token] = 1


def printTopMost(freq: dict[str, int], n: int) -> None:
    lst = [(k, v) for k, v in sorted(freq.items(), key=lambda x: -x[1])]
    for word, freq in lst[0:min(n, len(lst))]:
        print("{:<20}{:5}".format(word, freq), sep='')


#
# definitions for test.py
#

def tokenize(lines: Iterable[str]) -> list[str]:
    return [t for t in s_tokenize(lines)]


def countWords(t: Iterable[str], stop: list) -> None:
    d = {}
    s = {w: True for w in stop}
    s_countWords(d, t, s)
    return d
