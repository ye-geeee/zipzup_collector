#!/usr/bin/env python3

from cmath import nan
from nis import match
import sys
from fileReader import readCsv

if __name__ == '__main__':
    data = readCsv(sys.argv[1])
    print(data)
