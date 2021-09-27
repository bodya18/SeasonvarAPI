import json
from models.requests.seasons import Seasons
from models.requests.serials import Serials
from flask import Blueprint

serials_route = Blueprint('serials_route', __name__)


@serials_route.route('/api/serials/random/<int:count>', methods=["GET"])
def randomSerials(count):
    serials = Serials.GetRandomSerials(count)
    for i, serial in enumerate(serials):
        last_season = Seasons.GetLastSeason(serial['id'])
        serial['last_season'] = last_season
        serials[i] = serial
    return json.dumps(serials)


@serials_route.route('/api/serials/<int:id>', methods=["GET"])
def getSerial(id):
    last_season = Seasons.GetLastSeason(id)
    serial = Serials.GetSerialById(id)
    serial['last_season'] = last_season
    return serial


@serials_route.route('/api/serials', methods=["GET"])
def GetAllSerials():
    serials = Serials.GetAllSerials()
    for i, serial in enumerate(serials):
        last_season = Seasons.GetLastSeason(serial['id'])
        serial['last_season'] = last_season
        serials[i] = serial
    return json.dumps(serials)