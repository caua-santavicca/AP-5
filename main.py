import discord
from asyncio import sleep
<<<<<<< HEAD
from keep_alive import keep_alive
from modules.utils import unpickle, bkp, restore
from modules.player import Player
from modules.guild import Guild
from json.decoder import JSONDecodeError
=======
# from keep_alive import keep_alive
import functions
# import coreapi_cli
>>>>>>> main

client = discord.Client()
users: dict = {}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$m'):

        allycode = message.content.split()
        if len(allycode[0]) == 2:

            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:
                player_dt = Player(allycode[1])
                emoji = '👍'
                await message.add_reaction(emoji)
                embed = discord.Embed(title=player_dt.nick + "'s mods", color=0x000000)
                embed.add_field(name=' ======================== ', value=f'''
```fix
Total : {len([i for i in player_dt.mods])}
MQ: {player_dt.mq}
6* Mods: {len([i for i in player_dt.mods if i.dot == 6])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed > 0])}
No speed: {len([i for i in player_dt.mods if i.speed == 0 and i.primary != 'Speed'])}
```========================''', inline=False)
                embed.add_field(name='Info', value='''
Use _$help mq_ to se how the mod quality is calculated
========================''')
                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()

            except IndexError:

                users.update(restore())
                if str(message.author) in users:
                    for i in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][i])
                        emoji = '👍'
                        await message.add_reaction(emoji)
                        embed = discord.Embed(title=player_dt.nick + "'s mods", color=0x000000)
                        embed.add_field(name=' ======================== ', value=f'''
```fix
Total : {len([i for i in player_dt.mods])}
MQ: {player_dt.mq}
6* Mods: {len([i for i in player_dt.mods if i.dot == 6])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed > 0])}
No speed: {len([i for i in player_dt.mods if i.speed == 0 and i.primary != 'Speed'])}
```========================''', inline=False)
                        embed.add_field(name='Info', value='''
                    Use _$help mq_ to se how the mod quality is calculated
                    ========================''')
                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()
                    await bot.delete()
                else:
                    await message.channel.send('Ally code not registered, use $r <allycode> to register')

            except JSONDecodeError:

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$mp'):

        allycode = message.content.split()
        if len(allycode[0]) == 3:

            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:

                player_dt = Player(allycode[1])
                mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                      'Critical Damage',
                                      'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

                embed = discord.Embed(title=player_dt.nick, color=0x000000)
                for i in mods_primary:
                    if i.lower() == 'speed':
                        emoji = '👍'
                        await message.add_reaction(emoji)
                        embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == 'Speed'])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == 'Speed'])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == 'Speed'])}
```========================''', inline=False)

                    else:

                        embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == i])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == i])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == i])}
Mods 25+: {len([k for k in player_dt.mods if k.speed >= 25 and k.primary == i])}
Mods 20+: {len([k for k in player_dt.mods if 20 <= k.speed <= 24 and k.primary == i])}
Mods 15+: {len([k for k in player_dt.mods if 15 <= k.speed <= 19 and k.primary == i])}
Mods 10+: {len([k for k in player_dt.mods if 10 <= k.speed <= 14 and k.primary == i])}
Mods <10: {len([k for k in player_dt.mods if 9 <= k.speed and k.primary == i])}
```========================''', inline=False)
                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()

            except IndexError:
                mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                      'Critical Damage',
                                      'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

                users.update(restore())
                if str(message.author) in users:
                    for k in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][k])
                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        for i in mods_primary:
                            if i.lower() == 'speed':
                                emoji = '👍'
                                await message.add_reaction(emoji)
                                embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == 'Speed'])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == 'Speed'])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == 'Speed'])}
```========================''', inline=False)

                            else:

                                embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == i])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == i])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == i])}
Mods 25+: {len([k for k in player_dt.mods if k.speed >= 25 and k.primary == i])}
Mods 20+: {len([k for k in player_dt.mods if 20 <= k.speed <= 24 and k.primary == i])}
Mods 15+: {len([k for k in player_dt.mods if 15 <= k.speed <= 19 and k.primary == i])}
Mods 10+: {len([k for k in player_dt.mods if 10 <= k.speed <= 14 and k.primary == i])}
Mods <10: {len([k for k in player_dt.mods if 9 <= k.speed and k.primary == i])}
```========================''', inline=False)

                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()
                else:
                    await message.channel.send('Ally code not registered, use $r <allycode> to register')

            except JSONDecodeError:

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$mpd'):

        allycode = message.content.split()
        if len(allycode[0]) == 4:

            users.update(restore())
            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:

                if str(message.author) in users:
                    mods_slots: list = ['Circle', 'Triangle', 'Diamond', 'Arrow', 'Square', 'Cross']
                    mods_sets: list = ['Critical Chance', 'Critical Damage', 'Health', 'Defense', 'Offense', 'Tenacity',
                                       'Potency', 'Speed']

                    for i in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][i])

                        if allycode[1].lower() == 'cc':
                            allycode[1] = 'Critical Chance'

                        elif allycode[1].lower() == 'cd':
                            allycode[1] = 'Critical Damage'

                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                              'Critical Damage', 'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

                        i = allycode[1].title()
                        if i.title() in mods_primary:
                            emoji = '👍'
                            await message.add_reaction(emoji)

                            if i.lower() == 'speed':

                                a = ''
                                for k in mods_sets:
                                    a += f'''
{k}: {len([j for j in player_dt.mods if j.primary == 'Speed' and j.mod_set == k])}'''

                                embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == 'Speed'])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == 'Speed'])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == 'Speed'])}

-----------------------
    Sorted by Set
-----------------------
{a}
```========================''', inline=False)

                            else:

                                a = '''-----------------------
    Sorted by Set
-----------------------'''

                                for k in mods_sets:
                                    a += f'''
{k}: {len([j for j in player_dt.mods if j.primary == i.title() and j.mod_set == k])}'''
                                b = '''-----------------------
    Sorted by Slot
-----------------------'''

                                for k in mods_slots:
                                    if i == 'Critical Avoidance' or i == 'Potency' or i == 'Tenacity' \
                                            or i == 'Critical Chance' or i == 'Critical Damage':
                                        b = ''

                                    else:
                                        if (i == 'Defense' and k == 'Circle') or (i == 'Defense' and k == 'Square'):
                                            b += ''
                                        elif (i == 'Offense' and k == 'Circle') or (i == 'Offense' and k == 'Diamond'):
                                            b += ''
                                        elif (i == 'Protection' and k == 'Square') or (
                                                i == 'Protection' and k == 'Diamond'):
                                            b += ''
                                        elif (i == 'Health' and k == 'Square') or (i == 'Health' and k == 'Diamond'):
                                            b += ''
                                        else:
                                            b += f'''
{k}: {len([j for j in player_dt.mods if j.primary == i and j.slot == k])}'''

                                embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == i])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == i])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == i])}
Mods 25+: {len([k for k in player_dt.mods if k.speed >= 25 and k.primary == i])}
Mods 20+: {len([k for k in player_dt.mods if 20 <= k.speed <= 24 and k.primary == i])}
Mods 15+: {len([k for k in player_dt.mods if 15 <= k.speed <= 19 and k.primary == i])}
Mods 10+: {len([k for k in player_dt.mods if 10 <= k.speed <= 14 and k.primary == i])}
Mods <10: {len([k for k in player_dt.mods if 9 <= k.speed and k.primary == i])}
{b}
{a}
```========================''', inline=False)

                            embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                            await bot.delete()
                            await message.channel.send(message.author.mention)
                            await message.channel.send(embed=embed)
                            embed.clear_fields()

                        else:

                            emoji = '☠️'
                            await message.add_reaction(emoji)
                            await bot.delete()
                            bot = await message.channel.send('Something went wrong, please try again....')
                            await sleep(60)
                            await bot.delete()

                else:
                    player_dt = Player(allycode[1])
                    mods_slots: list = ['Circle', 'Triangle', 'Diamond', 'Arrow', 'Square', 'Cross']
                    mods_sets: list = ['Critical Chance', 'Critical Damage', 'Health', 'Defense', 'Offense', 'Tenacity',
                                       'Potency', 'Speed']

                    if allycode[2].lower() == 'cc':
                        allycode[2] = 'Critical Chance'

                    elif allycode[2].lower() == 'cd':
                        allycode[2] = 'Critical Damage'

                    embed = discord.Embed(title=player_dt.nick, color=0x000000)
                    mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                          'Critical Damage',
                                          'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

                    i = allycode[2].title()
                    if i.title() in mods_primary:
                        emoji = '👍'
                        await message.add_reaction(emoji)

                        if i.lower() == 'speed':

                            a = ''
                            for k in mods_sets:
                                a += f'''
{k}: {len([j for j in player_dt.mods if j.primary == 'Speed' and j.mod_set == k])}'''

                            embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == 'Speed'])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == 'Speed'])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == 'Speed'])}

-----------------------
    Sorted by Set
-----------------------
{a}
```========================''', inline=False)

                        else:

                            a = '''-----------------------
    Sorted by Set
-----------------------'''

                            for k in mods_sets:
                                a += f'''
{k}: {len([j for j in player_dt.mods if j.primary == i.title() and j.mod_set == k])}'''
                            b = '''-----------------------
    Sorted by Slot
-----------------------'''

                            for k in mods_slots:
                                if i == 'Critical Avoidance' or i == 'Potency' or i == 'Tenacity' \
                                        or i == 'Critical Chance' or i == 'Critical Damage':
                                    b = ''

                                else:
                                    if (i == 'Defense' and k == 'Circle') or (i == 'Defense' and k == 'Square'):
                                        b += ''
                                    elif (i == 'Offense' and k == 'Circle') or (i == 'Offense' and k == 'Diamond'):
                                        b += ''
                                    elif (i == 'Protection' and k == 'Square') or (
                                            i == 'Protection' and k == 'Diamond'):
                                        b += ''
                                    elif (i == 'Health' and k == 'Square') or (i == 'Health' and k == 'Diamond'):
                                        b += ''
                                    else:
                                        b += f'''
{k}: {len([j for j in player_dt.mods if j.primary == i and j.slot == k])}'''

                            embed.add_field(name=f'{i.title()} Primary', value=f'''========================
```fix
Total: {len([k for k in player_dt.mods if k.primary == i])}
6* Mods: {len([k for k in player_dt.mods if k.dot == 6 and k.primary == i])}
5* Mods: {len([k for k in player_dt.mods if k.dot == 5 and k.primary == i])}
Mods 25+: {len([k for k in player_dt.mods if k.speed >= 25 and k.primary == i])}
Mods 20+: {len([k for k in player_dt.mods if 20 <= k.speed <= 24 and k.primary == i])}
Mods 15+: {len([k for k in player_dt.mods if 15 <= k.speed <= 19 and k.primary == i])}
Mods 10+: {len([k for k in player_dt.mods if 10 <= k.speed <= 14 and k.primary == i])}
Mods <10: {len([k for k in player_dt.mods if 9 <= k.speed and k.primary == i])}
{b}
{a}
```========================''', inline=False)

                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()

                    else:

                        emoji = '☠️'
                        await message.add_reaction(emoji)
                        await bot.delete()
                        bot = await message.channel.send('Something went wrong, please try again....')
                        await sleep(60)
                        await bot.delete()

            except (IndexError, JSONDecodeError):

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$ms'):

        allycode = message.content.split()
        if len(allycode[0]) == 3:

            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:

                player_dt = Player(allycode[1])
                mods_sets: list = ['Critical Chance', 'Critical Damage', 'Health', 'Defense', 'Offense', 'Tenacity',
                                   'Potency', 'Speed']
                emoji = '👍'
                await message.add_reaction(emoji)

                embed = discord.Embed(title=player_dt.nick, color=0x000000)
                for k in mods_sets:
                    embed.add_field(name=f'{k} Set', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.mod_set == k])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.mod_set == k])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.mod_set == k])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.mod_set == k])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.mod_set == k])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.mod_set == k])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.mod_set == k])}
```========================''', inline=False)
                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()

            except IndexError:
                users.update(restore())
                if str(message.author) in users:
                    for i in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][i])
                        mods_sets: list = ['Critical Chance', 'Critical Damage', 'Health', 'Defense', 'Offense',
                                           'Tenacity', 'Potency', 'Speed']
                        emoji = '👍'
                        await message.add_reaction(emoji)

                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        for k in mods_sets:
                            embed.add_field(name=f'{k} Set', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.mod_set == k])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.mod_set == k])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.mod_set == k])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.mod_set == k])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.mod_set == k])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.mod_set == k])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.mod_set == k])}
```========================''', inline=False)
                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()
                else:
                    await message.channel.send('Ally code not registered, use ```$r <allycode>``` to register')

            except JSONDecodeError:

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$msd'):

        allycode = message.content.split()
        if len(allycode[0]) == 4:

            users.update(restore())
            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:
                mods_slots: list = ['Circle', 'Triangle', 'Diamond', 'Arrow', 'Square', 'Cross']
                mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                      'Critical Damage',
                                      'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

                if str(message.author) in users:
                    for m in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][m])

                        emoji = '👍'
                        await message.add_reaction(emoji)

                        if allycode[1].lower() == 'cc':
                            allycode[1] = 'Critical Chance'
                        elif allycode[1].lower() == 'cd':
                            allycode[1] = 'Critical Damage'
                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        a = ''
                        for i in mods_slots:
                            a += f'''{i}: {len([j for j in player_dt.mods if j.mod_set == allycode[1].title()
                                                and j.slot == i])}
'''
                        b = ''
                        for k in mods_primary:
                            b += f'''{k}: {len([j for j in player_dt.mods if j.mod_set == allycode[1].title() and
                                                j.primary == k])}
'''

                        embed.add_field(name=f'{allycode[1].title()} Set', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.mod_set == allycode[1].title()])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.mod_set == allycode[1].title()])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.mod_set == allycode[1].title()])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.mod_set == allycode[1].title()])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.mod_set == allycode[1].title()])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.mod_set == allycode[1].title()])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.mod_set == allycode[1].title()])}
-----------------------
    Sorted by Slot
-----------------------
{a}
-----------------------
    Sorted by Primary
-----------------------
{b}
```========================''', inline=False)
                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()
                else:
                    player_dt = Player(allycode[1])

                    emoji = '👍'
                    await message.add_reaction(emoji)

                    if allycode[2].lower() == 'cc':
                        allycode[2] = 'Critical Chance'
                    elif allycode[2].lower() == 'cd':
                        allycode[2] = 'Critical Damage'
                    embed = discord.Embed(title=player_dt.nick, color=0x000000)
                    a = ''
                    for i in mods_slots:
                        a += f'''{i}: {len([j for j in player_dt.mods if j.mod_set == allycode[2].title()
                                            and j.slot == i])}
'''
                    b = ''
                    for k in mods_primary:
                        b += f'''{k}: {len([j for j in player_dt.mods if j.mod_set == allycode[2].title() and
                                            j.primary == k])}
'''

                    embed.add_field(name=f'{allycode[2].title()} Set', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.mod_set == allycode[2].title()])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.mod_set == allycode[2].title()])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.mod_set == allycode[2].title()])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.mod_set == allycode[2].title()])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.mod_set == allycode[2].title()])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.mod_set == allycode[2].title()])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.mod_set == allycode[2].title()])}
-----------------------
    Sorted by Slot
-----------------------
{a}
-----------------------
   Sorted by Primary
-----------------------
{b}
```========================''', inline=False)
                    embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                    await bot.delete()
                    await message.channel.send(message.author.mention)
                    await message.channel.send(embed=embed)
                    embed.clear_fields()

            except (IndexError, JSONDecodeError):

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$mst'):

        allycode = message.content.split()
        if len(allycode[0]) == 4:

            users.update(restore())
            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')
            mods_slots: list = ['Circle', 'Triangle', 'Diamond', 'Arrow', 'Square', 'Cross']

            try:

                player_dt = Player(allycode[1])
                emoji = '👍'
                await message.add_reaction(emoji)

                embed = discord.Embed(title=player_dt.nick, color=0x000000)
                for k in mods_slots:
                    embed.add_field(name=f'{k}', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.slot == k])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.slot == k])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.slot == k])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.slot == k])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.slot == k])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.slot == k])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.slot == k])}
```========================''', inline=False)
                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()

            except IndexError:

                if str(message.author) in users:
                    emoji = '👍'
                    await message.add_reaction(emoji)
                    for m in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][m])
                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        for k in mods_slots:
                            embed.add_field(name=f'{k}', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.slot == k])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.slot == k])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.slot == k])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.slot == k])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.slot == k])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.slot == k])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.slot == k])}
```========================''', inline=False)
                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()
                else:
                    await message.channel.send('Ally code not registered, use ```$r <allycode>``` to register')

            except JSONDecodeError:

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$mstd'):

        allycode = message.content.split()
        if len(allycode[0]) == 5:

            users.update(restore())
            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')
            mods_slots: list = ['Circle', 'Triangle', 'Diamond', 'Arrow', 'Square', 'Cross']
            mods_sets: list = ['Critical Chance', 'Critical Damage', 'Health', 'Defense', 'Offense', 'Tenacity',
                               'Potency', 'Speed']
            mods_primary: list = ['Protection', 'Health', 'Offense', 'Defense', 'Critical Chance',
                                  'Critical Damage',
                                  'Critical Avoidance', 'Tenacity', 'Potency', 'Speed']

            try:

                if str(message.author) in users:
                    for m in range(len(users[str(message.author)])):
                        player_dt = Player(users[str(message.author)][m])
                        if allycode[1].title() in mods_slots:

                            emoji = '👍'
                            await message.add_reaction(emoji)
                            embed = discord.Embed(title=player_dt.nick, color=0x000000)
                            a = ''
                            for i in mods_sets:
                                a += f'''
{i}: {len([j for j in player_dt.mods if j.slot == allycode[1].title() and j.mod_set == i])}'''
                            b = '''-----------------------
    Sorted by Primary
-----------------------
'''

                            for k in mods_primary:

                                if allycode[1].lower() == 'circle' and (k.lower() != 'health'
                                                                        and k.lower() != 'protection'):
                                    b += ''
                                elif allycode[1].lower() == 'diamond' or allycode[1].lower() == 'square':
                                    b = ''
                                elif allycode[1].lower() == 'triangle' and \
                                        (k.lower() == 'speed' or k.lower() == 'potency' or k.lower() == 'tenacity'
                                         or k.lower() == 'critical avoidance'):
                                    b += ''
                                elif allycode[1].lower() == 'arrow' and \
                                        (k.lower() == 'critical chance' or k.lower() == 'critical damage'
                                         or k.lower() == 'tenacity' or k.lower() == 'potency'):
                                    b += ''
                                elif allycode[1].lower() == 'cross' and \
                                        (k.lower() == 'speed' or k.lower() == 'critical chance'
                                         or k.lower() == 'critical damage' or k.lower() == 'critical avoidance'):
                                    b += ''

                                else:

                                    b += f'''{k}: {len([j for j in player_dt.mods if j.slot == allycode[1].title() and
                                                        j.primary == k])}
'''

                            embed.add_field(name=f'{allycode[1].title()} Mods', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.slot == allycode[1].title()])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.slot == allycode[1].title()])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.slot == allycode[1].title()])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.slot == allycode[1].title()])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.slot == allycode[1].title()])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.slot == allycode[1].title()])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.slot == allycode[1].title()])}
-----------------------
Sorted by Set
-----------------------{a}
{b}
```========================''', inline=False)
                            embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                            await bot.delete()
                            await message.channel.send(message.author.mention)
                            await message.channel.send(embed=embed)
                            embed.clear_fields()

                        else:

                            emoji = '☠️'
                            await message.add_reaction(emoji)
                            await bot.delete()
                            bot = await message.channel.send('Something went wrong, please try again....')
                            await sleep(60)
                            await bot.delete()

                else:

                    player_dt = Player(allycode[1])
                    if allycode[2].title() in mods_slots:

                        emoji = '👍'
                        await message.add_reaction(emoji)
                        embed = discord.Embed(title=player_dt.nick, color=0x000000)
                        a = ''
                        for i in mods_sets:
                            a += f'''
{i}: {len([j for j in player_dt.mods if j.slot == allycode[2].title() and j.mod_set == i])}'''
                        b = '''-----------------------
   Sorted by Primary
-----------------------
'''

                        for k in mods_primary:

                            if allycode[2].lower() == 'circle' and (k.lower() != 'health'
                                                                    and k.lower() != 'protection'):
                                b += ''
                            elif allycode[2].lower() == 'diamond' or allycode[2].lower() == 'square':
                                b = ''
                            elif allycode[2].lower() == 'triangle' and \
                                    (k.lower() == 'speed' or k.lower() == 'potency' or k.lower() == 'tenacity'
                                     or k.lower() == 'critical avoidance'):
                                b += ''
                            elif allycode[2].lower() == 'arrow' and \
                                    (k.lower() == 'critical chance' or k.lower() == 'critical damage'
                                     or k.lower() == 'tenacity' or k.lower() == 'potency'):
                                b += ''
                            elif allycode[2].lower() == 'cross' and \
                                    (k.lower() == 'speed' or k.lower() == 'critical chance'
                                     or k.lower() == 'critical damage' or k.lower() == 'critical avoidance'):
                                b += ''

                            else:

                                b += f'''{k}: {len([j for j in player_dt.mods if j.slot == allycode[2].title() and
                                                    j.primary == k])}
'''

                        embed.add_field(name=f'{allycode[2].title()} Mods', value=f'''========================
```fix
6* Mods: {len([i for i in player_dt.mods if i.dot == 6 and i.slot == allycode[2].title()])}
5* Mods: {len([i for i in player_dt.mods if i.dot == 5 and i.slot == allycode[2].title()])}
Mods 25+: {len([i for i in player_dt.mods if i.speed >= 25 and i.slot == allycode[2].title()])}
Mods 20+: {len([i for i in player_dt.mods if 20 <= i.speed <= 24 and i.slot == allycode[2].title()])}
Mods 15+: {len([i for i in player_dt.mods if 15 <= i.speed <= 19 and i.slot == allycode[2].title()])}
Mods 10+: {len([i for i in player_dt.mods if 10 <= i.speed <= 14 and i.slot == allycode[2].title()])}
Mods <10: {len([i for i in player_dt.mods if 9 <= i.speed and i.slot == allycode[2].title()])}
-----------------------
    Sorted by Set
-----------------------{a}
{b}
```========================''', inline=False)
                        embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

                        await bot.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=embed)
                        embed.clear_fields()

                    else:

                        emoji = '☠️'
                        await message.add_reaction(emoji)
                        await bot.delete()
                        bot = await message.channel.send('Something went wrong, please try again....')
                        await sleep(60)
                        await bot.delete()

            except (IndexError, JSONDecodeError):

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$help'):

        if len(message.content) == 5:
            emoji = '🤔'
            await message.add_reaction(emoji)

            embed = discord.Embed(title=client.user.name, color=0x000000)
            embed.add_field(name='Mod Analysis', value='''========================
$m → basic speed analysis
```$m ally-code```
$mp → sort mods by primary
```$mp ally-code```
$mpd → sort mods by primary with additional details
```$mp ally-code primary``` 
$ms → sort mods by set
```$ms ally-code```
$msd → sort mods by set with additional details
```$ms ally-code set```
$mst → sort mods by slot
```$mst ally-code```
$mstd → sort mods by slot with additional details
```$mstd ally-code slot```======================== ''', inline=True)

            emoji = '👍'
            await message.add_reaction(emoji)
            await message.channel.send(embed=embed)

    if message.content.startswith('$help mq'):

        if len(message.content) == 8:
            emoji = '🤔'
            await message.add_reaction(emoji)

            embed = discord.Embed(title=client.user.name, color=0x000000)
            embed.add_field(name='Mod Quality', value='''========================
```fix
Mod Quality = (mod group * value) + (mod group * value)... / Squad GP / 1000000

The value of a mod is based on it speed, primary and set.

For example:
| Speed |                 Primary                |	 Set  | Value |
-------------------------------------------------------------------
|     	| Health, Protection, Potency, Tenacity, |        |       |
|   25  | Critical Avoidance, Defense (Diamond), | Health |  0.9  |
|       | Offense (Square)                       |		  |       |
-------------------------------------------------------------------
|     	| Health, Protection, Potency, Tenacity, |        |       |
|   25  | Critical Avoidance, Defense (Diamond), | Offense|  1.2  |
|       | Offense (Square)                       |		  |       |
-------------------------------------------------------------------
|     	| Health, Protection, Potency, Tenacity, |Tenacity|       |
|   25  | Critical Avoidance, Defense (Diamond), | Potency|   1   |
|       | Offense (Square)                       |		  |       |
-------------------------------------------------------------------
```
To se the complete list os values visit AP-5 discord server:

''', inline=True)
            embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)

            emoji = '👍'
            await message.add_reaction(emoji)
            await message.channel.send(embed=embed)

    if message.content.startswith('$gq'):

        guild = message.content.split()
        if len(guild[0]) == 3:
            users.update(restore())

            emoji = '🤔'
            await message.add_reaction(emoji)
            bot = await message.channel.send('One moment....')

            try:

                gq = Guild(guild[1])
                guild_gq = gq.gq()
                guild = guild_gq.split('\n')
                x = '\n'.join(guild[:13])
                y = '\n'.join(guild[13:26])
                z = '\n'.join(guild[26:39])
                w = '\n'.join(guild[39:])
                emoji = '👍'
                await message.add_reaction(emoji)
                embed = discord.Embed(title=gq.guild_name, color=0x000000)
                embed.add_field(name='Guild Quality', value=f'''```fix
{x}
```''', inline=True)
                embed.add_field(name='==========================', value=f'''```fix
{y}
```''', inline=False)
                embed.add_field(name='==========================', value=f'''```fix
{z}
```''', inline=False)
                embed.add_field(name='==========================', value=f'''```fix
{w}
```''', inline=False)
                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()

            except IndexError:

                if str(message.author) in users:
                    v = ''
                    for m in range(len(users[str(message.author)])):
                        gq = Guild(users[str(message.author)][m])
                        try:
                            if v.guild_name == gq.guild_name:
                                return
                            else:
                                guild_gq = gq.gq()
                                guild = guild_gq.split('\n')
                                x = '\n'.join(guild[:13])
                                y = '\n'.join(guild[13:26])
                                z = '\n'.join(guild[26:39])
                                w = '\n'.join(guild[39:])
                                emoji = '👍'
                                await message.add_reaction(emoji)
                                embed = discord.Embed(title=gq.guild_name, color=0x000000)
                                embed.add_field(name='Guild Quality', value=f'''```fix
{x}
```''', inline=True)
                                embed.add_field(name='==========================', value=f'''```fix
{y}
```''', inline=False)
                                embed.add_field(name='==========================', value=f'''```fix
{z}
```''', inline=False)
                                embed.add_field(name='==========================', value=f'''```fix
{w}
```''', inline=False)
                                embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                                await bot.delete()
                                await message.channel.send(message.author.mention)
                                await message.channel.send(embed=embed)
                                embed.clear_fields()
                                v = gq

                        except AttributeError:
                            guild_gq = gq.gq()
                            guild = guild_gq.split('\n')
                            x = '\n'.join(guild[:13])
                            y = '\n'.join(guild[13:26])
                            z = '\n'.join(guild[26:39])
                            w = '\n'.join(guild[39:])
                            emoji = '👍'
                            await message.add_reaction(emoji)
                            embed = discord.Embed(title=gq.guild_name, color=0x000000)
                            embed.add_field(name='Guild Quality', value=f'''```fix
{x}
```''', inline=True)
                            embed.add_field(name='==========================', value=f'''```fix
{y}
```''', inline=False)
                            embed.add_field(name='==========================', value=f'''```fix
{z}
```''', inline=False)
                            embed.add_field(name='==========================', value=f'''```fix
{w}
```''', inline=False)
                            embed.set_footer(icon_url=client.user.avatar_url_as(), text=client.user.name)
                            await bot.delete()
                            await message.channel.send(message.author.mention)
                            await message.channel.send(embed=embed)
                            embed.clear_fields()
                            v = gq

            except JSONDecodeError:

                emoji = '☠️'
                await message.add_reaction(emoji)
                await bot.delete()
                bot = await message.channel.send('Something went wrong, please try again....')
                await sleep(60)
                await bot.delete()

    if message.content.startswith('$r '):
        users.update(restore())
        register = message.content.split()
        if len(register[0]) == 2:
            emoji = '🤔'
            await message.add_reaction(emoji)

            ally: list = []
            flag: bool = True
            for i in range(1, len(register)):
                ally.append(register[i])

            for k in ally:

                if len(k) == 9:
                    flag = True

                else:
                    flag = False

            if not flag:
                await message.channel.send('Ally code not recognised')

            else:
                reg = {str(message.author): ally}
                users.update(reg)
                await message.channel.send(str(message.author.mention) + f'ally code {ally} registered')
                bkp(users)


users.update(restore())
token = unpickle()
keep_alive()
client.run(token)
