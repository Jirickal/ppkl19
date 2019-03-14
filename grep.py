#!/usr/bin/env python3
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.
"""


import sys
import re

try:
    pattern, path = sys.argv[1:]
except ValueError as err:
    print(__doc__.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1)
# standard error "neteče rourou"

try:
    with open(path) as file:
        for line in file:
            if re.search(pattern, line):
                print(line, end="")
except FileNotFoundError as err:
    print(__doc__.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1)