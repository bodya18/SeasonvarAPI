import json
from sqlalchemy.sql.expression import func, select
from models.tables import serials, CONNECTION


def GetAllSerials():
    result = serials.select()
    results = CONNECTION.execute(result).fetchall()
    for i, res in enumerate(results):
        results[i] = {'id':res[0], 'title': res[1]}
    return json.dumps(results)


def GetSerialById(id):
    result = serials.select().where(serials.c.id == str(id))
    data = CONNECTION.execute(result).fetchone()
    return json.dumps({"id":data[0], "title": data[1]})


def GetSerialsByTitle(title):
    result = serials.select().where(serials.c.title == str(title))
    data = CONNECTION.execute(result).fetchone()
    return json.dumps({"id":data[0], "title": data[1]})


def InsertSerial(title):
    ins = serials.insert().values(title = title) 
    result = CONNECTION.execute(ins)
    return result.lastrowid


def GetRandomSerials(count):
    result = select(serials).order_by(func.rand()).limit(count)
    results = CONNECTION.execute(result).fetchall()
    for i, res in enumerate(results):
        results[i] = {'id':res[0], 'title': res[1]}
    return json.dumps(results)