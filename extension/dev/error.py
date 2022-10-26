import discord
from akito import Var, Link
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command error handler
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Command On Cooldown",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} Don't try to spam.\nPlease retry after {str(error.retry_after)[:3]} seconds."
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed)

        elif isinstance(error, commands.NSFWChannelRequired):
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> NSFW Channel Required",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention}, this command/query can be used in NSFW Channel(s) Only"
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            
            await ctx.respond(embed=embed)

        elif isinstance(error, commands.CommandInvokeError):
            try:
                embed = discord.Embed(
                    title=f"<:oh:881566351783780352> Error Occurred!",
                    colour=discord.Color.red(),
                    description=f"```{error}```")

                embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
                embed.set_footer(text=f"This Could Be An Unexpected Error, Please Consider Reporting.")

                button = discord.ui.View()
                button.add_item(item=discord.ui.Button(
                    label=" Support Server", url=Link.server.value)
                )

                await ctx.respond(embed=embed, view=button)

            except:
                embed = discord.Embed(
                    title=f"<:oh:881566351783780352> Error Occurred!",
                    colour=discord.Color.red(),
                    description=f"```{error}``` in {ctx.channel.mention} of **{ctx.guild.name}**")

                embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
                embed.set_footer(text=f"This Could Be An Unexpected Error, Please Consider Reporting.")

                button = discord.ui.View()
                button.add_item(item=discord.ui.Button(
                    label="Support Server", url=Link.server.value)
                )

                await ctx.author.send(embed=embed, view=button)

            finally:
                channel = self.bot.get_channel(Var.error_logger.value)

                embed = discord.Embed(
                    title=f"<:oh:881566351783780352> Error Occurred!",
                    colour=discord.Color.red(),
                    description=f"**Command:** {ctx.command.name}\n"
                    f"```{ctx.message.content}``` \n"
                    f" ```{error}``` \n"
                    f"in {ctx.channel.mention} of \n"
                    f"**{ctx.guild.name}** : {ctx.guild.id}",)

                if ctx.guild.icon:
                    embed.set_thumbnail(url=ctx.guild.icon)

                embed.set_author(
                    name=f"{ctx.author} | {ctx.author.id}",
                    icon_url=ctx.author.display_avatar
                )
                await channel.send(embed=embed)

        elif isinstance(error, commands.NotOwner):
            channel = self.bot.get_channel(Var.error_logger.value)

            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Someone Tried To Use Dev Command!",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} tried to use **{ctx.command.name}** command in {ctx.channel.mention}"
                f"\n**Content:** `{ctx.message.content}\n`"
                f"\nof **{ctx.guild.name}** : {ctx.guild.id}")

            if ctx.guild.icon:
                embed.set_thumbnail(url= ctx.guild.icon)

            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)

            await channel.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> You don't have the required permission(s)",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} You don't have **{(','.join(i for i in error.missing_permissions)).replace('_',' ').title()}** permission(s) to use this command."
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> I don't have the required permission(s)",
                colour=discord.Color.red(),
                description=f"I don't have **{(','.join(i for i in error.missing_permissions)).replace('_',' ').title()}** permission(s) to perform this command."
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed)

        elif isinstance(error, commands.CommandNotFound):
            pass

        else:
            channel = self.bot.get_channel(Var.error_logger.value)
            e = discord.Embed(
                title='Error Occured',
                description=f'```py\n{error}```',
                color=discord.Color.red()
            )
            e.set_footer(
                text=ctx.author,
                icon_url=ctx.author.display_avatar.url
            )
            await channel.send(embed=e)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
