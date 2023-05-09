# Import necessary libraries
import discord
from discord import player
from discord import colour
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random

# List of all possible game moves
GAMES=["rock","paper","scissors"]

# Initialize the bot with command prefix '>>' and disable the default help command
client=commands.Bot(command_prefix=">>", help_command=None)

# Event that's called when the bot has connected to the server and is ready
@client.event
async def on_ready():
    # Set bot's activity status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=">>help"))
    print("We Are Ready Now")

# Define the 'help' command
@client.command(name="help")
async def _help(ctx):
    # Create an embedded message (a rich-content message)
    embed=discord.Embed(name="Help Commands")
    # Add a field to the embedded message explaining the play command
    embed.add_field(
        name="Play A Game",
        value="**`play [your move]`**, **`p [your move]`**, **`game [your move]`**",
        inline=False
    )
    # Set author's name and icon for the embedded message
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    # Set footer text and icon for the embedded message
    embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    # Send the embedded message
    await ctx.send(embed=embed)




# Define the 'play' command, with aliases 'p' and 'game'
@client.command(name="play",aliases=["p","game"],pass_context=True)
async def _play(ctx,move):
    # Choose a random move for the bot
    computer=random.choice(GAMES)
    # Create an embedded message for the game result
    embed=discord.Embed(name="Moves",colour=discord.Color.dark_grey())

    # Check the player's move and determine the game result
    if move.lower() not in ["rock","paper","scissors"]:
        await ctx.send("You Should Use [**`rock`**,**`paper`**,**`scissors`**]")
    elif move.lower() == "rock":
        if computer == "scissors":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "paper":
            res=("<@851920383723831356> Wins!")
    elif move.lower() == "paper":
        if computer == "rock":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "scissors":
            res=("<@851920383723831356> Wins!")
    elif move.lower() == "scissors":
        if computer == "paper":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "rock":
            res=("<@851920383723831356> Wins!")
    else:
        await ctx.send("Something Went Wrong!")

    # Prepare and send the game result
    embed.add_field(
        name="Players Moves",
        value=f"""
{ctx.author.mention} Choice => **{move}**,

<@851920383723831356> Choice => **{computer}**

**Result is:** => **{res}**

        """
    )
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://pxt.azureedge.net/blob/68f66c3ddc3acfc4c53157abf92eace202d46db2/static/courses/csintro/conditionals/rock-paper-scissors-items.png")
    # Send the game result
    await ctx.send(embed=embed)

# Handle errors that occur during the 'play' command
@_play.error
async def _play_error(ctx, error):
    # If the user didn't provide a move, send an error message
    if isinstance(error,commands.MissingRequiredArgument):
        print("We Have An Error, Missing Bad Arguments")
        await ctx.send("Please Compelete Required Argument")
    # If the user provided an invalid argument, send an error message    
    elif isinstance(error,commands.BadArgument):
        print("We Have An Error, Bad Argument")
        await ctx.send("Bad Arguments")
# Run the bot
client.run("your token")
