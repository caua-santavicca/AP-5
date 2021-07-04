from subprocess import Popen, PIPE
from json import load
from modules.mods import Mods
from modules.character import Character
import pathlib
from datetime import datetime


def get_data(allycode) -> None:
    """
    Fetch data of a player using the player ally code and save the data in a json file
    """
    player = "coreapi get http://swgoh.gg/api/player/" + str(allycode) + "/"
    process = Popen(player.split(), stdout=PIPE)
    output, error = process.communicate()
    with open(('data/player' + f'{str(allycode)}.json'), 'w') as player:
        player.write(str(output.decode('utf-8')))

    encoding = 'utf-8'
    mods = "coreapi get http://swgoh.gg/api/players/" + str(allycode) + "/mods/"
    process = Popen(mods.split(), stdout=PIPE)
    output, error = process.communicate()
    with open(('data/mods' + f'{str(allycode)}.json'), 'w') as mds:
        mds.write(str(output, encoding))


def get_mq(mods: list, squad_pg: int) -> float:
    """
    Calculate de mod quality of a player, by sorting the player mods by groups and multiplying the amount of mods in
    if group by the group value, then adds oll the groups and divide it by (player squad gp / 1_000_000)
    :param :
    :return: mod_q
    """
    data = mods
    squad_gp: int = squad_pg
    mod: float = sum(
        [len([i for i in data if i.speed >= 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                                    or i.primary == 'Potency'
                                                    or i.primary == 'Tenacity'
                                                    or (i.primary == 'Offense' and i.slot == 'Square')
                                                    or i.primary == 'Critical Avoidance'
                                                    or (i.primary == 'Defense'
                                                        and i.slot == 'Diamond'))
              and i.mod_set == 'Health']) * 0.9,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                                    or i.primary == 'Potency'
                                                    or i.primary == 'Tenacity'
                                                    or (i.primary == 'Offense' and i.slot == 'Square')
                                                    or i.primary == 'Critical Avoidance'
                                                    or (i.primary == 'Defense'
                                                        and i.slot == 'Diamond'))
              and (i.mod_set == 'Speed' or i.mod_set == 'Offense'
                   or i.mod_set == 'Critical Damage')]) * 1.2,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                                    or i.primary == 'Potency'
                                                    or i.primary == 'Tenacity'
                                                    or (i.primary == 'Offense' and i.slot == 'Square')
                                                    or i.primary == 'Critical Avoidance'
                                                    or (i.primary == 'Defense'
                                                        and i.slot == 'Diamond'))
              and (i.mod_set == 'Tenacity' or i.mod_set == 'Potency')]),
         len([i for i in data if i.speed >= 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                                    or i.primary == 'Potency'
                                                    or i.primary == 'Tenacity'
                                                    or (i.primary == 'Offense' and i.slot == 'Square')
                                                    or i.primary == 'Critical Avoidance'
                                                    or (i.primary == 'Defense'
                                                        and i.slot == 'Diamond'))
              and i.mod_set == 'Critical Chance']) * 1.1,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                                    or i.primary == 'Potency'
                                                    or i.primary == 'Tenacity'
                                                    or (i.primary == 'Offense' and i.slot == 'Square')
                                                    or i.primary == 'Critical Avoidance'
                                                    or (i.primary == 'Defense'
                                                        and i.slot == 'Diamond'))
              and i.mod_set == 'Defense']) * 0.8,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Damage'
                                                    or (i.primary == 'Offense' and i.slot != 'Square')
                                                    and i.mod_set == 'Health')]) * 1.1,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Damage'
                                                    or (i.primary == 'Offense' and i.slot != 'Square')
                                                    and (i.mod_set == 'Speed'
                                                         or i.mod_set == 'Critical Damage'
                                                         or i.mod_set == 'Offense'))]) * 1.4,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Damage'
                                                    or (i.primary == 'Offense' and i.slot != 'Square')
                                                    and (i.mod_set == 'Tenacity'
                                                         or i.mod_set == 'Potency'))]) * 1.2,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Damage'
                                                    or (i.primary == 'Offense' and i.slot != 'Square')
                                                    and i.mod_set == 'Critical Chance')]) * 1.3,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Damage'
                                                    or (i.primary == 'Offense' and i.slot != 'Square')
                                                    and i.mod_set == 'Defense')]),
         len([i for i in data if i.speed >= 25 and (i.primary == 'Defense'
                                                    and i.mod_set == 'Speed'
                                                    or i.mod_set == 'Offense'
                                                    or i.mod_set == 'Critical Damage')]),
         len([i for i in data if i.speed >= 25 and (i.primary == 'Defense'
                                                    and i.mod_set == 'Defense')]) * 0.6,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Defense'
                                                    and i.mod_set == 'Health')]) * 0.7,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Defense'
                                                    and i.mod_set == 'Tenacity'
                                                    or i.mod_set == 'Potency')]) * 0.8,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Defense'
                                                    and i.mod_set == 'Critical Chance')]) * 0.9,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Chance'
                                                    and i.mod_set == 'Speed'
                                                    or i.mod_set == 'Offense'
                                                    or i.mod_set == 'Critical Damage')]) * 1.1,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Chance'
                                                    and i.mod_set == 'Defense')]) * 0.7,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Chance'
                                                    and i.mod_set == 'Health')]) * 0.8,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Chance'
                                                    and i.mod_set == 'Tenacity'
                                                    or i.mod_set == 'Potency')]) * 0.9,
         len([i for i in data if i.speed >= 25 and (i.primary == 'Critical Chance'
                                                    and i.mod_set == 'Critical Chance')]),
         len([i for i in data if
              20 <= i.speed < 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Health']) * 0.7,
         len([i for i in data if
              20 <= i.speed < 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and (i.mod_set == 'Speed' or i.mod_set == 'Offense' or i.mod_set == 'Critical Damage')]),
         len([i for i in data if
              20 <= i.speed < 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and (i.mod_set == 'Tenacity' or i.mod_set == 'Potency')]) * 0.8,
         len([i for i in data if
              20 <= i.speed < 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Critical Chance']) * 0.9,
         len([i for i in data if
              20 <= i.speed < 25 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Defense']) * 0.6,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Health')]) * 0.9,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and (i.mod_set == 'Speed'
                                                              or i.mod_set == 'Critical Damage'
                                                              or i.mod_set == 'Offense'))]) * 1.2,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and (i.mod_set == 'Tenacity'
                                                              or i.mod_set == 'Potency'))]),
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Critical Chance')]) * 1.1,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Defense')]) * 0.8,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Speed'
                                                         or i.mod_set == 'Offense'
                                                         or i.mod_set == 'Critical Damage')]) * 0.8,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Defense')]) * 0.4,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Health')]) * 0.5,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Tenacity'
                                                         or i.mod_set == 'Potency')]) * 0.6,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Critical Chance')]) * 0.7,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Speed'
                                                         or i.mod_set == 'Offense'
                                                         or i.mod_set == 'Critical Damage')]) * 0.9,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Defense')]) * 0.5,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Health')]) * 0.6,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Tenacity'
                                                         or i.mod_set == 'Potency')]) * 0.7,
         len([i for i in data if 20 <= i.speed < 25 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Critical Chance')]) * 0.8,
         len([i for i in data if
              15 <= i.speed < 20 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Health']) * 0.5,
         len([i for i in data if
              15 <= i.speed < 20 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and (i.mod_set == 'Speed' or i.mod_set == 'Offense'
                   or i.mod_set == 'Critical Damage')]) * 0.8,
         len([i for i in data if
              15 <= i.speed < 20 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and (i.mod_set == 'Tenacity' or i.mod_set == 'Potency')]) * 0.6,
         len([i for i in data if
              15 <= i.speed < 20 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Critical Chance']) * 0.7,
         len([i for i in data if
              15 <= i.speed < 20 and (i.primary == 'Health' or i.primary == 'Protection'
                                      or i.primary == 'Potency'
                                      or i.primary == 'Tenacity'
                                      or (i.primary == 'Offense' and i.slot == 'Square')
                                      or i.primary == 'Critical Avoidance'
                                      or (i.primary == 'Defense'
                                          and i.slot == 'Diamond'))
              and i.mod_set == 'Defense']) * 0.4,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Health')]) * 0.7,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and (i.mod_set == 'Speed'
                                                              or i.mod_set == 'Critical Damage'
                                                              or i.mod_set == 'Offense'))]),
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and (i.mod_set == 'Tenacity'
                                                              or i.mod_set == 'Potency'))]) * 0.8,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Critical Chance')]) * 0.9,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Damage'
                                                         or (i.primary == 'Offense'
                                                             and i.slot != 'Square')
                                                         and i.mod_set == 'Defense')]) * 0.6,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Speed'
                                                         or i.mod_set == 'Offense'
                                                         or i.mod_set == 'Critical Damage')]) * 0.6,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Defense')]) * 0.2,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Health')]) * 0.3,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Tenacity'
                                                         or i.mod_set == 'Potency')]) * 0.4,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Defense'
                                                         and i.mod_set == 'Critical Chance')]) * 0.5,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Speed'
                                                         or i.mod_set == 'Offense'
                                                         or i.mod_set == 'Critical Damage')]) * 0.7,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Defense')]) * 0.3,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Health')]) * 0.4,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Tenacity'
                                                         or i.mod_set == 'Potency')]) * 0.5,
         len([i for i in data if 15 <= i.speed < 20 and (i.primary == 'Critical Chance'
                                                         and i.mod_set == 'Critical Chance')]) * 0.6])

    mod_q: float = round(mod / (squad_gp / 1_000_000), 2)

    return mod_q


def sort_data(allycode: str):
    """
    Sort de data obtained with get_data() function and organize the data into player and  mods class objects
    """
    mod_position: dict = {'5': 'Circle',
                          '4': 'Triangle',
                          '1': 'Square',
                          '2': 'Arrow',
                          '6': 'Cross',
                          '3': 'Diamond',
                          }
    set_translate: dict = {'1': 'Health',
                           '3': 'Defense',
                           '5': 'Critical Chance',
                           '6': 'Critical Damage',
                           '8': 'Tenacity',
                           '7': 'Potency',
                           '2': 'Offense',
                           '4': 'Speed',
                           }
    mod_tier: dict = {'1': 'e',
                      '2': 'd',
                      '3': 'c',
                      '4': 'b',
                      '5': 'a',
                      }

    if not pathlib.Path('data/mods' + f'{str(allycode)}.json').exists():

        get_data(allycode)

    else:

        player = pathlib.Path('data/mods' + f'{str(allycode)}.json')
        if datetime.fromtimestamp(player.stat().st_mtime) != datetime.today():

            get_data(allycode)

    with open(('data/mods' + f'{str(allycode)}.json'), 'r') as mds:
        data_mods = load(mds)

    mod_list = []
    for i in data_mods['mods']:
        speed: int = 0
        roll: int = 0
        for j in i['secondary_stats']:

            if j['name'] == 'Speed':

                speed = int(j["display_value"])
                roll = int(j['roll'])
        primary: str = i["primary_stat"]['name']
        dot: int = i["rarity"]
        tier: str = mod_tier[str(i['tier'])]
        slot: str = mod_position[str(i['slot'])]
        mod_set: str = set_translate[str(i['set'])]
        mod_id: str = i['id']
        character: str = i["character"]
        mod_list.append(Mods(speed, primary, dot, tier, slot, mod_set, mod_id, character, roll))

    g13 = 0
    g12 = 0
    with open(('data/player' + f'{str(allycode)}.json'), 'r') as ply:
        player = load(ply)
        char_list: list = []
        for k in player['units']:
            relic = 0

            if k['data']["gear_level"] == 12 or k['data']["gear_level"] == 13:
                relic = 0

                if k['data']['relic_tier'] == 2 and k['data']["gear_level"] == 13:
                    relic = 0

                elif k['data']['relic_tier'] == 3 and k['data']["gear_level"] == 13:
                    relic = 1

                elif k['data']['relic_tier'] == 4 and k['data']["gear_level"] == 13:
                    relic = 2

                elif k['data']['relic_tier'] == 5 and k['data']["gear_level"] == 13:
                    relic = 3

                elif k['data']['relic_tier'] == 6 and k['data']["gear_level"] == 13:
                    relic = 4
                elif k['data']['relic_tier'] == 7 and k['data']["gear_level"] == 13:
                    relic = 5

                elif k['data']['relic_tier'] == 8 and k['data']["gear_level"] == 13:
                    relic = 6

                elif k['data']['relic_tier'] == 9 and k['data']["gear_level"] == 13:
                    relic = 7

                elif k['data']['relic_tier'] == 10 and k['data']["gear_level"] == 13:
                    relic = 8

            name = k['data']["name"]
            gear = k['data']["gear_level"]
            char_list.append(Character(gear, name, relic))

            if k['data']['relic_tier'] > 1 and k['data']["gear_level"] == 13:
                g13 += 1

            if k['data']["gear_level"] == 12:
                g12 += 1

        for i in player['data']:

            if i == 'name':
                nick = player['data'][i]

            if i == "galactic_power":
                pg = player['data'][i]

            if i == "character_galactic_power":
                char_pg = player['data'][i]

            if i == "ship_galactic_power":
                ship_pg = player['data'][i]

        return pg, nick, mod_list, char_pg, ship_pg, g12, g13, char_list


def get_gq(char: list, squad_pg: int) -> float:
    """
    Calculate the player gear quality
    :param char:
    :param squad_pg:
    :return:
    """

    data: list = char
    squad_pg: int = squad_pg
    gear = 0
    for i in data:

        if i.gear == 12:
            gear += 1

        elif i.gear == 13:
            gear += 1.5

            if 1 <= i.relic <= 4:
                gear += 0.2 * i.relic

            elif 5 <= i.relic <= 6:
                gear += 0.2 * i.relic + (0.1 * (i.relic - 4))

            elif 7 <= i.relic <= 8:
                gear += 0.2 * i.relic + (0.2 * (i.relic - 6))

    gq: float = round((gear / (squad_pg / 1_000_000)), 2)

    return gq


class Player:

    def __init__(self, ally: str) -> None:
        self.__ally: str = ally
        data = sort_data(ally)
        self.__pg: int = data[0]
        self.__nick: str = data[1]
        self.__mods: list = data[2]
        self.__char_pg: int = data[3]
        self.__ship_gp: int = data[4]
        self.__g12: int = data[5]
        self.__g13: int = data[6]
        self.__char: list = data[7]
        self.__mq: float = get_mq(self.mods, self.char_pg)
        self.__gq: float = get_gq(self.char, self.char_pg)
        self.__tq: float = self.mq + self.gq

    @property
    def ally(self) -> str:
        return self.__ally

    @property
    def pg(self) -> int:
        return self.__pg

    @property
    def nick(self) -> str:
        return self.__nick

    @property
    def mods(self) -> list:
        return self.__mods

    @property
    def char_pg(self) -> int:
        return self.__char_pg

    @property
    def ship_pg(self) -> int:
        return self.__ship_gp

    @property
    def g12(self) -> int:
        return self.__g12

    @property
    def g13(self) -> int:
        return self.__g13

    @property
    def char(self) -> list:
        return self.__char

    @property
    def mq(self) -> float:
        return self.__mq

    @property
    def gq(self) -> float:
        return self.__gq

    @property
    def tq(self) -> float:
        return self.__tq


if __name__ == "__main__":
    t = Player('387821568')
    print(t.nick)
    print(t.mq)
    print(t.gq)
    print(t.tq)
    print(t.char[0].relic)
    print(t.char[0].name)
