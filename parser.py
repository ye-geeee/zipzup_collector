#!/usr/bin/env python3

import csv
import sys
import pandas as pd

def decode(fileName):
    if fileName.endswith(".csv"):
        fileName = fileName.replace(".csv", "")

    with open(f"{fileName}_utf.csv", "w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        with open(f"{fileName}.csv", "r", encoding="cp949") as f:
            reader = csv.reader(f)
            for i in range(15):
                next(reader)

            for row in reader:
                writer.writerow(row)
    
    return fileName + "_utf.csv"

if __name__ == '__main__':
    fileName = decode(sys.argv[1])
    