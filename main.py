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
upvote = "<:upvote:726140828090761217>"
downvote = '<:downvote:726140881060757505>'
reddit = praw.Reddit(client_id='ID',
                     client_secret='Secret',
                     user_agent='Tech-Bot')
#------------------------Start---------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f".help (on {len(client.guilds)} servers)"))
    print('Bot online, lets hope you wont cry.')
#-------------------------Reddit stuff--------------------------------------------
@client.command()
async def pokimane(ctx):
    memes_submissions = reddit.subreddit('pokimanehot').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

@client.command()
async def linuxmeme(ctx):
    memes_submissions = reddit.subreddit('linuxmemes').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

@client.command()
async def muta(ctx):
    memes_submissions = reddit.subreddit('SomeOrdinaryGmrs').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

#------------------------------Moderation------------------------------------------
@client.command()
@has_permissions(administrator=True)
async def rm(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
    sent = await ctx.send(F"I deleted `{amount}` messages")
    sleep(1)
    await sent.delete()
@client.command()
@has_permissions(administrator=True)
async def sudo(ctx,*,arg):
    if arg == "rm -rf /*":
        amount = 100
        await ctx.channel.purge(limit=amount)

@client.command()
@has_permissions(administrator=True)
async def kick(ctx,member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} kicked !')
@client.command()
@has_permissions(administrator=True)
async def ban(ctx,member : discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044 {member.mention} Banned!')
@client.command()
@has_permissions(administrator=True)
async def mute(ctx,member : discord.Member, *, reason = None):
    await ctx.guild.create_role(name='muted', permissions=discord.Permissions(0))
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send(f'https://tenor.com/view/turn-down-volume-mute-volume-gif-14268149 {member.mention} Muted!')

@client.command()
@has_permissions(administrator=True)
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:

        user = ban_entry.user

        await ctx.guild.unban(user)

        await ctx.send(f'{user.mention} Unbanned!.')

#-------------------------Features-----------------------------------------------------------------

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong **{round(client.latency * 1000)}ms**')
@client.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def compgen(ctx,*,arg):
    if arg == "-c":
        await ctx.send("https://fossbytes.com/a-z-list-linux-command-line-reference/")
@client.command()
async def github(ctx):
    await ctx.send("This bot is not forked anymore: https://github.com/Abb1x/Ububot Here: https://github.com/PhereloHD/Tech-Bot ")

#------------------Features that are getting Tested/Secrets-----------------------------------------------------------

@client.command()
async def nam(ctx):
     await ctx.send("Error")

@client.command ()
async def test(ctx):
    await ctx.send("Testing in Progress!")

@client.command ()
async def picard(ctx):
    await ctx.send("Make it so!")

@client.command ()
async def spock(ctx):
    await ctx.send("Live Long and Prosper!")

@client.command ()
async def story(ctx):
    a = ["You killed yourself. F", "You don't know what to do, so you decided to Program a Discord-Bot", "You went out to watch Pokimane's livestream."]
    await ctx.send(random.choice(a))

@client.command ()
async def quotes(ctx):
    q = ["**Talk is cheap. Show me the code.** -Linus Torvalds", "**When you don't create things, you become defined by your tastes rather than ability. your tastes only narrow & exclude people. so create.** - Why The Lucky Stiff", "**Programs must be written for people to read, and only incidentally for machines to execute.** - Harold Abelson, Structure and Interpretation of Computer Programs"]
    await ctx.send(random.choice(q))

@client.command ()
async def site(ctx):
    await ctx.send("https://www.tuxbot.tech/")


@client.command ()
async def fuckyou(ctx):
    await ctx.send("no u m8")


@client.command ()
async def greekgodx(ctx):
    await ctx.send("fatass")

@client.command ()
async def god(ctx):
    await ctx.send("https://github.com/torvalds/linux")



#---------------------Errors---------------------------------------------------
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description=":x: │ **This command does not exist**",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description=f":x: │ **{ctx.message.author.mention} is not in the sudoers file.This incident will be reported.**",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description=f":x: │ **Missing required arguments**",colour=discord.Colour.red())
        await ctx.send(embed=embed)


#------------------------------------------Docs----------------------------------------------------------------------

@client.command()
async def docs(ctx,*,arg):
    if arg == "Ubuntu":
        await ctx.send("Here are the officials docs for Ubuntu : https://docs.ubuntu.com/")
    if arg == "Popos":
        await ctx.send("Here are the officials docs for PopOS : https://pop.system76.com/docs/")
    if arg == "Debian":
        await ctx.send("Here are the officials docs for Debian : https://www.debian.org/doc/")
    if arg == "Elementaryos":
        await ctx.send("Here are the officials docs for ElementaryOS : https://elementary.io/docs")
    if arg == "Kubuntu":
        await ctx.send("Here are the officials docs for Kubuntu : https://wiki.kubuntu.org/Kubuntu/KubuntuDocs")
    if arg == "Lubuntu":
        await ctx.send("Here are the officials docs for lubuntu : https://docs.lubuntu.net/")
    if arg == "Xubuntu":
        await ctx.send("Here are the officials docs for Xubuntu: https://docs.xubuntu.org")
    if arg == "Arch":
        await ctx.send("Here are the officials docs for Arch: https://wiki.archlinux.org/")
    if arg == "Manjaro":
        await ctx.send("Here are the official docs for Manjaro: https://manjaro.org/ ")


@docs.error
async def docs_error(ctx,error) :
    if isinstance(error, commands.MissingRequiredArgument):
            author = ctx.message.author
            embed = discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name='Available distro docs:')
            embed.add_field(name='Ubuntu',value = "ubuntu",inline=False)
            embed.add_field(name='Debian',value = "debian", inline=False)
            embed.add_field(name='PopOS',value = "popos",inline=False)
            embed.add_field(name='ElementaryOS',value = "elementaryos",inline=False)
            embed.add_field(name='Kubuntu',value = "kubuntu",inline=False)
            embed.add_field(name='lubuntu',value = "lubuntu",inline=False)
            embed.add_field(name='Xubuntu',value = "xubuntu",inline=False)
            embed.add_field(name='Arch',value = "Arch",inline=False)
            embed.add_field(name='Manjaro',value = "Manjaro",inline=False)
            await ctx.send(embed=embed)
#----------------------------Help---------------------------------------------------------------------------------------
@client.command()
async def help(ctx):
    author = ctx.message.author
    await author.create_dm()
    embed = discord.Embed(
    colour = discord.Colour.green()
    )
    embed.set_author(name='List of commands')
    embed.add_field(name='ban', value='Bans a member', inline=False)
    embed.add_field(name='unban', value='Unbans a member', inline=False)
    embed.add_field(name='kick', value='Kicks a member', inline=False)
    embed.add_field(name='mute', value='Mutes a member', inline=False)
    embed.add_field(name='rm <amount>', value='Purge a number of messages', inline=False)
    embed.add_field(name='echo', value='Copies your message', inline=False)
    embed.add_field(name='sudo rm -rf /*', value='Deletes 100 messages', inline=False)
    embed.add_field(name='ping', value='Returns pong!', inline=False)
    embed.add_field(name='compgen -c', value='Gives you a list of linux commands', inline=False)
    embed.add_field(name='docs <distro>', value='Send you a link of officials docs of chosen distro (no value = list of distros)', inline=False)
    embed.add_field(name='linuxmeme', value='gives you a random linux meme', inline=False)
    embed.add_field(name='muta', value='Random SomeOrdinaryGamer memes.', inline=False)
    embed.add_field(name='pokimane', value='You do not wanna know that.', inline=False)
    embed.add_field(name='meme', value='Gives you a random meme.', inline=False)
    embed.add_field(name='story', value='Gives you a story.', inline=False)
    embed.add_field(name='picard', value='MAKE IT SO!', inline=False)
    embed.add_field(name='spock', value='Live Long and Prosper!', inline=False)
    embed.add_field(name='quote', value='Gives you a random Programing quote', inline=False)
    embed.add_field(name='god', value='Gives you the Github Profile of Linus Torvalds', inline=False)
    embed.add_field(name='nam', value='Error', inline=False)
    embed.add_field(name='Extras!', value='There are some secret features with the commands so test and try to find them out!', inline=False)
    await ctx.send(embed=embed)
    
#---------------------------------------------END-----------------------------------------------------



client.run('Token')
