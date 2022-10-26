import akito
import discord
from akito import Link, final
from discord.ext import commands
from discord.commands import slash_command

def helpmain(ctx):
    updates = "\n <:TextChannel:886507750060859472>".join([i for i in akito.updates])
    embed = discord.Embed(
        title=f"<a:Tick:884027409123397682> HELP!",
        colour=discord.Color.blurple(),
        description=f"**Slash commands:** `/`",
    )
    embed.add_field(
        name=f"<a:utility:881782538627076096> " "Utility",
        value=f"Some Utility & Useful Commands.\n",
    )
    embed.add_field(
        name=f"<:moderation:881782591060062288> Moderation",
        value=f"Server Moderation Commands.\n",
    )
    embed.add_field(
        name=f"<:Sparkle:884028940883206176> Fun",
        value=f"Some Fun & Other Commands.\n",
    )
    embed.add_field(
        name=f"<:Anime:881813511414611968> Weeb",
        value=f"Anime/Manga Related Commands.\n",
    )
    embed.add_field(
        name=f"<:Zelda:884027752716587048> Misc",
        value=f"Some More Commands. Just Check It Out :D\n",
    )
    # embed.add_field(
    #     name=f"<a:GenshinImpact:887940868068229151> Genshin",
    #     value=f"Game Data: Character, Element, Enemy, Nation, Potion, Weapon.\n",
    # )
    # embed.add_field(
    #     name=f"🔞 NSFW", 
    #     value=f"You know what is this & so do i.👀\n"
    # )
    embed.add_field(
        name=f"<:settings:881782626946539540> Other Commands!",
        value=f"`/vote`: Support Me!\n"
    )
    # embed.add_field(
    #     name= "<:DarlingHeart:884029459487928330> Suggest features/stuffs using `/suggest` command!",
    #     value= "** **",
    #     inline = False
    # )
    embed.add_field(
        name=f"📰 Latest Updates:",
        value=f"<:TextChannel:886507750060859472> {updates}",
        inline=False,
    )
    embed.set_image(url=Link.banner.value)
    return embed


def utility():
    u = discord.Embed(
        title=f"<a:utility:881782538627076096> Utility Commands.",
        colour=discord.Color.blurple(),
        description=f"`addemoji` | `avatar` | `embed` | `ping` | `poll` | `roleinfo` | `say` | `serverinfo` | `textchannelinfo` | "
        "`userinfo` | `voicechannelinfo`"
    )
    return u

def moderation():
    m = discord.Embed(
        title=f"<:moderation:881782591060062288> Moderation Commands.",
        colour=discord.Color.blurple(),
        description=f"`ban` | `kick` | `lock` | `nuke` | `purge` | `slowmode` | `unban` | `unlock`"
    )
    return m

def fun():
    f = discord.Embed(
        title=f"<:Sparkle:884028940883206176> Fun Commands.",
        colour=discord.Color.blurple(),
        description=f"`advice` | `ask` | `bored` | `dare` | `roast` | `tictactoe` | `truth` | `wallpaper`"
    )
    return f

def misc():
    m = discord.Embed(
        title=f"<:Zelda:884027752716587048> Misc Commands.",
        colour=discord.Color.blurple(),
        description=f"`game` | `github` | `meme` | `movie` | `pypi` | `reddit` | `redditinfo` "
    )
    return m

def weeb():
    am = discord.Embed(
        title=f"<:Anime:881813511414611968> Weeb Commands.",
        colour=discord.Color.blurple(),
        description=f"`anifact` | `anime` | `animememe` | `aniquote` | `manga` | `myanimelist`"
    )
    return am


# def GenshinMenu():
#     embed = discord.Embed(
#         title="<a:GenshinImpact:887940868068229151> Genshin Impact!",
#         colour=discord.Color.blurple(),
#         description=f"**Argument Guide:**\n`[]`: required | `()`: optional\n\n"
#         f"`gcharacter` | `gelement` | `genemy` | `gnation` | `gpotion` | `gweapon`"
#     )
#     return embed


# def nsfw():
#     nsfw = discord.Embed(
#         title=f"🔞 NSFW Commands",
#         colour=discord.Color.blurple(),
#         description=f"`4k` | `anal` | `bj` | `boob` | `cum` | `feet` | `hentai` | "
#         f"`lesbian` | `lewd` | `pussy`\n"
#         f"\n***Note:** These commands can be used in NSFW channels only.*\n",
#     )
#     return nsfw


class Dropdown(discord.ui.Select):
    def __init__(self):

        super().__init__(
            placeholder="📃 Select Help Category/Section",
            options=[
                discord.SelectOption(
                    emoji="<a:utility:881782538627076096>",
                    label="Utility",
                    description="Some Utility & Useful Commands.",
                ),
                discord.SelectOption(
                    emoji="<:moderation:881782591060062288>",
                    label="Moderation",
                    description="Server Moderation Commands.",
                ),
                discord.SelectOption(
                    emoji="<:Sparkle:884028940883206176>",
                    label="Fun",
                    description="Some Fun & Other Commands.",
                ),
                discord.SelectOption(
                    emoji="<:Anime:881813511414611968>",
                    label="Weeb",
                    description="Anime/Manga Related Commands.",
                ),
                discord.SelectOption(
                    emoji="<:Zelda:884027752716587048>",
                    label="Misc",
                    description="Some More Commands. Just Check It Out :D",
                ),
                # discord.SelectOption(
                #     emoji="<a:GenshinImpact:887940868068229151>",
                #     label="Genshin",
                #     description="Game Data: Characters, Enemies, Artifacts, etc.",
                # ),
                # discord.SelectOption(
                #     emoji="🔞",
                #     label="NSFW",
                #     description="You know what is this, so do i.👀",
                # ),
            ],
        )

    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "Utility":
            await interaction.response.send_message(embed=utility(), ephemeral=True)
        elif self.values[0] == "Moderation":
            await interaction.response.send_message(embed=moderation(), ephemeral=True)
        elif self.values[0] == "Fun":
            await interaction.response.send_message(embed=fun(), ephemeral=True)
        elif self.values[0] == "Weeb":
            await interaction.response.send_message(embed=weeb(), ephemeral=True)
        elif self.values[0] == "Misc":
            await interaction.response.send_message(embed=misc(), ephemeral=True)
        # if self.values[0] == "Genshin":
            # await interaction.response.send_message(embed=GenshinMenu(), ephemeral=True)
        # elif self.values[0] == "NSFW":
        #     await interaction.response.send_message(embed=nsfw(), ephemeral=True)


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())
        self.add_item(item=discord.ui.Button(label="Invite Link", style=5, url=Link.bot.value))
        self.add_item(item=discord.ui.Button(label="Support Server", style=5, url=Link.server.value))
        self.add_item(item=discord.ui.Button(label="Vote Here", style=5, url=Link.topgg.value))


class Help(commands.Cog, name="Help Menu"):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="help", 
        description = "Get to know me: Help!"
    )
    async def help(self, ctx):
        await ctx.respond(content="** **", embed=helpmain(ctx), view=DropdownView())
        # if not cmd:
        #     embed = helpmain(ctx)
        #     await ctx.respond(content="** **", embed=embed, view=DropdownView())

        # else:
            # try:
            #     command = self.bot.get_command(cmd)
                
            #     aliases = " | ".join([str(i).lower() for i in command.aliases])
            #     if not aliases:
            #         aliases = None

            #     description = command.description
            #     if not description:
            #         description = None

            #     embed = discord.Embed(
            #         title = str(command.name).title(),
            #         color = discord.Color.blue(),
            #         description= f"{str(description).capitalize()}\n\n"
            #         f"**Aliases:** ```py\n{str(aliases).lower()}```\n"
            #         f"**Usage:** ```py\n/{str(command.name).lower()} {command.usage}```\n"
            #         f"**More Info:** \n{command.help}"
            #     )
            #     embed.set_thumbnail(url=self.bot.user.display_avatar)
            #     await ctx.respond(embed=embed)
            
            # except:

    # @help.command(aliases=["utility", "Utility"])
    # 
    # async def help_utility(self, ctx):
    #     await ctx.respond(embed=utility())


    # @help.command(aliases=["moderation", "mod", "Moderation", "Mod"])
    # 
    # async def help_moderation(self, ctx):
    #     await ctx.respond(embed=moderation())


    # @help.command(aliases=["fun", "Fun"])
    # 
    # async def help_fun(self, ctx):
    #     await ctx.respond(embed=fun())


    # @help.command(aliases=["roleplay", "rp", "Image", "Roleplay", "image"])
    # 
    # async def help_roleplay(self, ctx):
    #     await ctx.respond(embed=roleplay())


    # @help.command(aliases=["weeb", "Weeb"])
    # 
    # async def help_weeb(self, ctx):
    #     await ctx.respond(embed=weeb())


    # @help.command(aliases=["misc", "Misc"])
    # 
    # async def help_misc(self, ctx):
    #     await ctx.respond(embed=misc())


    # # genshin base command
    # @help.group(aliases=["g", "gm", "gi", "genshin"])
    # 
    # async def genshinimpact(self, ctx):
    #     await ctx.respond(embed=GenshinMenu())


    # @help.group(aliases=["NSFW"])
    # 
    # @commands.is_nsfw()
    # async def nsfw(self, ctx):
    #     await ctx.respond(embed=nsfw())


def setup(bot):
    bot.add_cog(Help(bot))
