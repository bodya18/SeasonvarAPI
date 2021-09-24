from models.requests.episodes import GetEpisodeBySeasonId
from flask import Blueprint

series_route = Blueprint('series_route', __name__)


@series_route.route('/api/series/<int:seazonId>', methods=["GET"])
def getSeazon(seazonId):
    return GetEpisodeBySeasonId(seazonId)