import discord
import aiohttp
from akito import Embed, prefix
from discord.ext import commands


class GWeaponCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin weapons command
    (
        name="genshinweapon", 
        aliases=["gw", "gweapon", "genshinimpactweapon"],
        description = "Genshin Impact Potion Info",
        usage = "[Weapon Name]",
        help = "If `Weapon Name` is not provided, it shows list of available weapons.")
    
    async def gweapon(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/weapons"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            weapons = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:DilucWave:889078733636534272> Genshin Impact: Weapons",
                colour=discord.Color.blue(),
                description=f"**__Name__ of Weapons:**\n"
                f"{weapons}\n"
                f"\n**To Get Info:**\n"
                f"`/gweapon [name]`\n",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = f"https://api.genshin.dev/weapons/{search}"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)

                    embed = discord.Embed(
                        title=f"{data['rarity']} ⭐ {data['name']} | {data['passiveName']}",
                        colour=discord.Color.blue(),
                        description=data["passiveDesc"],
                    )
                    embed.add_field(name="🌀 Type", value=data["type"])
                    embed.add_field(name="💫 Stat", value=data["subStat"])
                    embed.add_field(name="📌 Location", value=data["location"])

                    embed.set_thumbnail(url=f"{url}/icon")
                    await ctx.respond(embed=embed)

            except KeyError:
                embed = await Embed.datanotfound(self, ctx)
                await ctx.respond(embed=embed, =60)

            except:
                raise


def setup(bot):
    bot.add_cog(GWeaponCmd(bot))
