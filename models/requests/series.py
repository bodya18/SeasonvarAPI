from operator import and_
from models.tables import episodes, seasons, voices, CONNECTION
from sqlalchemy.sql.expression import select, text
import json


class Series:

    def GetEpisodeById(id):
        result = episodes.select().where(episodes.c.id == str(id))
        return CONNECTION.execute(result).one()

    def GetEpisodeBySeasonId(seasonId):
        result = select([text("episodes.*, voices.voice")]).where(
            and_(
                episodes.c.voiceId == voices.c.id,
                episodes.c.seasonId == seasonId
            )
        )
        data = CONNECTION.execute(result).all()
        for i, res in enumerate(data):
            data[i] = res._asdict()
        return data

    def GetEpisodeByLink(link):
        result = episodes.select().where(episodes.c.link == str(link))
        return CONNECTION.execute(result).one()

    def GetEpisodeByTitle_SeasonId(title, seasonId):
        result = seasons.select().where(
            and_(
                episodes.c.title == str(title),
                episodes.c.seasonId == str(seasonId)
            )
        )
        return CONNECTION.execute(result).all()

    def InsertEpisode(title, voiceId, number, seasonId, link, subtitles=''):
        ins = episodes.insert().values(title=title, voiceId=voiceId, number=number,
                                       seasonId=seasonId, link=link, subtitles=subtitles)
        result = CONNECTION.execute(ins)
        return result.lastrowid
