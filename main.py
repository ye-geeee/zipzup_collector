#!/usr/bin/env python3

from dis import dis
from sqlalchemy import create_engine
from cmath import nan
from nis import match
import sys
from fileReader import readCsv
from sqlalchemy.orm import sessionmaker
from districts import District, generateDistricts

engine = create_engine(
    'mysql+pymysql://[db유저이름]:[db password]@[host address]/[db name]')
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    data = readCsv(sys.argv[1])

    session = Session()
    districts = generateDistricts(data[['dist_origin']].copy())
    session.add_all(districts)
    session.commit()
