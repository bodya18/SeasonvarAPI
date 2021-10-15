from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, TEXT
from middleware.config import DB_DIALECT, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

engine = create_engine(f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4")
meta = MetaData()

voices = Table(
    'voices', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('voice', String(255), nullable=False, unique=True),
)

serials = Table(
    'serials', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False, unique=True)
)

seasons = Table(
    'seasons', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False),
    Column('description', TEXT, nullable=False),
    Column('number', Integer),
    Column('serialId', Integer, ForeignKey('serials.id')),
    Column('link', String(255)),
    Column('image', String(255), nullable=False),
)

episodes = Table(
    'episodes', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('seazonId', Integer, ForeignKey('seasons.id')),
    Column('voiceId', Integer, ForeignKey('voices.id')),
    Column('number', Integer, nullable=False),
    Column('link', String(255), nullable=False),
    Column('subtitles', String(255))
)

meta.create_all(engine)

CONNECTION = engine.connect()