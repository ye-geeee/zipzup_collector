#!/usr/bin/env python3

import csv
import sys

if __name__ == '__main__':

    fileName = sys.argv[1]

    if fileName.endswith(".csv"):
        fileName = fileName.replace(".csv", "")

    with open(f"{fileName}_utf.csv", "w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        with open(f"{fileName}.csv", "r", encoding="cp949") as f:
            reader = csv.reader(f)
            for row in reader:
                writer.writerow(row)
