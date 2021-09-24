from operator import and_
from models.tables import episodes, seazons, voices, CONNECTION
from sqlalchemy.sql.expression import select, text
import json

def GetEpisodeById(id):
    result = episodes.select().where(episodes.c.id == str(id))
    return CONNECTION.execute(result).fetchone()

def GetEpisodeBySeasonId(seazonId):
    result = select([text("episodes.*, voices.voice")]).where(
        and_(
            episodes.c.voiceId == voices.c.id,
            episodes.c.seazonId == seazonId
        )
    )
    data = CONNECTION.execute(result).fetchall()
    for i, res in enumerate(data):
        data[i] = {"id": res[0], "title": res[1], "seazonId": res[2], "voiceId": res[3], "number": res[4], "link": res[5], "subtitles": res[6], "voice": res[7]}
    return json.dumps(data)



def GetEpisodeByLink(link):
    result = episodes.select().where(episodes.c.link == str(link))
    return CONNECTION.execute(result).fetchone()


def GetEpisodeByTitle_SeazonId(title, seazonId):
    result = seazons.select().where(
        and_(
            episodes.c.title == str(title),
            episodes.c.seazonId == str(seazonId)
        )
    )
    return CONNECTION.execute(result).fetchall()


def InsertEpisode(title, voiceId, number, seazonId, link, subtitles = ''):
    ins = episodes.insert().values(title = title, voiceId = voiceId, number = number, seazonId = seazonId, link = link, subtitles = subtitles) 
    result = CONNECTION.execute(ins)
    return result.lastrowid