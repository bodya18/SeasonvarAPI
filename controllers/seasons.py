from models.requests.seasons import Seasons
from flask import Blueprint

seasons_route = Blueprint('seasons_route', __name__)


@seasons_route.route('/api/seasons/<int:serialId>', methods=["GET"])
def getSeason(serialId):
    return Seasons.getSeasonsBySerialId(serialId)


@seasons_route.route('/api/seasons/get/<int:id>', methods=["GET"])
def getSeasonById(id):
    return Seasons.GetSeasonById(id)