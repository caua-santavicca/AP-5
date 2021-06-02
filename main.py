import discord
from os import environ
from asyncio import sleep
# from keep_alive import keep_alive
import functions

# import coreapi_cli

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$mods'):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_speed(allycode[1])
            if type(mods) == tuple:
                embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                embed.add_field(name='Mods ', value=f'''========================
```fix
6* Mods: {mods[6]}
5* Mods: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()
            else:
                await message.channel.send(mods)
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()

    if message.content.startswith('$modp'):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_primary_speed(allycode[1], allycode[2])
            if type(mods) == tuple:
                if allycode[2].lower() == 'speed':
                    embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                    embed.add_field(name=f'{allycode[2].title()} Primary', value=f'''========================
```fix
6* Mods: {mods[6]}
5* Mods: {mods[5]}
```========================''', inline=False)
                    await bot.delete()
                    await message.channel.send(message.author.mention)
                    await message.channel.send(embed=embed)
                    embed.clear_fields()
                else:
                    embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                    embed.add_field(name=f'{allycode[2].title()} Primary', value=f'''========================
```fix
6* Mods: {mods[6]}
5* Mods: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                    await bot.delete()
                    await message.channel.send(message.author.mention)
                    await message.channel.send(embed=embed)
                    embed.clear_fields()
            else:
                await bot.delete()
                bot = await message.channel.send(mods)
                await sleep(60)
                await bot.delete()
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()

    if message.content.startswith('$ms'):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_set_speed(allycode[1], allycode[2])
            if type(mods) == tuple:
                embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                embed.add_field(name=f'{allycode[2].title()} Set', value=f'''========================
```fix
6* Mods: {mods[6]}
5* Mods: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()
            else:
                await bot.delete()
                bot = await message.channel.send(mods)
                await sleep(60)
                await bot.delete()
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()

    if message.content.startswith('$slot'):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_position_speed(allycode[1], allycode[2])
            if type(mods) == tuple:
                embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                embed.add_field(name=f'{allycode[2].title()} Mods', value=f'''========================
```fix
6* Mods: {mods[6]}
5* Mods: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()
            else:
                await bot.delete()
                bot = await message.channel.send(mods)
                await sleep(60)
                await bot.delete()
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()

    if message.content.startswith('$ps '):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_position_set_speed(allycode[1], allycode[2], allycode[3])
            if type(mods) == tuple:
                embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                embed.add_field(name=f'{allycode[2].title()} {allycode[3].title()} Set',
                                value=f'''========================
```fix
Total: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()
            else:
                await bot.delete()
                bot = await message.channel.send(mods)
                await sleep(60)
                await bot.delete()
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()

    if message.content.startswith('$mpps '):
        allycode = message.content.split()
        bot = await message.channel.send('One moment....')
        try:
            mods = functions.mods_position_primary_set_speed(allycode[1], allycode[2], allycode[3], allycode[4])
            if type(mods) == tuple:
                embed = discord.Embed(title=functions.get_player_nick(allycode[1]), color=0xffffff)
                embed.add_field(name=f'{allycode[2].title()} {allycode[4].title()} Primary {allycode[3].title()} Set',
                                value=f'''========================
```fix
Total: {mods[5]}
Mods 25+: {mods[0]}
Mods 20+: {mods[1]}
Mods 15+: {mods[2]}
Mods 10+: {mods[3]}
Mods <10: {mods[4]}
```========================''', inline=False)
                await bot.delete()
                await message.channel.send(message.author.mention)
                await message.channel.send(embed=embed)
                embed.clear_fields()
            else:
                await bot.delete()
                bot = await message.channel.send(mods)
                await sleep(60)
                await bot.delete()
        except IndexError:
            await bot.delete()
            bot = await message.channel.send('Deu Merda!')
            await sleep(60)
            await bot.delete()


token = environ.get("DISCORD_BOT_SECRET")
# keep_alive()
client.run('ODI0MzQ2Mjg5MDU0Njc5MDUx.YFuCTg.m8kqDvY2fzOMCX_azi2PLhaoJM4')
