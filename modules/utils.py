import os
from pickle import load as pik
from sqlalchemy import create_engine
from pandas import DataFrame
import psycopg2


def unpickle():
    """Unpickle the bot token"""
    with open('token.pickle', 'rb') as file:
        token = pik(file)
    return token


def bkp(backup: list) -> None:
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    engine = create_engine(uri, echo=False)
    d = {'discord_id': [backup[0]], 'ally': [backup[1]]}
    df = DataFrame(data=d)
    df.to_sql('registry', con=engine, if_exists='append')


def restore() -> dict:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor()
    cur.execute('select * from registry')
    recset = cur.fetchall()
    registry = {}
    for i in range(len(recset)):
        ally = recset[i][2].removeprefix('{').removesuffix('}')
        dict = {recset[i][1]: ally.split(',')}
        registry.update(dict)
    con.close()
    return registry
