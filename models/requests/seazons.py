from operator import and_
from models.tables import seazons, CONNECTION
import json

def GetSeazonById(id):
    result = seazons.select().where(seazons.c.id == str(id))
    return CONNECTION.execute(result).fetchall()

def getSeazonsBySerialId(serialId):
    result = seazons.select().where(seazons.c.serialId == serialId)
    data = CONNECTION.execute(result).fetchall()
    for i, res in enumerate(data):
        data[i] = {"id": res[0], "title": res[1], "description": res[2], "number": res[3], "serialId": res[4], "link": res[5], "image": res[6]}
    return json.dumps(data)

def GetSeazonByTitle_SerialId(title, serialId):
    result = seazons.select().where(
        and_(
            seazons.c.title == str(title),
            seazons.c.serialId == str(serialId)
        )
    )
    return CONNECTION.execute(result).fetchall()


def InsertSeazon(title, description, number, serialId, link):
    ins = seazons.insert().values(title = title, description = description, number = number, serialId = serialId, link = link) 
    result = CONNECTION.execute(ins)
    return result.lastrowid