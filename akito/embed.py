import discord

class Embed:

    # missing required permission
    async def missingrequiredpermission(self, ctx, permission_name):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Missing Required Permission.",
            colour=discord.Color.red(),
            description=f"You need {permission_name} permission to use this command.\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed

    # data not found
    async def datanotfound(self, ctx):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Data Not Found.",
            colour=discord.Color.red(),
            description=f"{ctx.author.mention} I don't seem to find data for your command/query.\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed


    # missing required argument
    async def missingrequiredargument(self, ctx):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Missing Required Argument.",
            colour=discord.Color.red(),
            description=f"Required Argument is missing. Please use it in correct way."
            f"\n\nCorrect Usage: `/{ctx.command.name} {ctx.command.usage}`\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed


    # member not found
    async def membernotfound(self, ctx):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Member Not Found",
            colour=discord.Color.red(),
            description=f"Member Not Found. Please use it in correct way."
            f"\n\nCorrect Usage: `/{ctx.command.name} {ctx.command.usage}`\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed


    # channel not found
    async def channelnotfound(self, ctx):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Channel Not Found.",
            colour=discord.Color.red(),
            description=f"Channel Not Found. Please use it in correct way."
            f"\n\nCorrect Usage: `/{ctx.command.name} {ctx.command.usage}`\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed

    # guild not Found
    async def guildnotfound(self, ctx):
        embed = discord.Embed(
            title=f"<:oh:881566351783780352> Guild Not Found.",
            colour=discord.Color.red(),
            description=f"Guild Not Found. Please use it in correct way."
            f"\n\nCorrect Usage: `/{ctx.command.name} {ctx.command.usage}`\n"
            f"\nFor More: `/help {ctx.command.name}`"
        )
        embed.set_footer(text=f"Join My Server For Additional Help!")
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        return embed