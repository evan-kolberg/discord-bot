# https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg
import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)

client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(
        activity=discord.Streaming(name="Stuff, use .help ", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))


# ---------

# Events in console for join and leave

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')


# ---------

# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=["?"])
async def help(ctx):
    await ctx.send(
        "**Help Menu:**\n.help - Shows this menu\n.ping - Shows bot ping\n.8ball {Question} - Answers your question randomly\n.specialcommands - Shows a list of commands that require permissions")


@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount + 1)


@clear.error
async def clear_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


@client.command(aliases=['sc'])
async def specialcommands(ctx):
    await ctx.send(
        "**Special Commands**:\n.clear {Amount} - Clears messages - Requires *Manage Messages*\n.kick - Kicks members - Requires *Kick Members*\n.ban - Bans members - Requires *Ban Members*\n.unban - Unbans members - Requires *Ban Members*")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@kick.error
async def kick_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@ban.error
async def ban_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


@client.command(aliases=['pardon'])
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            return

token = input("What is the bot token?: ")
client.run(token)
# hi

