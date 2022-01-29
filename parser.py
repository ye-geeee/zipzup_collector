#!/usr/bin/env python3

from cmath import nan
import csv
from nis import match
import sys
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine

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
    cols = pd.read_csv(fileName, nrows = 1)
    cols = cols.columns.tolist()
    cols_to_use = cols[:len(cols) - 3]

    data = pd.read_csv(fileName, usecols=cols_to_use)
    return data

def preProcess(data):
    data.columns = ['addr_join', 'bunji', 'bonbun', 'bubun', 'apt_name', 'area', 'date', 'day', 'price', 'floor', 'year_build', 'addr_road']

    addrStrList = []
    doList = []
    siList = []
    gunList = []
    guList = []
    dongList = []
    eupList = []
    myeonList = []
    riList = []

    for addrStr in data.addr_join:
        addrs = addrStr.split(" ")

        if addrs[1].endswith('구'):
            addr = addrs[1]
            addrs[1] = addr[:2] + '시'
            addrs.append(addr[2:])
        
        do = ''
        si = ''
        gun = ''
        gu = ''
        dong = ''
        eup = ''
        myeon = ''
        ri = ''

        for addr in addrs:
            if addr.endswith('도'):
                do = addr
            elif addr.endswith('시'):
                si = addr
            elif addr.endswith('군'):
                gun = addr
            elif addr.endswith('구'):
                gu = addr
            elif addr.endswith('동'):
                dong = addr
            elif addr.endswith('읍'):
                eup = addr
            elif addr.endswith('면'):
                myeon = addr
            elif addr.endswith('리'):
                ri = addr

        addrStrList.append(' '.join(addrs))
        doList.append(do)
        siList.append(si)
        gunList.append(gun)
        guList.append(gu)
        dongList.append(dong)
        eupList.append(eup)
        myeonList.append(myeon)
        riList.append(ri)

    data.addr_join = addrStrList
    data['do'] = doList
    data['si'] = siList
    data['gun'] = gunList
    data['gu'] = guList
    data['dong'] = dongList
    data['eup'] = eupList
    data['myeon'] = myeonList
    data['ri'] = riList

    data['year'] = data.date // 100
    data['month'] = data.date % 100
    data['date'] = data.date * 100 + data.day

    data = data[['addr_join', 'bunji', 'bonbun', 'bubun', 'addr_road', 'do', 'si', 'gun', 'gu', 'dong', 'eup', 'myeon', 'ri', \
        'apt_name', 'area', 'date', 'year', 'month', 'day', 'price', 'floor', 'year_build']]

    return data

def updateDb(data):
    # Use your database address and password
    # db_connection_str = 'mysql+pymysql://[db유저이름]:[db password]@[host address]/[db name]'
    db_connection_str = 'mysql+pymysql://root:test@localhost/test'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()

    data.to_sql(name="test", con=db_connection, if_exists='append')

if __name__ == '__main__':
    fileName = decode(sys.argv[1])
    data = readCsv(fileName)
    data = preProcess(data)
    updateDb(data)
