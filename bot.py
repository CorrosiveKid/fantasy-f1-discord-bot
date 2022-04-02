import os

import discord
import flag
import requests
from discord.ext import commands
from dotenv import load_dotenv
from table2ascii import table2ascii

load_dotenv()

description = """Fantasy F1 leaderboard bot."""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", description=description, intents=intents)

bot_token = os.getenv("BOT_TOKEN")
cookie = os.getenv("COOKIE")
league_id = os.getenv("LEAGUE_ID")
f1_season = os.getenv("F1_SEASON")


async def fetch_f1_data():
    """Fetch the fantasy F1 league data from the API."""
    headers = {"Cookie": cookie}
    response = requests.get(
        f"https://fantasy-api.formula1.com/f1/{f1_season}/leaderboards/leagues?v=1&league_id={league_id}",
        headers=headers,
    )
    return response.json()


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def leaderboard(ctx):
    """Send the fantasy f1 leaderboard as a message."""
    data = await fetch_f1_data()
    leaderboard_entrants = data["leaderboard"]["leaderboard_entrants"]
    league_name = data["leaderboard"]["league_name"]
    output = table2ascii(
        header=["Team", "Score"],
        body=[
            [
                f"{flag.flag(entrant['user_country'])}{entrant['username']}[{entrant['team_name']}]",
                entrant["score"],
            ]
            for entrant in leaderboard_entrants
        ],
    )
    await ctx.send(
        f"🏁 Fantasy Formula 1 Leaderboard - {league_name} 🏁\n```\n{output}\n```"
    )


bot.run(bot_token)
