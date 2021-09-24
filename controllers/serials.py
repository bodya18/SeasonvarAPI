from models.requests.serials import GetRandomSerials, GetSerialById
from flask import Blueprint

serials_route = Blueprint('serials_route', __name__)

@serials_route.route('/api/serials/random/<int:count>', methods=["GET"])
def randomSerials(count):
    return GetRandomSerials(count)


@serials_route.route('/api/serials/<int:id>', methods=["GET"])
def getSerial(id):
    return GetSerialById(id)


@serials_route.route('/api/seazons/<int:serialId>', methods=["GET"])
def getSeazonsBySerial(serialId):
    return getSeazonsBySerial(serialId)