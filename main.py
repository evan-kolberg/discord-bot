'''
This program operates a Discord Python bot that users can interact with within a server
'''
import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')


# Confirms that the bot working properly
@client.event
async def on_ready():
    print('Online')
    await client.change_presence(
        activity=discord.Streaming(name="Stuff, use .help ", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))


# ---------
# Events in console for join and leave

# When a member joins the server, the bot will welcome them
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server. Welcome!!!')


# When a member leaves the server, the bot will note their absence
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server. Do not worry, he will be back soon')


# ---------
# Commands

# The ping command to test latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


# 8ball command - The user asks a question and the bot will give a random response as an 8 ball would
@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
                 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
                 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# help command -
@client.command(aliases=["?"])
async def help(ctx):
    await ctx.send(
        "**Help Menu:**\n.help - Shows this menu\n.ping - Shows bot ping\n.8ball {Question} - Answers your question randomly\n.specialcommands - Shows a list of commands that require permissions")


# Destroys a channel - purges thus channel
@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount + 1)


# Bot sends error command to inform user that they do not have high enough permissions
@clear.error
async def clear_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


# Special commands - Displays list of commands that the user can operate
@client.command(aliases=['sc'])
async def specialcommands(ctx):
    await ctx.send(
        "**Special Commands**:\n.clear {Amount} - Clears messages - Requires *Manage Messages*\n.kick - Kicks members - Requires *Kick Members*\n.ban - Bans members - Requires *Ban Members*\n.unban - Unbans members - Requires *Ban Members*")


# The user can ask the bot to kick a user with correct permissions
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


# Displays an error if the user does not have the correct permissions needed to perform the kick command
@kick.error
async def kick_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


# The user can ask the bot to ban a user with correct permissions
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def devban9261(ctx, member: discord.Member, *, reason=None):
    await member.devban9261(reason=reason)




# Displays an error if the user does not have the correct permissions needed to perform the ban command
@ban.error
async def ban_error(ctx, error):
    await ctx.send(
        "Either you do not have permission to run this command, your syntax was invalid, or there was an error.")


# Unban command - with banning powers, a user can unban a member of the server
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


# Asks the user for a token for the bot to run
token = input("What is the bot token?: ")
# Runs the client with the token
client.run(token)
import turtle
while True:
    turtle.forward(100)
    turtle.backward(100)
