from models.requests.serials import Serials
from flask import Blueprint

serials_route = Blueprint('serials_route', __name__)

@serials_route.route('/api/serials/random/<int:count>', methods=["GET"])
def randomSerials(count):
    return Serials.GetRandomSerials(count)


@serials_route.route('/api/serials/<int:id>', methods=["GET"])
def getSerial(id):
    return Serials.GetSerialById(id)
