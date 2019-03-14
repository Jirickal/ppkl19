#!/usr/bin/env python3

import sys
import re

print(sys.argv)
pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        if re.search(pattern, line):
            print(line, end="")