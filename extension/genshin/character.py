import discord
import aiohttp
from akito import Embed, prefix
from discord.ext import commands


# genshin CHARACTER info
def gicinfo(ctx, data, url):
    embed = discord.Embed(
        title=f"{data['rarity']} ⭐ {data['name']}",
        colour=ctx.author.color,
        description=data["description"],
    )

    embed.add_field(name="Vision", value=data["vision"])
    embed.add_field(name="Weapon", value=data["weapon"])
    embed.add_field(name="Nation", value=data["nation"])
    embed.add_field(name="Birthday", value=f"{data['birthday']}"[6:])
    embed.add_field(name="Constellation", value=data["constellation"])

    embed.set_thumbnail(url=f"{url}/icon")
    embed.set_image(url=f"{url}/portrait")
    embed.set_footer(text=f"Requested By: {ctx.author}", icon_url=f"{ctx.author.display_avatar}")

    return embed


# genshin SKILL TALENT character
def gicskill(ctx, data):

    skills = "\n\n".join([f"**{i['name']} | {i['unlock']}**\n{i['description']}" for i in data["skillTalents"]])

    embed = discord.Embed(
        title=f"{data['rarity']} ⭐ {data['name']} Skill Talents",
        colour=ctx.author.color,
        description=skills,
    )

    return embed


# genshin PASSIVE TALENT character
def gicpassive(ctx, data):

    passives = "\n\n".join(
        [
            f"**{i['name']} | {i['unlock']}**\n{i['description']}"
            for i in data["passiveTalents"]
        ]
    )

    embed = discord.Embed(
        title=f"{data['rarity']} ⭐ {data['name']} Passive Talents",
        colour=ctx.author.color,
        description=passives,
    )

    return embed


# genshin Constellations character
def gicconst(ctx, data):

    consts = "\n\n".join(
        [
            f"**{i['name']} | {i['unlock']}**\n{i['description']}\n*Level: {i['level']}*"
            for i in data["constellations"]
        ]
    )

    embed = discord.Embed(
        title=f"{data['rarity']} ⭐ {data['name']} Constellations",
        colour=ctx.author.color,
        description=consts,
    )

    return embed


class GenchinCharacter(discord.ui.View):
    def __init__(self, data, ctx):
        self.data = data
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(emoji="🌠", label="Skill Talents", style=discord.ButtonStyle.blurple)
    async def skill(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(embed=gicskill(self.ctx, self.data), ephemeral=True)

    @discord.ui.button(emoji="💫", label="Passive Talents", style=discord.ButtonStyle.danger)
    async def passive(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(embed=gicpassive(self.ctx, self.data), ephemeral=True)

    @discord.ui.button(emoji="🌌", label="Constellations", style=discord.ButtonStyle.blurple)
    async def const(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(embed=gicconst(self.ctx, self.data), ephemeral=True)


class CharacterCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin characters command
    @commands.command(
        name="genshincharacter",
        aliases=["gc", "gcharacter", "genshinimpactcharacter"],
        description="Genshin Impact Character Info",
        usage = "(Character Name)",
        help = "If `Character Name` is not provided, it shows list of available characters.")
    async def gcharacter(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/characters"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            elements = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:ChildeCool:889113056662126613> Genshin Impact: Characters",
                colour=ctx.author.color,
                description=f"**__Name__ of Characters:**\n"
                f"{elements}\n"
                f"\n**To Get Info:**\n"
                f"`{prefix(ctx)}gcharacter [name]`\n",
            )

            embed.set_footer(
                text=f"Requested By: {ctx.author}",
                icon_url=f"{ctx.author.display_avatar}",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = f"https://api.genshin.dev/characters/{search}"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)

                    await ctx.respond(
                        content=f"** **",
                        embed=gicinfo(ctx, data, url),
                        view=GenchinCharacter(data, ctx),
                    )

            except KeyError:
                embed = await Embed.datanotfound(self, ctx)
                await ctx.respond(embed=embed, delete_after=60)

            except:
                raise


def setup(bot):
    bot.add_cog(CharacterCmd(bot))
