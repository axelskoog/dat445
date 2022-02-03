#!/usr/bin/env python3

import sys
import requests

from os import _exit, EX_OSERR as EXIT_FAILURE, EX_OK as EXIT_SUCCESS

sys.dont_write_bytecode = True

import wordfreq as wf  # noqa: E402


def usage(arg0) -> int:
    print(f'Usage: {arg0} <stopfile> <file/url> <limit>')
    return EXIT_FAILURE


def main(argc: int, argv: list):

    arg0 = argv.pop(0)
    argc -= 1

    if argc < 3:
        return usage(arg0)

    try:
        limit = int(argv[2])
    except ValueError:
        # could not type cast to integer
        return usage(arg0)

    frequencies = {}

    # argv[0] is the file containing stop words. see usage().
    with open(argv[0], 'r', encoding="utf-8") as f:
        # build a dictionary instead. hash in constant time.
        stopwords = {line.strip(): True for line in f}

    if "http" in argv[1]:
        with requests.Session().get(argv[1], headers=None, stream=True) as resp:
            r = resp.iter_lines(decode_unicode=True)
            wf.s_countWords(frequencies, wf.s_tokenize(r), stopwords)
    else:
        with open(argv[1], 'r', encoding="utf-8", errors='ignore') as f:
            wf.s_countWords(frequencies, wf.s_tokenize(f), stopwords)

    wf.printTopMost(frequencies, limit)
    return EXIT_SUCCESS


if __name__ == "__main__":
    # crt.o, bring me back from interpreter hell ;-;
    try:
        sys.exit(main(len(sys.argv), sys.argv))
    except Exception as err:
        print(err)
        _exit(EXIT_FAILURE)


