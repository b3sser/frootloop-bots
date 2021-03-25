# bot.py
import os
import random
import discord
import urllib, re
from dotenv import load_dotenv
from discord.ext import commands 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='ntr ')

@bot.event
async def on_ready():
    print('NTR is now online!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ntr help"))

@bot.remove_command('help')
@bot.command(name='help')
async def customhelp(ctx):
    helpembed = discord.Embed(
        title = 'Help',
        description = 'Hello and welcome to NTR - NHentai Totally Random!\n',
        colour = discord.Colour.gold()
    )
    helpembed.add_field(name='How it works', value=('On `ntr cum` this bot sends a random gallery from nHentai.net\n'
                                                    'Same works with `ntr rule` for rule34.xxx\n'
                                                    'Not so random is the function `ntr newrule <tag> <number>`. It returns the latest <number> (optional, defaults to 1) posts on rule34 that were tagged with <tag> (optional, defaults to all)'), inline=False)
    helpembed.add_field(name='Reacting', value=('Below each you can react with four emojis to show your opinion\n'
                                                ':hot_face: if it\'s good, :yawning_face: if it\'s boring, :face_vomiting: if it\'s rather eww and :rotating_light: if you wanna get out your banhammer and call the FBI'), inline=False)
    helpembed.add_field(name='Credits', value=(':arrow_right: This bot was made by IsaTheFrootLoop#8269. It is still being developed, please report all bugs, issues and suggestions to them.\n'
                                               ':arrow_right: Please do not redistribute or publish this bot without their explicit permission.'), inline=False)
    await ctx.send(embed=helpembed)

@bot.command(name='cum')
async def get_hent(ctx):
    hennum = random.randint(1, 329628)
    henurl = 'https://nhentai.net/g/' + str(hennum) + '/'
    nice = '\U0001F975'
    boring = '\U0001F971'
    eww = '\U0001F922'
    fbiopenup = '\U0001F6A8' 
    message = await ctx.send(henurl)
    await message.add_reaction(nice)
    await message.add_reaction(boring)
    await message.add_reaction(eww)
    await message.add_reaction(fbiopenup)

@bot.command(name='rule')
async def get_rule34(ctx, ):
    picnum = random.randint(1, 4262800)
    picurl = 'https://rule34.xxx/index.php?page=post&s=view&id=' + str(picnum)
    nice = '\U0001F975'
    boring = '\U0001F971'
    eww = '\U0001F922'
    fbiopenup = '\U0001F6A8' 
    message = await ctx.send(picurl)
    await message.add_reaction(nice)
    await message.add_reaction(boring)
    await message.add_reaction(eww)
    await message.add_reaction(fbiopenup)

@bot.command(name='newrule')
async def get_rule_tag(ctx, hentag='all', number=1):
    tagurl = 'https://rule34.xxx/index.php?page=post&s=list&tags=' + str(hentag)
#    await ctx.send(tagurl)
    htm_content = urllib.request.urlopen(tagurl)
#    print(htm_content.read(100000))
    search_results = re.findall('href="index.php\?page=post&amp;s=view&amp;id=(.{7})', htm_content.read().decode())
#    await ctx.send(search_results)
    indexxx = 0
    while indexxx < number:
        await ctx.send('https://rule34.xxx/index.php?page=post&s=view&id=' + search_results[indexxx])
        indexxx += 1
    await ctx.send('Happy fapping!')
bot.run(TOKEN) 
