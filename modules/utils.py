from pickle import load as pik
from json import dumps, load


def unpickle():
    """Unpickle the bot token"""
    with open('token.pickle', 'rb') as file:
        token = pik(file)
    return token


def bkp(backup: dict) -> None:
    with open('data/backup.json', 'w+') as back_up:
        bcp = dumps(backup, indent=4)
        back_up.write(bcp)


def restore() -> dict:
    with open('data/backup.json', 'r') as backup:
        register = load(backup)
    return register
