import discord
import aiohttp
from akito import prefix
from discord.ext import commands


class PotionCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin potion command
    (
        name="genshinpotion", 
        aliases=["gp", "gpotion", "genshinimpactpotion"],
        description="Genshin Impact Potion Info",
        usage = "[Potion Name]",
        help = "If `Potion Name` is not provided, it shows list of available potions.")
    
    async def gpotion(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/consumables/potions"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            potions = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:BarbaraPoint:889078048362733580> Genshin Impact: Potions",
                colour=discord.Color.blue(),
                description=f"**__Name__ of Potions:**\n"
                f"{potions}\n"
                f"\n**To Get Info:**\n"
                f"`/gpotion [name]`\n",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = "https://api.genshin.dev/consumables/potions"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)
                    data = data[search]

                    craft = "\n".join(
                        [f"{i['item']} x {i['quantity']}" for i in data["crafting"]]
                    )

                    embed = discord.Embed(
                        title=f"{data['rarity']} ⭐ {data['name']}",
                        colour=discord.Color.blue(),
                        description=f"{data['effect']}\n"
                        f"\n**Crafting:**\n"
                        f"{craft}\n",
                    )

                    embed.set_thumbnail(
                        url=f"https://api.genshin.dev/consumables/potions/{search}"
                    )
                    await ctx.respond(embed=embed)

            # except KeyError:
            #     embed = discord.Embed(
            #         title=f"<:oh:881566351783780352> Data Not Found",
            #         colour = discord.Color.red(),
            #         description=f"{ctx.author.mention} I don't seem to find data for `{search}`"
            #         f"\nPlease check spelling again in `/gpotion`")
            #     embed.set_footer(text=f"Join My Server For Additional Help!")
            #     embed.set_author(name = ctx.author , icon_url = ctx.author.display_avatar)
            #     await ctx.respond(embed=embed, =60)

            except:
                raise


def setup(bot):
    bot.add_cog(PotionCmd(bot))
