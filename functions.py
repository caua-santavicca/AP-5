from subprocess import Popen, PIPE
from json import load, decoder, dump
# import coreapi

mod_primary = {'health': 55,
               'offence': 48,
               'defense': 49,
               'speed': 5,
               'protection': 56,
               'tenacity': 18,
               'potency': 17,
               'cc': 53,
               'critical chance': 53,
               'critical damage': 16,
               'cd': 16,
               'ca': 54,
               'critical avoidance': 54,
               }

mod_position = {'circle': 5,
                'triangle': 4,
                'square': 1,
                'arrow': 2,
                'cross': 6,
                'plus': 6,
                'diamond': 3,
                }

set_translate = {'health': 1,
                 'defense': 3,
                 'cc': 5,
                 'critical chance': 5,
                 'cd': 6,
                 'critical damage': 6,
                 'tenacity': 8,
                 'potency': 7,
                 'offence': 2,
                 'speed': 4,
                 }

mod_tier = {'e': 1,
            'd': 2,
            'c': 3,
            'b': 4,
            'a': 5,
            }


def get_player(allycode):
    """
    Take a allycode and fetch mods data for that ally code and save the data on a json file
    :param allycode:
    :return:
    """
    url = "coreapi get http://swgoh.gg/api/player/" + str(allycode) + "/"
    process = Popen(url.split(), stdout=PIPE)
    output, error = process.communicate()
    with open('player.json', "w+") as player:
        player.write(str(output.decode('latin-1')))


def get_mods(allycode):
    """
    Take a allycode and fetch mods data for that ally code and save the data on a json file
    :param allycode:
    :return:
    """
    encoding = 'utf-8'
    url = "coreapi get http://swgoh.gg/api/players/" + str(allycode) + "/mods/"
    process = Popen(url.split(), stdout=PIPE)
    output, error = process.communicate()
    with open("mods.json", "w+") as mods:
        mods.write(str(output, encoding))


def mods_speed(allycode):
    """
    Take the file created with get_mods function and sort the mods data by speed
    :param allycode:
    :return:
    """
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as mods:
            data_mods = load(mods)
        for i in data_mods['mods']:
            for j in i['secondary_stats']:
                if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                    a += 1
                elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                    b += 1
                elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                    c += 1
                elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                    d += 1
                elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                    e += 1
            if i["rarity"] == 5:
                f += 1
            if i["rarity"] == 6:
                g += 1
        return a, b, c, d, e, f, g
    except decoder.JSONDecodeError:
        return 'Deu merda!'


def mods_primary_speed(allycode, primary):
    """
    Take the file created with get_mods function and sort the mods data by speed and primary
    :param primary:
    :param allycode:
    :return:
    """
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as json_file:
            data_mods = load(json_file)
        for i in data_mods['mods']:
            if i["primary_stat"]['stat_id'] == mod_primary[primary]:
                if i["primary_stat"]['stat_id'] != 5:
                    for j in i['secondary_stats']:
                        if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                            a += 1
                        elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                            b += 1
                        elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                            c += 1
                        elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                            d += 1
                        elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                            e += 1
                if i["rarity"] == 5:
                    f += 1
                if i["rarity"] == 6:
                    g += 1
        return a, b, c, d, e, f, g
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!'


def mods_set_speed(allycode, mod_set):
    """
    Take the file created with get_mods function and sort the mods data by speed and set
    :param mod_set:
    :param allycode:
    :return:
    """
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as mods:
            data_mods = load(mods)
        for i in data_mods['mods']:
            if i["set"] == set_translate[mod_set]:
                for j in i['secondary_stats']:
                    if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                        a += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                        b += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                        c += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                        d += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                        e += 1
                if i["rarity"] == 5:
                    f += 1
                if i["rarity"] == 6:
                    g += 1
        return a, b, c, d, e, f, g
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!'


def mods_position_speed(allycode, position):
    """
    Take the file created with get_mods function and sort the mods data by speed and set
    :param position:
    :param allycode:
    :return:
    """
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as mods:
            data_mods = load(mods)
        for i in data_mods['mods']:
            if i["slot"] == mod_position[position]:
                for j in i['secondary_stats']:
                    if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                        a += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                        b += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                        c += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                        d += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                        e += 1
                if i["rarity"] == 5:
                    f += 1
                if i["rarity"] == 6:
                    g += 1
        return a, b, c, d, e, f, g
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!'


def mods_position_set_speed(allycode, position, mod_set):
    """
    Take the file created with get_mods function and sort the mods data by speed and set
    :param mod_set:
    :param position:
    :param allycode:
    :return:
    """
    a, b, c, d, e, h = 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as mods:
            data_mods = load(mods)
        for i in data_mods['mods']:
            if i["slot"] == mod_position[position.lower()] and i["set"] == set_translate[mod_set.lower()]:
                h += 1
                for j in i['secondary_stats']:
                    if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                        a += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                        b += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                        c += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                        d += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                        e += 1
        return a, b, c, d, e, h
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!'


def mods_position_primary_set_speed(allycode, position, primary, mod_set):
    """
    Take the file created with get_mods function and sort the mods data by speed and set, position and primary
    :param mod_set:
    :param primary:
    :param position:
    :param allycode:
    :return:
    """
    a, b, c, d, e, h = 0, 0, 0, 0, 0, 0
    try:
        get_mods(allycode)
        with open("mods.json") as mods:
            data_mods = load(mods)
        for i in data_mods['mods']:
            if i["slot"] == mod_position[position] and i["set"] == set_translate[mod_set] \
                    and i["primary_stat"]['stat_id'] == mod_primary[primary]:
                h += 1
                for j in i['secondary_stats']:
                    if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] >= 250_000.0:
                        a += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 200_000.0 <= j['value'] <= 240_000.0:
                        b += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 150_000.0 <= j['value'] <= 190_000.0:
                        c += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and 100_000.0 <= j['value'] <= 140_000.0:
                        d += 1
                    elif (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] <= 90_000.0:
                        e += 1
        return a, b, c, d, e, h
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!'


def get_player_nick(allycode):
    """
    get player nick using get_player function to fetch player data
    :param allycode:
    :return:
    """
    try:
        get_player(allycode)
        with open('player.json') as player:
            player_data = load(player)
        for i in player_data['data']:
            if i == 'name':
                return player_data['data'][i]
    except (decoder.JSONDecodeError, KeyError, TypeError):
        return 'Deu merda!!'


def register(allycode, tag):
    keys = allycode.split()
    a = {tag: keys[1]}
    return a


def backup():
    with open('registers_backup.json', 'w') as backup:
        dump(a, backup)


if __name__ == '__main__':
    #print(mods_speed(387821568))
    #print(mods_set_speed(387821568, 'health'))
    #a = []
    #for i in range(3):
        #a.append(register('a 387821568', str(i)))
    #backup()
    get_mods(387821568)
    with open("mods.json") as mods:
        data_mods = load(mods)
    a = 0
    f = 0
    for i in data_mods['mods']:
        for j in i['secondary_stats']:
            if (j['name'] == 'Speed' or j["stat_id"] == 5) and j['value'] == 140_000.0:
                a += 1
                if i["rarity"] == 5:
                    f += 1
    print(a)
    print(f)
