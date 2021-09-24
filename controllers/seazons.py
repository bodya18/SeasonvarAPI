from models.requests.seazons import getSeazonsBySerialId
from flask import Blueprint

seazons_route = Blueprint('seazons_route', __name__)


@seazons_route.route('/api/seazons/<int:serialId>', methods=["GET"])
def getSeazon(serialId):
    return getSeazonsBySerialId(serialId)