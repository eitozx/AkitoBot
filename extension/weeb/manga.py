import aiohttp
import discord
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command


class MangaCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "manga", 
        description = "To get manga info"
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.cooldown(5, 1, commands.BucketType.default)
    async def manga(
        self, ctx, *, 
        name: discord.Option(str,'Name of the manga', required=True)
    ):
        try:

            async with aiohttp.ClientSession() as session:
                response = await session.get(
                    f"https://kitsu.io/api/edge/manga?filter[text]={name}"
                )
                data = await response.json(content_type=None)
                manga = data["data"][0]

            async with aiohttp.ClientSession() as session:
                url = f"https://kitsu.io/api/edge/manga/{int(manga['id'])}/genres"
                Response = await session.get(url)
                Data = await Response.json(content_type=None)
                Manga = Data["data"]

            titleedit = manga["attributes"]["slug"].replace(" ", "-")
            titleurl = f"https://kitsu.io/manga/{titleedit}"

            embed = discord.Embed(
                title=manga["attributes"]["canonicalTitle"],
                url=titleurl,
                description=manga["attributes"]["synopsis"],
                colour=discord.Color.blue(),
            )

            embed.add_field(name="📅 Start Date", value=manga["attributes"]["startDate"])
            embed.add_field(name="⏳ Status", value=manga["attributes"]["status"])
            embed.add_field(name="🗓️ End Date", value=manga["attributes"]["endDate"])
            embed.add_field(
                name="🏆 Popularity Rank", value=manga["attributes"]["popularityRank"]
            )
            embed.add_field(
                name="⭐ Rating Rank", value=manga["attributes"]["ratingRank"]
            )
            embed.add_field(name="🗂️ Type", value=manga["attributes"]["subtype"])

            avgrating = manga["attributes"]["averageRating"]
            embed.add_field(name="💯 Avg. Rating", value=f"{avgrating}/100")

            volume = manga["attributes"]["volumeCount"]
            chapter = manga["attributes"]["chapterCount"]
            embed.add_field(name="📚 Vol. | Chp.", value=f"{volume} | {chapter}")

            embed.add_field(
                name="®️ Age Rating", value=manga["attributes"]["ageRating"]
            )

            genre = ", ".join([i["attributes"]["name"] for i in Manga])
            if not genre:
                genre = "Data Not Available"
            embed.add_field(name="🧬 Genre", value=genre)

            altitle = ", ".join(
                [
                    f"{i}"
                    for i in manga["attributes"]["titles"].values()
                    if i is not None
                ]
            )
            embed.add_field(name="🪢 Other Titles", value=altitle)
            embed.set_thumbnail(url=manga["attributes"]["posterImage"]["original"])

            if manga["attributes"]["coverImage"] == None:
                imageurl = manga["attributes"]["posterImage"]["original"]
            else:
                imageurl = manga["attributes"]["coverImage"]["original"]
            embed.set_image(url=imageurl)

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
    bot.add_cog(MangaCmd(bot))
