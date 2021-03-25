# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Stuff - Important for da bot to work
# Prefix festlegen
bot = commands.Bot(command_prefix='&&')

# Aktivitaet festlegen, die der Bot auf DC zeigt
@bot.event
async def on_ready():
    print('Secretary is now online!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="&&help"))

@bot.remove_command('help')                     # Custom Help
@bot.command(name='help')
async def customhelp(ctx):
    helpembed = discord.Embed(
        title = 'Help',
        description = 'Hello and welcome to Isas Secretary Bot. This is the help page, including syntax explanation and a list of all available Characters',
        colour = discord.Colour.blurple()
    )
    
    helpembed.add_field(name='How it works', value=('This bot listens to the prefix "&&".\n'
                                                    'The Syntax is as follows: `&&<name> <special>`\n'
                                                    'Please note: Upper or lower case letters does matter. Most commands here use only lower case.\n'
                                                    '\n'
                                                    '`<special>` may be left empty for a normal quote or optionally be `oath` or `chocolate`.\n'
                                                    '`oath` delivers the characters voice line upon establishing Oath (GFL) or Pledge (Azur Lane), if applicable.\n'
                                                    '`chocolate` delivers the voice line the character uses when giving you chocolate on Valentines Day, if applicable.\n'
                                                    '\n'
                                                    'Example: `&&friedrich` delivers a random quote from Friedrich der Grosse from Azur Lane.\n'
                                                    'Example: `&&hk416 oath` delivers what HK416 from GFL says during the Oath Ceremony'), inline=False)
    
    helpembed.add_field(name='List of characters', value='Below is a list of currently available characters and their respective &&command. To request a character, please contact the bots owner, Isa.', inline=False)
    helpembed.add_field(name='Azur Lane:', value=('Friedrich der Grosse - `friedrich`\n'
                                                 'Hammann - `hammann`\n'
                                                 'Atago - `atago`\n'
                                                 'Enterprise - `enterprise`\n'
                                                 'Belfast - `belfast`\n'
                                                 'More cuming soon'), inline=True)
    helpembed.add_field(name='Girls\' Frontline (GFL):', value=('HK416 - `hk416`\n'
                                                                'WA2000 - `wachan`\n'
                                                                'IDW - `idw`\n'
                                                                'M4A1 - `m4`\n'
                                                                'More cuming soon'), inline=True)
    helpembed.add_field(name='Others:', value=('Shinobu Oshino - Bakemonogatari - `shinobu`\n'
                                               'Rias Gremory - Highschool DxD - `rias`\n'
                                               'More cuming soon'), inline=False)
    helpembed.add_field(name='Credits', value=(':arrow_right: This bot was made by IsaTheFrootLoop#8269. It is still being developed, please report all bugs, issues and suggestions to them.\n'
                                               ':arrow_right: Please do not redistribute or publish this bot without my (Isas) explicit permission. If you want to get it for one of your servers or share with your friends, drop me a quick dm for the permission and invite link.\n'
                                               ':arrow_right: The images used for each character do not belong to the programmer, they are official artworks from the respective game or series where possible, but some (only in "Others") might also be fanart. If an artist wants their fanart to be taken out of this bot, contact Isa (the programmer) for it to be taken down.'), inline=False)

    await ctx.send(embed=helpembed)

@bot.command(name='hk416')                      # GFL
async def hk416quote(ctx, special='no'):
    hk416_quotes_list = [
        'Commander, I am all you need.',
        'HKM4? I have no need for such a name anymore!',
        'How have you been doing these days, Commander? If you\'re feeling down, I\'ll make you smile by any means necessary... You got a better idea? Let\'s hear it.',
        'Good morning, Commander. I won\'t lose to anyone today.',
        'HK416......Please remember this name, this...extraordinary name.',
        'I am perfect.',
    ]    
    
    if special == 'oath':
        quote = 'Be it you or achievements in combat, everything is mine. You don\'t have to raise a finger, Commander. I\'ll settle everything for you.'
    elif special == 'chocolate':
        quote = 'My chocolate was made with perfectly calculated ingredients. Ehh? It tastes weird? You jest.'
    else:
        quote = random.choice(hk416_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'HK416:',
        description = quote ,
        colour = discord.Colour.gold()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755408436858191902/HK416_S.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='wachan')
async def wa2000quote(ctx, special='no'):
    wa2000_quotes_list = [
        'Commander, stand aside and don\'t get in my way.',
        'Idiot... If I really hated you, then I wouldn\'t be talking to you.',
        'Listen carefully! Don\'t call my name so casually and don\'t touch my gun with your filthy hands!',
        'Eh? My face is red? It\'s because... it\'s a bit hot today! D-Don\'t get the wrong idea!',
        'Is there anything else left to do? Letting someone so valuable like myself be busying the entire day, you\'d better reward me well after work, okay?',
        'Hey, where did you go!? Do you really dislike seeing my face that much!?',
        'I, of all people, am giving you my gratitude. So you better accept it from the bottom of your heart.',
        'Hmph, fine then.',
        'Idiot, I don\'t want you to be worried over me...',
        'You\'re free now anyway, it\'s pitiful seeing you all alone, so I shall accompany you for a bit...',
    ]    
         
    if special == 'oath':
        quote = 'I\'m a tool created solely for the purpose of killing, and I\'ve never thought about anything else besides that. Commander, are you sure you want me by your side? Hmm...with this, maybe I can become more perfect'
    elif special == 'chocolate':
        quote = 'I just happen to have some extra chocolate! I won\'t forgive you if you turn it down!'
    else:
        quote = random.choice(wa2000_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'WA2000:',
        description = quote ,
        colour = discord.Colour.gold()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755461041877549176/WA2000_S.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='idw')
async def idwquote(ctx, special='no'):
    idw_quotes_list = [
        'Commander, Well done nya~!',
        'Are you the commander who is willing to adopt me ? I\'ll do my best !',
        'You like cats, Commeownder? So you like me?',
        'Huh? My age? I was born the day I met you, Commeownder!',
        'Up a bit! Yes, yes, right there! Thanks Commeownder!',
        'Commander, how\'s the weather outside? Let\'s go sunbathing together, I\'ve been wanting to do that since forever!',
        'Morning commander! Let me give you a hand~!',
        'Let\'s play together~!',
        'So many cat ears nya!',
        'Let\'s go searching for food!',
        'Don\'t treat me as pistols!',
        'Da nyaaa~',
    ]    
      
    if special == 'oath':
        quote = 'What? Really? All I wanted...was home. I never though about having you all to meowself. But if that\'s what you want, Commeownder...I\'m helping meowself'
    else:
        quote = random.choice(idw_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'IDW:',
        description = quote ,
        colour = discord.Colour.greyple()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755465557968552031/IDW_S.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='m4')
async def m4a1quote(ctx, special='no'):
    m4a1_quotes_list = [
        'Commander, please take care of me from now on.',
        'As always, I have complete faith in your judgment. Let us lead everyone to victory.',
        'Umm, commander... That... kind of tickles...',
        'You\'re going to give me treats?',
        'One day... I will make M16 nee-san proud',
        'Our bond and trust, don\'t need candied words to decorate ...',
    ]    
         
    if special == 'oath':
        quote = 'Commander... it\'s a privilege to fight for you. Umm... What I mean to say is that. After this, please let me stay by your side forever.'
    elif special == 'chocolate':
        quote = 'Here... obligatory chocolate.'
    else:
        quote = random.choice(m4a1_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'M4A1:',
        description = quote ,
        colour = discord.Colour.green()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755468367946711130/M4A1_S.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='friedrich')                  # Azur Lane
async def friedrichquote(ctx, special='no'):
    friedrich_quotes_list = [
        'Feel free to fawn over me as much as you wish, more, and more...',
        'Do occasionally come and fawn over me.',
        'Come, my child... If you are unable to sleep, allow me to play you a lullaby.',
        'You\'ve returned to my side once more, my child. Tell me, what is it that you wish for? Wealth? Glory? Or perhaps eternal youth?',
        'My child, if you desire absolute victory, you must maintain absolute rationality.',
        'My appearance upon the battlefield gives off an air of cruelty? Hehe... I\'ll take that as a compliment.',
        'All those emotions that you\'ve bottled up through all those conflicts... Listen to my concert, and let it all out.',
        'Even should you anger me, I\'ll forgive you as long as you properly apologize.',
        'If you are ever afraid, come hide behind my back.',
        'Just like a baby... how sweet.',
        'My child, no matter what it is that you desire, I can help you obtain it.',
        'Now then, what kind of reward would you like?',
        'Welcome back. Whether it\'s good news or bad news, I\'d be glad to hear you out.',
        'Shall I sing the contents of this message for you?',
        'I do prefer this to fighting. Here, my child. Open your mouth~ ahhn~',
        'Please dote upon me more. Yes, more... more...!',
    ]
    
    if special == 'oath':
        quote = 'From now on, I shall share everything with you - your sorrow, your joy, your pain, and your pleasure. My child, I will always, always welcome you into my embrace...'
    elif special == 'chocolate':
        quote = 'My child, I have plenty of chocolate here. If you would like one - nay, if you would like for me to feed you more, just let me know. Relax, I shall allow whatever you wish, and I shall grant all of your desires...'
    else:
        quote = random.choice(friedrich_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'KMS Friedrich der Grosse:',
        description = quote ,
        colour = discord.Colour.red()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755410957391626300/Friedrich_der_GroeIcon.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='hammann')
async def hammannquote(ctx, special='no'):
    hammann_quotes_list = [
        'Hey! Don\'t stare at me like such an idiot, you pervert! ... I\'m cute? Did you really think just complimenting me would make me happy? You moron!',
        'How long were you going to keep me waiting?! Being alone feels so... Hmph!',
        'You pervert! What are you staring at?!',
        'Get ready for punishment if you open the window!',
        'Why won\'t you talk to me?',
        'I don\'t want you touching me, you pervert!',
        '*Picks up phone* Hello, is this Military Police? Yes, this Commander is a pervert and he...',
        'Go finish your missions already!',
        'Are you actually going to have me open the rewards for you?',
        'I brought your mail, Commander... Where\'s my "thanks"?!',
        'Good work... I-I didn\'t say anything! Get back to work, now!',
        'Hmph, flattering me won\'t get you anywhere!',
        'I\'m going to crush all of you weaklings!',
        'Hmph, did you really think this would be enough to make me happy?',
        '*Sob* ... Commander, you big idiot!',
        'I\'m not doing it just for you or anything like that!',
        'Why am I always so angry? Because a certain commander just won\'t learn! And I\'m angry at myself for not getting angry at him!',
        'If you\'re not looking at me, then at whom?! You just don\'t understand girls at all because you\'re so stupid! Just because I\'m not being proactive doesn\'t mean you... Wha?! Don\'t hug me all of a sudden... I-I\'ll call the police!',
    ]
    
    hammann_chocolate = [
        'I made this for you! ...I-if you don\'t want it, then I\'ll just eat it! ...You really don\'t want it? ...J-just eat it, you idiot!',
        'How long were you going to make Hammann wait?! I\'ve been trying to give you your chocolate for minutes now! W-what, you think I\'ve been hiding it behind my back this whole time? Of course not!',
    ]    
    
    if special == 'oath':
        quote = 'You\'ve finally learned, haven\'t you? I\'ll gratefully accept it... B-b-but I\'m not happy about it in the slightest!'
    elif special == 'chocolate':
        quote = random.choice(hammann_chocolate)
    else:
        quote = random.choice(hammann_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'USS Hammann:',
        description = quote ,
        colour = discord.Colour.blurple()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755414309768790025/HammannIcon.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='enterprise')
async def enterprisequote(ctx, special='no'):
    enterprise_quotes_list = [
        'I will continue to be victorious until the war ends.',
        'Want to look at my medal collection?',
        'Is it you, Commander? ...Recently, I\'m thinking about whether or not I can engage in anti-submarine actions...',
        'Luck is also a part of strength? Then if possible, I\'d like to impart some of it to my older sister.',
        'So long as we live, there are things that will never go our way. When we die, it must happen in a way that carries no regrets.',
        'What the...?!',
        'It\'s one battle after another, huh...',
        'I\'ve been on the battlefield for a long time, so I know about the importance of logistics. Commander, let\'s greet the girls who work hard behind the scenes.',
        'I will show you... what lies at the end of power',
        'Commander, tell me. How many more do I have to sink?',
        'Interesting...!',
        'All the lights in the sky are stars, just as all the lights on the seas are enemies... Commander, will there be a day where there\'s no more fighting?',
        'What do you want to do after the war? --Me? I\'ll probably stick with you. I feel the safest out of battle when I\'m with you. Will you... take me along with you?',
        'I\'m counting on you. Don\'t fall behind!',
        'All right, let me see what you\'re made of!',
        'Don\'t worry, I\'m right here.',
    ]    
    
    enterprise_chocolate = [
        'Valentine\'s chocolate for you. I put my all into making it, and I\'m confident that no other girl\'s chocolate is better than it. Eat it. Promise me.',
        'I\'ll be honest, I feel a bit weird about giving chocolate to you... Actually, never mind, don\'t worry about it. Obviously, my feelings play a big part in the making of this chocolate, but I got some recipe advice from my friends too. I hope you\'ll like it, Commander.',
    ]
         
    if special == 'oath':
        quote = 'I carry with me the hopes and wills of the countless battlefields and goodbyes that I have experienced. Commander, are you prepared to shoulder them all?... I see. Then let us walk together until the end of our lives.'
    elif special == 'chocolate':
        quote = random.choice(enterprise_chocolate)
    else:
        quote = random.choice(enterprise_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'USS Enterprise:',
        description = quote ,
        colour = discord.Colour.purple()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/756466402449162260/EnterpriseIcon.png')
    
    await ctx.send(embed=quoteembed)
    
@bot.command(name='belfast')
async def belfastquote(ctx, special='no'):
    belfast_quotes_list = [
        'Are you my master? Pleasure to meet you. I am Belfast the maid. From now on, I dedicate myself to you.',
        'Welcome back, master. I\'ve prepared the tea. Furthermore, I\'ve sorted the documents over here. Please work at your leisure.',
        'Is something the matter, master?',
        'In order to become an excellent master, you must start from self confidence. Please do your best to turn your will into action, master.',
        'Do you want some tea? Ah... if you want something else, I\'ll prepare some coffee or whiskey.',
        'Sunbathing on Thames river wasn\'t bad. But this current life of mine is better...',
        'Aimlessly touching a lady is not a gentlemanly behaviour. Please behave yourself around others.',
        'It\'s a maid\'s duty to dedicate her all to her master. Would you like to see, master?',
        'There\'s a new letter. Shall I read it for you, master?',
        'Welcome back, master. I\'ve readied some light snacks over here.',
        'Master, the ladies who went off for commissions have been waiting for you to greet them.',
        'I won\'t let you down.',
        'It\'s a maid\'s duty to remove their master\'s obstacles.',
        'Dear enemies, this is going to be a little bit painful',
        'I\'m mean, you say? Hehe. Recently I\'ve come to enjoy your troubled look a little. By all means, please forgive me.',
        'Are you awake? ...Hehe, your sleeping face was so cute, I couldn\'t bear waking you up... How did it feel, resting on my lap? You are free to enjoy it to your heart\'s content',
        'Such a willful appearance... a maid uniform is of course the appropriate dress for a maid, is it not?',
        'Do let us know if you have any needs that the Royal Maids might service.',
        'Welcome home, Master. You may rest easy knowing the Royal Maids are here to protect you.',
        
    ]    
    
    belfast_chocolate = [
        'Happy Valentine\'s Day, Master. I poured my gratitude and affection into this chocolate. It contains my feelings, humble as they may be. I ask you to be so gracious as to accept it.',
        'Master, you know, while we may be "ships," we are also "people," and as such we want to do things for those we cherish and respect, to express our gratitude, and our... love. What\'s that? I think saying anything more would be unbecoming of a Lady of the Royal Navy, don\'t you?',
    ]
         
    if special == 'oath':
        quote = 'Now this is a little troubling... I\'m fine with simply protecting you, my master, as well as occassionally enjoying your troubled look... But with such an important bond being formed, I\'ve become wanting to serve you even more, as well as receiving more of your attention, master...'
    elif special == 'chocolate':
        quote = random.choice(belfast_chocolate)
    else:
        quote = random.choice(belfast_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'HMS Belfast:',
        description = quote ,
        colour = discord.Colour.gold()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/756478237097328772/BelfastIcon.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='atago')
async def atagoquote(ctx, special='no'):
    atago_quotes_list = [
        'No matter the mission, just leave everything to big sister here~!',
        'Oh my, what a cute commander! Please allow your big sister Atago to take good care of you from now on!',
        'Welcome back! What should we do today?'
        'You shouldn\'t ask about a maiden\'s weight so casually~ *giggles*',
        'Commander~ I can see you ogling me in a daze, you know?',
        'Oh my~ Are you going to give me a massage?',
        'You can touch me even more if you\'d like... but there\'s no saying what might happen next... *giggles*',
        'Welcome back, Commander. Are you tired? Come bury yourself in big sister\'s bosom~!',
        'My whole body feels... hot... Commander, can you stay with me for a bit?',
        'Naughty children need to be punished~',
        'Ara Ara, how should I torment you today?',
        'Looks like big sis needs to get a little serious.',
        'You\'ve been naughty, Commander. Do you want to be punished so badly? *giggles*',
        'It\'s all your fault, Commander... If you make such a cute face, I won\'t be able to keep my hands off of you...',
        'It\'s no good... I can\'t control myself anymore! Commander, won\'t you become mine? You don\'t have to worry about anything... All you have to do is listen to me, and I\'ll satisfy all your needs...',
    ]    
    
    atago_chocolate = [
        'Did you enjoy Atago\'s chocolate? Ehehe, there\'s no way your big sister would forget about you, Commander~ As long as you open your mouth, I\'d be glad to deliver chocolate to you everyday~',
        'Hehe~ Now that you have my chocolate  is there anywhere special you want to go on our date? You thought I\'d let you go so easily after you took your big sister\'s chocolates?',
    ]
         
    if special == 'oath':
        quote = 'Oh my, you\'ve caught me, Commander. Or should I say, I\'ve finally caught you? Hehe~ I\'ll never let you go now!'
    elif special == 'chocolate':
        quote = random.choice(atago_chocolate)
    else:
        quote = random.choice(atago_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'IJN Atago:',
        description = quote ,
        colour = discord.Colour.gold()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/756478259838976060/AtagoIcon.png')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='shinobu')                    # Other
async def shinobuquote(ctx):
    shinobu_quotes_list = [
        'Panaino!',
        'Ka ka!',
        'It\'s not good to expect too much, but you can\'t do anything if you\'re being overly pessimistic. If you just wait thinking it\'s useless, nothing will come of it.',
        'It\'s difficult to change the world on your own, but twisting it a little might not be all that hard.',
        'There\'s no reason a fake can\'t do what the real thing would. And it\'s possible for a fake to be more real than the real thing.',
        'The sun is my enemy, but the moon has been good to me.',
        'We can\'t let the past be mere water under the bridge. Even so, there\'s no reason that we can\'t come together.',
    ]    
         
    quote = random.choice(shinobu_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'Shinobu Oshino:',
        description = quote ,
        colour = discord.Colour.gold()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755425581407141888/shinobu_icon.jpg')
    
    await ctx.send(embed=quoteembed)

@bot.command(name='rias')
async def riasquote(ctx):
    rias_quotes_list = [
        'We haven\'t lost yet! You lose when you\'ve given up!',
        'The first strike decides the battle.',
        'Devote your life to me.',
        'My name is Rias Gremory. And I am a Devil.',
        'Even a pawn can take down a king.',
        'Insulting my servants warrants death.',
        'I\'ll get right to the point: We\'re all devils.',
        'You have to forget about that girl. You are a member of the Gremory family now.',
        'For me, live on.',
    ]    
       
    quote = random.choice(rias_quotes_list)
        
    quoteembed = discord.Embed(
        title = 'Rias Gremory:',
        description = quote ,
        colour = discord.Colour.dark_red()
    )
    
    quoteembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/755408029855252550/755452514694070292/Riasicon.png')
    
    await ctx.send(embed=quoteembed)

# Stuff 2 - The Return of Stuff
bot.run(TOKEN)