from operator import and_
from models.tables import seazons, CONNECTION
import json


class Seazons:

    def GetSeazonById(id):
        result = seazons.select().where(seazons.c.id == str(id))
        return CONNECTION.execute(result).one()

    def getSeazonsBySerialId(serialId):
        result = seazons.select().where(seazons.c.serialId == serialId)
        data = CONNECTION.execute(result).all()
        for i, res in enumerate(data):
            data[i] = res._asdict()
        return json.dumps(data)

    def GetSeazonByTitle_SerialId(title, serialId):
        result = seazons.select().where(
            and_(
                seazons.c.title == str(title),
                seazons.c.serialId == str(serialId)
            )
        )
        return CONNECTION.execute(result).all()

    def InsertSeazon(title, description, number, serialId, link):
        ins = seazons.insert().values(title=title, description=description,
                                      number=number, serialId=serialId, link=link)
        result = CONNECTION.execute(ins)
        return result.lastrowid
