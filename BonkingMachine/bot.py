# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='&bonk ')

@bot.event
async def on_ready():
    print('Bonking Machine is now online!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="&bonk help"))

@bot.remove_command('help')
@bot.command(name='help')
async def customhelp(ctx):
    helpembed = discord.Embed(
        title = 'Help',
        description = 'Hello and welcome to the Bonking Machine!',
        colour = discord.Colour.gold()
    )
    helpembed.add_field(name='How it works', value=(':hammer: This bot listens to the prefix "&bonk ".\n'
                                                    ':hammer: Use `&bonk <person>` to bonk someone who deserves it\n'
                                                    ':hammer: Example: `&bonk @Isa`\n'
                                                    ':hammer: Use `&bonk themall` to just bonk everyone'), inline=False)
    if ctx.guild.id == 687395143359266817:
        helpembed.add_field(name='Only in KML', value=(':cop: Use `&bonk jail <person>` to send someone to horny jail\n'
                                                       ':cop: and `&bonk release <person>` to release them again (reverts the jail command)'), inline=False)
    helpembed.add_field(name='Credits', value=(':arrow_right: This bot was made by IsaTheFrootLoop#8269. It is still being developed, please report all bugs, issues and suggestions to them.\n'
                                               ':arrow_right: The Bonking Machine was fully inspired by Koi, the bestest fox loaf.\n'
                                               ':arrow_right: Please do not redistribute or publish this bot without my explicit permission.'), inline=False)
    await ctx.send(embed=helpembed)

bonkimages = [
    'https://cdn.discordapp.com/attachments/755160227518611621/755161567913443378/gottabonkthemall.png',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161209761693707/gottabonkthem2.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161228447580230/gottabonkthem3.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161404750823554/gottabonkthem4.png',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161427223773244/gottabonkthem5.png',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161448631631902/gottabonkthem6.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161484631474316/gottabonkthem7.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161516323635210/gottabonkthem8.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161540985880796/gottabonkthem9.png',
    'https://cdn.discordapp.com/attachments/755160227518611621/755178169086246942/gottabonkthem10.jpg',
    'https://cdn.discordapp.com/attachments/755160227518611621/755161183677317191/gottabonkthem1.png',
]

@bot.command(name='themall')
async def bonkeveryone(ctx):
    bonkallembed = discord.Embed(
        title = 'Bonk!',
        description = 'You\'ve all been such naughty boys, feel bonked!',
        colour = discord.Colour.magenta()
    )
    
    bonkallembed.set_footer(text='Better behave!')
    bonkallembed.set_image(url=random.choice(bonkimages))
    
    await ctx.send(embed=bonkallembed)

@bot.command(name='now')
async def bonksomeone(ctx, person: discord.Member):
    if person.bot == False:
        bonkembed = discord.Embed(
            title = 'Bonk!',
            description = 'Naughty boy ' + person.mention + ' Feel bonked!',
            colour = discord.Colour.magenta()
            )
    
        bonkembed.set_footer(text='Better behave!')
        bonkembed.set_image(url=random.choice(bonkimages))
        
    await ctx.send(embed=bonkembed)
    
@bot.command(name='jail')
async def sendtojail(ctx, person: discord.Member):
    if ctx.guild.id != 687395143359266817:
        await ctx.send('Sorry, this command was custom made and only works on the Koikatsu Maid Lounge Server.')
    elif person.bot == True:
        await ctx.send('Sorry, this command only works with actual Members, not with Bots.')
    else:
        criminal = discord.utils.find(lambda m: m.id == 735916858095697940, ctx.guild.roles)
        if criminal in person.roles:
            await ctx.send('The member you try to send to jail is already in jail')
        else:
            master = discord.utils.find(lambda m: m.id == 731189558720593953, ctx.guild.roles)
            await person.add_roles(criminal, atomic=True)
            await person.remove_roles(master, atomic=True)
            await ctx.send(person.name + 'has been sent to horny jail')
        
@bot.command(name='release')
async def releasejail(ctx, person: discord.Member):
    if ctx.guild.id != 687395143359266817:
        await ctx.send('Sorry, this command was custom made and only works on the Koikatsu Maid Lounge Server.')
    elif person.bot == True:
        await ctx.send('Sorry, this command only works with actual Members, not with Bots.')
    elif ctx.message.author == person:
        await ctx.send('You can\'t release yourself naughty idiot. The Horny Police and Staff will decide your fate.')
        bonksomeone(ctx, person)
    else:
        criminal = discord.utils.find(lambda m: m.id == 735916858095697940, ctx.guild.roles)
        if criminal in person.roles:
            master = discord.utils.find(lambda m: m.id == 731189558720593953, ctx.guild.roles)
            await person.remove_roles(criminal, atomic=True)
            await person.add_roles(master, atomic=True)
            await ctx.send(person.name + 'has been released from horny jail')
        else:
            await ctx.send('The member you try to release is not in jail')
        
bot.run(TOKEN) 