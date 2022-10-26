import aiohttp
import discord
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command

class AnimeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "anime", 
        description = "To get anime info"
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.cooldown(5, 1, commands.BucketType.default)
    async def anime(
        self, ctx, *, 
        name: discord.Option(str,'Name of the anime', required=True)
    ):

        try:

            async with aiohttp.ClientSession() as session:
                response = await session.get(
                    f"https://kitsu.io/api/edge/anime?filter[text]={name}"
                )
                
                data = await response.json(content_type=None)
                anime = data["data"][0]

            async with aiohttp.ClientSession() as session:
                url = f"https://kitsu.io/api/edge/anime/{int(anime['id'])}/genres"
                Response = await session.get(url)
                Data = await Response.json(content_type=None)
                Anime = Data["data"]

            titleedit = anime["attributes"]["slug"].replace(" ", "-")
            titleurl = f"https://kitsu.io/anime/{titleedit}"

            embed = discord.Embed(
                title=anime["attributes"]["canonicalTitle"],
                url=titleurl,
                description=anime["attributes"]["synopsis"],
                colour=discord.Color.blue(),
            )

            embed.add_field(name="📅 Start Date", value=anime["attributes"]["startDate"])
            embed.add_field(name="⏳ Status", value=anime["attributes"]["status"])
            embed.add_field(name="🗓️ End Date", value=anime["attributes"]["endDate"])
            embed.add_field(name="🏆 Popularity Rank", value=anime["attributes"]["popularityRank"])
            embed.add_field(name="⭐ Rating Rank", value=anime["attributes"]["ratingRank"])
            embed.add_field(name="🗂️ Type", value=anime["attributes"]["subtype"])
            embed.add_field(name="💽 Episode Count", value=anime["attributes"]["episodeCount"])

            length = anime["attributes"]["episodeLength"]
            embed.add_field(name="⌚ Episode Length", value=f"{length} min")

            total = anime["attributes"]["totalLength"]
            embed.add_field(name="⏲️ Total Length", value=f"{total} min")

            avgrating = anime["attributes"]["averageRating"]
            embed.add_field(name="💯 Avg. Rating", value=f"{avgrating}/100")

            embed.add_field(name="®️ Age Rating", value=anime["attributes"]["ageRating"])

            genre = ", ".join([i["attributes"]["name"] for i in Anime])
            if not genre:
                genre = "Data Not Available"
            embed.add_field(name="🧬 Genre", value=genre)

            altitle = ", ".join(
                [
                    f"{i}" for i in anime["attributes"]["titles"].values() if i is not None
                ]
            )
            embed.add_field(name="🪢 Other Titles", value=altitle)

            embed.set_thumbnail(url=anime["attributes"]["posterImage"]["original"])

            if anime["attributes"]["coverImage"] == None:
                imageurl = anime["attributes"]["posterImage"]["original"]
            else:
                imageurl = anime["attributes"]["coverImage"]["original"]

            embed.set_image(url=imageurl)

            YtID = anime["attributes"]["youtubeVideoId"]
            button = discord.ui.View()
            if YtID:
                link = f"https://www.youtube.com/watch?v={YtID}"
                button.add_item(item=discord.ui.Button(
                        emoji="<:youtube:314349922885566475>", label="YouTube", url=link)
                )

            await ctx.respond(embed=embed, view=button)

        except KeyError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        except IndexError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        else:
            pass

def setup(bot):
    bot.add_cog(AnimeCmd(bot))
