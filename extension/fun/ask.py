import json
import akito
import random
import discord
from discord.ext import commands
from discord.commands import slash_command


class _8BallCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "ask", 
        description = "Random Answers To Your Questions."
    )
    async def ask(self, ctx, *, question):
        with open("data/CmdData.json", "r", encoding="utf-8") as f:
            # the data folder has been deleted & not provided in this public repo
            data = json.load(f)
            response = random.choice(data["ask"])


        embed = discord.Embed(
            title=f"🤔 {question}",
            description=f"😎 **{response}**",
            colour=discord.Color.blue(),
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(_8BallCmd(bot))
