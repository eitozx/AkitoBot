import aiohttp
import discord
from discord.ext import commands
from akito.var import Token, Link

def votelock():
    async def votecheck(ctx):
        header = {"Authorization": str(Token.topgg.value)}
        # params={"userId": ctx.message.author.id},

        async with aiohttp.ClientSession() as session:
            try:
                # response = await session.get(f"https://top.gg/api/bots/{ctx.bot.user.id}/check", headers = header, params = params)
                response = await session.get(f"https://top.gg/api/bots/885876809776893964/check?userId={ctx.author.id}", headers = header)
                data = await response.json(content_type=None)

                # return result
                if data['voted'] == 1:
                    print(f"{ctx.author} Yes")
                    return True

                else:                    

                    embed = discord.Embed(
                        title="<a:Tick:884027409123397682> Vote Required Command!", 
                        colour=discord.Color.blue(),
                        description=f"{ctx.author.mention} this command is **Vote Locked**.\n"
                        "You **Need to vote** if you **want to use this command**\n\n"
                        "Please **VOTE to use this command anytime for next 12 hours.**"
                    )

                    embed.add_field(
                        name = "You can unlock other commands too!",
                        value = f"`/vote` for complete list!",
                        inline = False
                    )
                    embed.set_thumbnail(url=ctx.bot.user.display_avatar)

                    view = discord.ui.View()
                    view.add_item(item=discord.ui.Button(label="Vote Me", url=Link.topgg.value))

                    await ctx.respond(embed=embed, view=view)

                    print(f"{ctx.author} No")
                    return False

            except:
                print("Error in Tracking Vote")
                return True

    return commands.check(votecheck)