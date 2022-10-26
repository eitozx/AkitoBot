import os
import aiohttp
import discord
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command

class MovieCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "movie", 
        description = "To get movie info"
    )
    async def movie(self, ctx, *, name : discord.Option(str, 'Name of the movie', required=True)):
        try:
            async with aiohttp.ClientSession() as session:
                oldsite = await session.get(
                    f"https://api.themoviedb.org/3/search/movie?api_key={os.getenv('MOVIEDB_API_KEY')}&query={name}"
                )
                olddata = await oldsite.json(content_type=None)
                id = olddata["results"][0]["id"]
                new = await session.get(
                    f"https://api.themoviedb.org/3/movie/{id}?api_key={os.getenv('MOVIEDB_API_KEY')}"
                )
                data = await new.json(content_type=None)

            embed = discord.Embed(
                title=data["title"],
                description=data["overview"],
                url=data["homepage"],
                colour=discord.Color.blue(),
            )

            genres = " , ".join([i["name"] for i in data["genres"]])
            if not genres:
                genres = "Data Not Available"
            embed.add_field(name="🧬 Genre", value=genres)

            embed.add_field(
                name="🏆 Popularity", value=data.get("popularity", "Data Not Available")
            )
            embed.add_field(name="📅 Release", value=data["release_date"])

            country = " , ".join([i["name"] for i in data["production_countries"]])
            if not country:
                country = "Data Not Available"
            embed.add_field(name="🌎 Production Country", value=country)

            embed.add_field(name="⭐ Rating", value=data["vote_average"])

            revenue = data["revenue"]
            if not revenue:
                revenue = "Data Not Available"
            else:
                revenue = f"${revenue}"
            embed.add_field(name="💸 Revenue", value=revenue)

            if data["tagline"] == "":
                tagline = "None"
            else:
                tagline = data["tagline"]
            embed.add_field(name="🔗 Tagline", value=tagline, inline=False)

            poster = data["poster_path"]
            embed.set_thumbnail(url=f"https://image.tmdb.org/t/p/original{poster}")

            image = data["backdrop_path"]
            embed.set_image(url=f"https://image.tmdb.org/t/p/original{image}")
            await ctx.respond(embed=embed)

        except IndexError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        except:
            raise

def setup(bot):
    bot.add_cog(MovieCmd(bot))
