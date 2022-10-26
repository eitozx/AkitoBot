import enum
import os
import dotenv

dotenv.load_dotenv()


class Token(enum.Enum):
    bot = os.getenv("BOT_TOKEN")
    topgg = os.getenv("TOPGG_TOKEN")
    movie = os.getenv("MOVIEDB_API_KEY")
    airi = os.getenv("AIRI_TOKEN")
    weeby = os.getenv("WEEBY")

    twitch_client = os.getenv("TWITCH_CLIENT_ID")
    twitch_access = os.getenv("TWITCH_ACCESS_TOKEN")
    twitch_secret = os.getenv("TWITCH_CLIENT_SECRET")


class Var(enum.Enum):

    vote_role = # ROLE ID 

    error_logger = # TEXT CHANNEL ID
    guild_logger = # TEXT CHANNEL ID
    vote_logger = # TEXT CHANNEL ID
    post_logger = # TEXT CHANNEL ID
    command_logger = # TEXT CHANNEL ID
    connect_logger = # TEXT CHANNEL ID

    suggestion_logger = # TEXT CHANNEL ID


class Link(enum.Enum):
    bot = # Bot invite link
    server = # Support server invite link
    topgg = # top.gg link
    banner = # bot banner link
