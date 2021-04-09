#!/usr/bin/env python3

import itertools
import string

LETTERS = list(string.ascii_letters)

def combinations():
    for L in range(0, len(LETTERS)+1):
        for subset in itertools.combinations(LETTERS, L):
            yield "".join(subset)

if __name__ == '__main__':
        for combination in combinations():
            print(combination)
