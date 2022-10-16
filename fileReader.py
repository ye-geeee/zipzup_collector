import csv
from nis import match
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


def readCsv(fileName):
    fileName = decode(fileName)

    cols = pd.read_csv(fileName, nrows=1)
    cols = cols.columns.tolist()
    cols_idx = cols[:len(cols) - 3]
    del cols_idx[2:4]

    data = pd.read_csv(fileName, usecols=cols_idx)
    cols_name = ['dist_origin', 'bunji', 'building', 'area', 'date_contract',
                 'day_contract', 'price', 'floor', 'year_build', 'dist_road']
    data.columns = cols_name

    return data
