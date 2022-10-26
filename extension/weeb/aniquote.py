import discord
import random
import aiohttp
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command


class AniquoteCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "aniquote", 
        description = "To get anime quotes"
    )
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.cooldown(1, 36, commands.BucketType.default)
    async def aniquote(
        self, ctx, *, 
        character: discord.Option(str, 'You want quote of which anime character?', required=False, default=None)
    ):
        try:

            if character is not None:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(
                        f"https://animechan.vercel.app/api/quotes/character?name={character}"
                    )
                    data = await response.json(content_type=None)

                    embed = discord.Embed(
                        title=f"<:Yay:881813475238748211> {random.choice(data)['character']}",
                        description=random.choice(data)["quote"],
                        colour=discord.Color.blue(),
                    )
                    embed.add_field(
                        name="<:Anime:881813511414611968> Anime:",
                        value=random.choice(data)["anime"],
                    )
                    await ctx.respond(embed=embed)

            else:

                async with aiohttp.ClientSession() as session:
                    response = await session.get(
                        "https://animechan.vercel.app/api/random"
                    )
                    data = await response.json(content_type=None)
                    embed = discord.Embed(
                        title=f"<:Yay:881813475238748211> {data['character']}",
                        description=data["quote"],
                        colour=discord.Color.blue(),
                    )
                    embed.add_field(
                        name="<:Anime:881813511414611968> Anime:", value=data["anime"]
                    )
                    await ctx.respond(embed=embed)

        except KeyError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        except IndexError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        else:
            pass


def setup(bot):
    bot.add_cog(AniquoteCmd(bot))
