import discord
import os
import json
import praw
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
reddit = praw.Reddit(client_id='mq3IHq-iSdxquw',
                     client_secret='MASkagROt68WoC-_pi-bm7SZmbY',
                     user_agent='Tech-Bot')
#------------------------Start--------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'Laughing at Windows users...'))
    print('Bot online, lets hope you wont cry.')
    
#-------------------------Reddit stuff------------------------------------------
@client.command ()
async def linuxmeme(ctx):
    memes_submissions = reddit.subreddit('linuxmemes').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)


@client.command ()
async def historymeme(ctx):
    memes_submissions = reddit.subreddit('historymemes').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

@client.command ()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').top()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

#------------------------------Moderation------------------------------------------
@client.command ()
@has_permissions(administrator=True)
async def rm(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
    sent = await ctx.send(f'I deleted `{amount}` messages')
    sleep(1)
    await sent.delete()
@client.command ()
@has_permissions(administrator=True)
async def doas(ctx,*,arg):
    if arg == "rm -rf /*":
        amount = 100
        await ctx.channel.purge('***See you in the Bunker!***')
        await ctx.channel.purge(limit=amount)


#-------------------------Features-----------------------------------------------------------------

@client.command ()
async def ping(ctx):
    await ctx.send(f'This does not mean anything really. **{round(client.latency * 1000)}ms**')

@client.command ()
async def echo(ctx, *, message: str):
    if not ("@" in message):
        await ctx.send(message)
    else:
        await ctx.send("**Sorry, but you can't @ with echo.**")
        
@client.command ()
async def compgen(ctx,*,arg):
    if arg == '-c':
        await ctx.send('https://fossbytes.com/a-z-list-linux-command-line-reference/')


#------------------Features-----------------------------------------------------------
@client.command ()
async def github(ctx):
    await ctx.send("https://github.com/PhereloHD/Tech-Bot/")


@client.command ()
async def nam(ctx):
     await ctx.send('Error')

@client.command ()
async def test(ctx):
    await ctx.send('nice you didn\'t do something bad')

@client.command ()
async def picard(ctx):
    await ctx.send('Make it so!')

@client.command ()
async def spock(ctx):
    await ctx.send('Live Long and Prosper!')

@client.command ()
async def quotes(ctx):
    q = ["**Talk is cheap. Show me the code.** -Linus Torvalds", "**When you don't create things, you become defined by your tastes rather than ability. your tastes only narrow & exclude people. so create.** - Why The Lucky Stiff", "**Programs must be written for people to read, and only incidentally for machines to execute.** - Harold Abelson, Structure and Interpretation of Computer Programs"]
    await ctx.send(random.choice(q))


@client.command ()
async def fuckyou(ctx):
    await ctx.send('no u m8')

@client.command ()
async def god(ctx):
    await ctx.send("https://github.com/torvalds/linux")

@client.command ()
async def ara(ctx):
    await ctx.send('YOU SUMMONED AKENO!!!')
    await ctx.send("https://www.anime-planet.com/images/characters/akeno-himejima-34165.jpg?t=1545970466")

@client.command ()
async def simp(ctx):
    simprate = random.randint(0,100)
    await ctx.send(f"{ctx.message.author.mention} **Your simprate: " + str(simprate) + " %**")


@client.command ()
async def whoAmI(ctx):
   await ctx.send(f'You are {ctx.message.author.mention}')

#-------------------------------Rules--------------------------------------------------------
@client.command ()
async def r(ctx, arg):
    if arg == "1":
        await ctx.send('**1. No spam!**')
    if arg == "2":
        await ctx.send('**2. No griefing!**')
    if arg == "3":
        await ctx.send('**3. No insults!**')
    if arg == "4":
        await ctx.send('**4. No successive voice switching!**')
    if arg == "5":
        await ctx.send('**5. No voice distortion or soundboard!**')
    if arg == "6":
        await ctx.send('**6. No CAPS!**')
    if arg == "7":
        await ctx.send('**7. No Zalgo!**')
    if arg == "8":
        await ctx.send('**8. No hassle!**')
    if arg == "9":
        await ctx.send("**9. Don't bother anyone!**")
    if arg == "10":
        await ctx.send("**10. Don't slander anyone**")
    if arg == "11":
        await ctx.send("**11. Don't press anyone**")
    if arg == "12":
        await ctx.send('**12. Follow the guidelines! https://discordapp.com/guidelines **')
    if arg == "13":
        await ctx.send('**13. Worship Abbix**')
    if arg == "34":
        await ctx.send('**You sick fuck**')
#---------------------Errors---------------------------------------------------
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description="***Nice try*** │ **This command does not exist**",colour=discord.Colour.blue())
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description=f"***Report incoming*** │ **{ctx.message.author.mention} Is not an Admin**",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description=f"**F** │ **Missing required arguments**",colour=discord.Colour.green())
        await ctx.send(embed=embed)



#----------------------------Help---------------------------------------------------------------------------------------
@client.command()
async def help(ctx,*,arg):    
    if arg == 'linux':
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.green()
        )
        embed.set_author(name='List of Linux and Management commands')
        embed.add_field(name='rm <amount>', value='Purge a number of messages', inline=False)
        embed.add_field(name='echo', value='Speaks after you', inline=False)
        embed.add_field(name='doas rm -rf /*', value='Deletes 100 messages', inline=False)
        embed.add_field(name='compgen -c', value='Gives you a list of linux commands', inline=False)
        embed.add_field(name='linuxmeme', value='gives you a random linux meme', inline=False)
        await ctx.send(embed=embed)

    if arg == "misc":
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.green()
         )
        embed=discord.Embed(title='Misc', description='Misc commands ', inline=False)
        embed.set_author(name='List of misc commands')
        embed.add_field(name='quotes', value='Gives you legendary Quotes', inline=False)
        embed.add_field(name='god', value="Gives you the Linux Kernel source code", inline=False)
        embed.add_field(name='nam', value="Error", inline=False)
        embed.add_field(name='picard', value="Gives you Motivation", inline=False)
        embed.add_field(name='ping', value="This doesn't mean anything really", inline=False)
        embed.add_field(name='ara', value="It's Punga's Fault", inline=False)
        embed.add_field(name='r ', value="r + Rule number to get the listed Rules", inline=False)
        embed.add_field(name='spock', value='Gives you Motivation', inline=False)
        embed.add_field(name='simp', value='Gives you your simprate', inline=False)
        embed.add_field(name='whoAmI', value='What do you expect?', inline=False)
        embed.add_field(name='meme', value='Gives you a random meme. Fresh from Reddit', inline=False)
        await ctx.send(embed=embed)
        
    
#---------------------------------------------END-----------------------------------------------------



client.run('token')
