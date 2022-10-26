import requests
import discord
from akito import Embed
from discord.ext import commands
from discord.commands import slash_command

class AddemojiCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "addemoji",
        description = "To add emoji in server"
    )
    @commands.has_permissions(manage_emojis=True)
    async def addemoji(
        self, ctx, 
        emojiurl: discord.Option(str, 'discord Emoji Url', required=True), 
        name: discord.Option(str, 'Name of the emoji', required=True, default=None)
    ):
        try:
            if emojiurl.startswith("https:"):

                response = requests.get(emojiurl)
                emojis = await ctx.guild.create_custom_emoji(
                    name=name, image=response.content
                )
                emoji = self.bot.get_emoji(emojis.id)

                if emoji.animated:
                    description = f"{ctx.author.mention} Added emoji:\n`<a:{emoji.name}:{emoji.id}>`"
                else:
                    description = f"{ctx.author.mention} Added emoji:\n`<:{emoji.name}:{emoji.id}>`"

                embed = discord.Embed(
                    title=f"New Emoji Added!",
                    description=description,
                    colour=discord.Color.blue(),
                )
                embed.set_image(url=emoji.url)
                await ctx.respond(embed=embed)

            else:
                emoid = (emojiurl)[-19:-1]

                if "a" in emojiurl:
                    link = f"https://cdn.discordapp.com/emojis/{emoid}.gif?v=1"
                else:
                    link = f"https://cdn.discordapp.com/emojis/{emoid}.png?v=1"

                emoji = await ctx.guild.create_custom_emoji(name=name, image=link)
                emoji = self.bot.get_emoji(emoid)

                embed = discord.Embed(
                    title=f"New Emoji Added!",
                    description=f"{ctx.author.mention} Added New Emoji!",
                    colour=discord.Color.blue(),
                )
                embed.set_image(url=emoji.url)
                await ctx.respond(embed=embed)
                await ctx.respond(link)

        except TypeError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(AddemojiCmd(bot))
