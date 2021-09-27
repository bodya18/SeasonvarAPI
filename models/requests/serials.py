import json
from sqlalchemy.sql.expression import func, select
from models.tables import serials, CONNECTION


class Serials:

    def GetAllSerials():
        result = serials.select()
        results = CONNECTION.execute(result).all()
        for i, res in enumerate(results):
            results[i] = res._asdict()
        return results

    def GetSerialById(id):
        result = serials.select().where(serials.c.id == str(id))
        data = CONNECTION.execute(result).one()._asdict()
        return data

    def GetSerialsByTitle(title):
        result = serials.select().where(serials.c.title == str(title))
        data = CONNECTION.execute(result).one()._asdict()
        return data

    def InsertSerial(title):
        ins = serials.insert().values(title=title)
        result = CONNECTION.execute(ins)
        return result.lastrowid

    def GetRandomSerials(count):
        result = select(serials).order_by(func.rand()).limit(count)
        results = CONNECTION.execute(result).all()
        for i, res in enumerate(results):
            results[i] = res._asdict()
        return results
