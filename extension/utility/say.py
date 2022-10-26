import discord
from akito import final
from discord.ext import commands
from discord.commands import slash_command

class SayCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "say",
        description = "To say anything as bot"
    )
    @commands.guild_only()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def say(
        self, ctx, 
        *message: discord.Option(str, 'Message that you want the \'bot\' to say', required=True)
    ):
        try:
            id = int(str(message[0]).replace("<#", "").replace(">", ""))
            channel = self.bot.get_channel(id)
            message = (
                str(message[1:])
                .replace("('", "")
                .replace("',)", "")
                .replace(", ", " ")
                .replace("')", "")
                .replace("'", "")
                .replace("()", "** **")
            )
            await channel.send(f"{message}")

        except:
            message = (
                str(message)
                .replace("('", "")
                .replace("',)", "")
                .replace(", ", " ")
                .replace("')", "")
                .replace("'", "")
                .replace("()", "** **")
            )
            await ctx.respond(f"{message}")

def setup(bot):
    bot.add_cog(SayCmd(bot))
