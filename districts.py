import pandas as pd
from sqlalchemy import null


from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Districts(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True)
    dist_origin = Column(String)
    dist_join = Column(String)
    sub_dist1 = Column(String)
    sub_dist2 = Column(String)
    sub_dist3 = Column(String)
    sub_dist4 = Column(String)

    def __init__(self, dist_origin, dist_join, sub_dist1, sub_dist2, sub_dist3, sub_dist4):
        self.dist_origin = dist_origin
        self.dist_join = dist_join
        self.sub_dist1 = sub_dist1
        self.sub_dist2 = sub_dist2
        self.sub_dist3 = sub_dist3
        self.sub_dist4 = sub_dist4

    def __repr__(self):
        return "<User('%s')>" % (self.dist_origin)


def generateDistricts(rawInfo: pd.DataFrame):
    distDf = rawInfo.drop_duplicates(subset=['dist_origin'])
    districts = []
    print("There are " + str(distDf.shape.index + " districts info to update")

    for dist in distDf['dist_origin']:
        specificDistrictInfo=getDistricts(dist)
        districts.append(Districts(
            dist,
            ''.join(specificDistrictInfo),
            specificDistrictInfo[0],
            specificDistrictInfo[1],
            specificDistrictInfo[2],
            specificDistrictInfo[3] if len(
                specificDistrictInfo) > 3 else None
        ))
    return districts


def getDistricts(dist: str):
    dists=dist.split(" ")

    if len(dists[1]) > 4:
        dists.insert(2, dists[1][2:])
        dists[1]=dists[1][:2] + '시'

    return dists
