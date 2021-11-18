from models.tables import seasons, CONNECTION


class Seasons:

    def GetSeasonById(id):
        result = seasons.select().where(seasons.c.id == id)
        data = CONNECTION.execute(result).one()._asdict()
        return data

    def getSeasonsBySerialId(serialId):
        result = seasons.select().where(seasons.c.serialId == serialId)
        data = CONNECTION.execute(result).all()
        for i, res in enumerate(data):
            data[i] = res._asdict()
        return data

    def InsertSeason(title, description, number, serialId, link):
        ins = seasons.insert().values(title=title, description=description,
                                      number=number, serialId=serialId, link=link)
        result = CONNECTION.execute(ins)
        return result.lastrowid

    def GetLastSeason(serialId):
        result = seasons.select().where(seasons.c.serialId == serialId)
        data = CONNECTION.execute(result).all()
        if data == []:
            return None
        data = data[-1]._asdict()
        return data
