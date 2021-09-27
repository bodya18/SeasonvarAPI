from models.requests.series import Series
from flask import Blueprint

series_route = Blueprint('series_route', __name__)


@series_route.route('/api/series/<int:seasonId>', methods=["GET"])
def getSeason(seasonId):
    return Series.GetEpisodeBySeasonId(seasonId)