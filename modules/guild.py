import codecs
from subprocess import Popen, PIPE
from json import load
from typing import List
from modules.player import Player
import pathlib
from datetime import datetime


def get_id(ally: str) -> int:
    """
    read the player .json file and get this player guild id
    :param ally:
    :return:
    """

    if not pathlib.Path('data/player' + f'{str(ally)}.json').exists():

        player = "coreapi get http://swgoh.gg/api/player/" + str(ally) + "/"
        process = Popen(player.split(), stdout=PIPE)
        output, error = process.communicate()
        with open('data/player' + f'{str(ally)}.json', "w+") as player:
            player.write(str(output.decode('utf-8')))

    else:

        player = pathlib.Path('data/player' + f'{str(ally)}.json')
        if datetime.fromtimestamp(player.stat().st_mtime) != datetime.today():

            player = "coreapi get http://swgoh.gg/api/player/" + str(ally) + "/"
            process = Popen(player.split(), stdout=PIPE)
            output, error = process.communicate()
            with open('data/player' + f'{str(ally)}.json', "w+") as player:
                player.write(str(codecs.decode(output, 'utf-8-sig')))

    with open('data/player' + f'{str(ally)}.json', 'r') as ply:
        player = load(ply)

        for i in player['data']:
            if i == 'guild_id':
                guild_id: int = player['data'][i]

    return guild_id


class Guild:

    def __init__(self, ally: str) -> None:
        self.__id: int = get_id(ally)
        self.__players: List[Player] = self.get_players()
        self.__n_players: int = len(self.players)
        self.__guild_name: str = self.get_guild_name()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def players(self) -> List:
        return self.__players

    @property
    def n_players(self) -> int:
        return self.__n_players

    @property
    def guild_name(self) -> str:
        return self.__guild_name

    def get_guild_name(self) -> str:
        """
        Seek for guild name in the guild file
        :return:
        """
        with open('data/guild' + f'{str(self.id)}.json', 'r') as file:
            guild = load(file)

        for i in guild['data']:

            if i == 'name':
                return guild['data'][i]

            else:
                return 'DEU BO'

    def get_guild_data(self) -> None:
        """
        write the guild data in a .json file
        :return:
        """

        guild = "coreapi get http://swgoh.gg/api/guild/" + str(self.id) + "/"
        process = Popen(guild.split(), stdout=PIPE)
        output, error = process.communicate()

        with open('data/guild' + f'{str(self.id)}.json', "w+") as player:
            player.write(str(output.decode('utf-8')))

    def get_players(self) -> List:

        if not pathlib.Path('data/guild' + f'{str(self.id)}.json').exists():

            Guild.get_guild_data(self)

        else:

            guild = pathlib.Path('data/guild' + f'{str(self.id)}.json')
            if datetime.fromtimestamp(guild.stat().st_mtime) != datetime.today():

                Guild.get_guild_data(self)

        with open('data/guild' + f'{str(self.id)}.json', 'r') as file:
            guild = load(file)

        players = []
        for i in guild['players']:
            for k in i['data']:

                if k == 'name':
                    a = Player(i['data']['ally_code'])
                    players.append(a)

        return players

    def gq(self) -> str:
        """
        Calculate the guild quality
        :return:
        """
        guild = self.players
        guild_tq = []
        guild_tq_av = sum(i.tq for i in guild) / self.n_players
        guild_gq_av = sum(i.gq for i in guild) / self.n_players
        guild_mq_av = sum(i.mq for i in guild) / self.n_players
        for player in guild:
            guild_tq.append(player.tq)
        guild_tq.sort(key=float, reverse=True)
        gq_p1: str = '''|    Nick    |   MQ   |   GQ   |   TQ   |'''
        for i in guild_tq:
            for player in guild:

                if player.tq == i:

                    if len(player.nick) > 10:
                        gq_p1 += f'''\n| {player.nick[0:7] + '...'} '''

                    else:
                        gq_p1 += f'''\n| {player.nick + (' ' * (10 - len(player.nick)))} '''

                    if player.mq >= 100:
                        gq_p1 += f'''| {player.mq:.2f} '''

                    else:
                        gq_p1 += f'''| {player.mq:.2f}  '''

                    if player.gq >= 100:
                        gq_p1 += f'''| {player.gq:.2f} '''

                    else:
                        gq_p1 += f'''| {player.gq:.2f}  '''

                    if player.tq >= 100:
                        gq_p1 += f'''| {player.tq:.2f} |'''

                    else:
                        gq_p1 += f'''| {player.tq:.2f}  |'''

        gq_p1 += f'''\n\nNº of players: {self.n_players}\nMQ Average: {guild_mq_av:.2f}'''
        gq_p1 += f'''\nGQ Average: {guild_gq_av:.2f}'''
        gq_p1 += f'''\nTQ Average: {guild_tq_av:.2f}'''

        return gq_p1
