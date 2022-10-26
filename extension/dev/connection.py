import discord
from akito import Var, __version__
from discord.ext import commands
from asyncio import sleep

class ConnectionHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        print(f"{self.bot.user} Connected.")
        
        channel = self.bot.get_channel(Var.connect_logger.value)
        embed = discord.Embed(
            title="Bot Connected!",
            colour=discord.Color.green(),
            description=f"**Guilds**: {len(self.bot.guilds)}\n"
        )
        await channel.send(embed=embed)
        
        while True:
            await self.bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f"Akito Shutting Down Soon!",
                )
            )
            await sleep(6)
            await self.bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f"discord.gg/ceila for Updates & New Akito",
                )
            )
            await sleep(15)

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.bot.user} Disconnected.")

        channel = self.bot.get_channel(Var.connect_logger.value)
        embed = discord.Embed(
            title="Bot Disconnected!",
            colour=discord.Color.red(),
            description=f"**Guilds**: {len(self.bot.guilds)}\n"
        )
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_resumed(self):
        print(f"{self.bot.user} Reconnected.")

        channel = self.bot.get_channel(Var.connect_logger.value)
        embed = discord.Embed(
            title="Bot Reconnected!",
            colour=discord.Color.gold(),
            description=f"**Guilds**: {len(self.bot.guilds)}\n"
        )
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ConnectionHandler(bot))
