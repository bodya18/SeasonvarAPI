from sqlalchemy.sql.expression import func, select
from models.tables import serials, CONNECTION


class Serials:

    def GetAllSerials():
        result = serials.select().order_by('id')
        results = CONNECTION.execute(result).all()
        for i, res in enumerate(results):
            results[i] = res._asdict()
        return results

    def GetSerialById(id):
        result = serials.select().where(serials.c.id == str(id))
        data = CONNECTION.execute(result).one()._asdict()
        return data

    def GetRandomSerials(count):
        result = select(serials).order_by(func.rand()).limit(count)
        results = CONNECTION.execute(result).all()
        for i, res in enumerate(results):
            results[i] = res._asdict()
        return results


    def Search(search):
        result = select(serials).where(serials.c.title.ilike(f'%{search}%'))
        results = CONNECTION.execute(result).all()
        for i, res in enumerate(results):
            results[i] = res._asdict()
        return results