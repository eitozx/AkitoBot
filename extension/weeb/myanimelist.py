import re
import discord
import aiohttp
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command


def remove_html_tags(text):
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def main(data, ctx):
    description = data["about"]
    if not description:
        description = "No Bio."
    else:
        description = remove_html_tags(f"{data['about']}")

    embed = discord.Embed(
        title=data["username"],
        description=description,
        colour=discord.Color.blue(),
        url=data["url"],
    )
    embed.add_field(name="🧒 Gender", value=data["gender"])

    bday = data["birthday"]
    if not bday:
        bday = "Not Available."
    else:
        bday = bday.split("T")[0]
    embed.add_field(name="🎂 Birthday", value=bday)

    location = data["location"]
    if not location:
        location = "Not Set"
    embed.add_field(name="🌎 Location", value=location)
    embed.add_field(name="🆔 ID", value=data["user_id"])

    embed.add_field(name="👀 Last Seen", value=data["last_online"].split("T")[0])
    embed.add_field(name="📅 Joined On", value=data["joined"].split("T")[0])

    anime = "\n".join([f"{i[0]} : {i[1]}" for i in data["anime_stats"].items()])
    embed.add_field(name="💮  Anime Stats", value=anime.title().replace("_", " "))

    manga = " \n".join([f"{i[0]} : {i[1]}" for i in data["manga_stats"].items()])
    embed.add_field(name="㊙️ Manga Stats", value=manga.title().replace("_", " "))

    img = data["image_url"]
    if not img:
        img = "https://noimage.png/"
    embed.set_thumbnail(url=img)
    return embed


def fav(data, ctx):
    description = data["about"]
    if not description:
        description = "No Bio."
    else:
        description = remove_html_tags(f"{data['about']}")

    embed = discord.Embed(
        title=f"{data['username']}'s Favorites",
        description=description,
        colour=discord.Color.blue(),
        url=data["url"],
    )

    anime = "\n".join([i["name"] for i in data["favorites"]["anime"]])
    if not anime:
        anime = "No Favorites"
    embed.add_field(name="💮  Anime", value=anime)

    manga = "\n".join([i["name"] for i in data["favorites"]["manga"]])
    if not manga:
        manga = "No Favorites"
    embed.add_field(name="🉐  Manga", value=manga)

    embed.add_field(name="** **", value="** **")

    characters = "\n".join([i["name"] for i in data["favorites"]["characters"]])
    if not characters:
        characters = "No Favorites"
    embed.add_field(name="🎭 Characters", value=characters)

    ppl = "\n".join([i["name"] for i in data["favorites"]["people"]])
    if not ppl:
        ppl = "No Favorites"
    embed.add_field(name="👥  People", value=ppl)

    img = data["image_url"]
    if not img:
        img = "https://noimage.png/"
    embed.set_thumbnail(url=img)
    return embed


class button(discord.ui.View):
    def __init__(self, data, ctx):
        self.data = data
        self.ctx = ctx
        super().__init__()

        self.add_item(item=discord.ui.Button(emoji="🔗", label="MAL Profile", style=discord.ButtonStyle.link, url=self.data["url"],))

    @discord.ui.button(emoji="⭐", label="Favorites", style=discord.ButtonStyle.green)
    async def favorites(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(
            embed=fav(self.data, self.ctx), ephemeral=True)


class MyanimelistCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "myanimelist", 
        description = "To get MAL profile data"
    )
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    async def myanimelist(
        self, ctx, 
        user: discord.Option(str, 'MyAnimeList username', required=True, default=None)
    ):
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://api.jikan.moe/v3/user/{user}"
                response = await session.get(url)
                data = await response.json(content_type=None)

            await ctx.respond(content=f"** **", embed=main(data, ctx), view=button(data=data, ctx=ctx))


        except KeyError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(MyanimelistCmd(bot))
