from operator import and_
from models.tables import episodes, voices, CONNECTION
from sqlalchemy.sql.expression import select, text
import json

class Series:

    def GetEpisodeById(id):
        result = episodes.select().where(episodes.c.id == id)
        return CONNECTION.execute(result).one()._asdict()

    def GetEpisodeBySeasonId(seasonId):
        result = select([text("episodes.*, voices.voice")]).where(
            and_(
                episodes.c.voiceId == voices.c.id,
                episodes.c.seazonId == seasonId
            )
        )
        data = CONNECTION.execute(result).all()
        for i, res in enumerate(data):
            data[i] = res._asdict()
        return json.dumps(data)
