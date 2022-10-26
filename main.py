import os
import jishaku
import discord
from discord.ext import commands
from akito import Token

try:
    import uvloop
    import asyncio
except ImportError:
    pass


def main():

    bot = commands.Bot(
        case_insensitive = True,
        strip_after_prefix = True,
        intents= discord.Intents.default(),
        command_prefix= commands.when_mentioned,
    )

    bot.remove_command("help")

    for folder in os.listdir("extension"):
        if os.path.exists(os.path.join("extension", folder)):

            for filename in os.listdir(f"extension/{folder}"):
                # afaik, i excluded these folders as the cogs inside them 
                # were still under transistion from text command to slash command,
                # but i didn't make the changes because i was occupied with some stuff
                if folder in ["genshin",'roleplay','image','nsfw']:
                    pass
                else:
                    if filename.endswith(".py"):
                        bot.load_extension(f"extension.{folder}.{filename[:-3]}")


    bot.unload_extension('extension.fun.tictactoe') # i unloaded this one too, because i had to update some stuff in it, idr that anymore lol
    bot.load_extension("jishaku")
    print(f"Loaded {len(bot.extensions)}")
    bot.run(Token.bot.value)


if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        uvloop.install()
    except:
        pass
    finally:
        main()
