import random
import aiohttp
import discord
from akito import Token, final
from discord.ext import commands
from discord.commands import slash_command

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(
        name = "game", 
        description = "To get game info."
    )
    async def game(self, ctx, *, name : discord.Option(str, 'Name of the game', required=True)):
        try:
            async with aiohttp.ClientSession() as session:

                url = f"https://api.igdb.com/v4/games"

                header = {
                    "Client-ID": Token.twitch_client.value,
                    "Authorization": f"Bearer {Token.twitch_access.value}",
                }

                # to search game
                data = f"""
                        search "{name}"; 
                        fields name, alternative_names.name, cover.url, first_release_date, game_engines.name, game_modes.name, genres.name, involved_companies.company.name, keywords.name, platforms.name, player_perspectives.name, screenshots.url, storyline, summary, total_rating, total_rating_count, url, websites.url;
                        limit 5;
                        """

                response = await session.post(url, headers=header, data=data)
                base = await response.json(content_type=None)
                game = base[0]

            summary = game.get("summary")
            if not summary:
                summary = " "
            else:
                summary = game["summary"]
            embed = discord.Embed(
                title=game["name"],
                url=game["url"],
                description=summary,
                # description = game["summary"],
                colour=discord.Color.blue(),
            )

            rating = game.get("total_rating")
            if not rating:
                rating = "Data Not Available"
            else:
                rating = f"{round(game['total_rating'])}/100"
            embed.add_field(name="⭐ Rating", value=rating)

            release = game.get("first_release_date")
            if not release:
                release = "Data Not Available"
            else:
                release = f"<t:{game['first_release_date']}:D>"
            embed.add_field(name="📅 Release Date", value=release)

            gamemode = game.get("game_modes")
            if not gamemode:
                gamemode = "Data Not Available"
            else:
                gamemode = " ,".join([i["name"] for i in game["game_modes"]])
            embed.add_field(name="📳 Game Mode", value=gamemode)

            genre = game.get("genres")
            if genre:
                genre = " ,".join([i["name"] for i in game["genres"]])
            else:
                genre = "Data Not Available"
            embed.add_field(name="🧬 Genre", value=genre)

            company = game.get("involved_companies")
            if not company:
                company = "Data Not Available"
            else:
                company = " ,".join(
                    [i["company"]["name"] for i in game["involved_companies"]]
                )
            embed.add_field(name="🏢 Company", value=company)

            perspective = game.get("perspective")
            if not perspective:
                perspective = "Data Not Available"
            else:
                perspective = " ,".join(
                    [i["name"] for i in game["player_perspectives"]]
                )
            embed.add_field(name="👀 Perspective", value=perspective)

            platforms = game.get("platforms")
            if not platforms:
                platforms = "Data Not Available"
            else:
                platforms = " ,".join([i["name"] for i in game["platforms"]])
            embed.add_field(name="💻 Platforms", value=platforms, inline=False)

            cover = game.get("cover")
            if cover:
                cover = f"https:{game['cover']['url']}".replace("t_thumb", "t_original")
                embed.set_thumbnail(url=cover)
            
            image = game.get("screenshots")
            if image:
                image = random.choice(([i["url"] for i in game["screenshots"]]))
                image = f"https:{image}".replace("t_thumb", "t_original")
                embed.set_image(url=image)

            await ctx.respond(embed=embed)

        except IndexError:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Data Not Found",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} I don't seem to find data for `{name}`",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            await ctx.respond(embed=embed)

        except:
            raise


def setup(bot):
    bot.add_cog(Misc(bot))
