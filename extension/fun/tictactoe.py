import discord
from typing import List
from asyncio import sleep
from akito import Embed, final
from discord.ext import commands


# Defines a custom button that contains the logic of the game.
# The ['TicTacToe'] bit is for type hinting purposes to tell your IDE or linter
# what the type of `self.view` is. It is not required.
class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, x: int, y: int, ctx, user):
        self.ctx = ctx
        self.user = user
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):

        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = f"{self.user.mention}'s turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = f"{self.ctx.author.mention}'s  turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = f"{self.ctx.author.mention} **WON!!!** 🎉\n{self.user.mention} Lost 💀"
            elif winner == view.O:
                content = f"{self.user.mention} **WON!!!** 🎉\n{self.ctx.author.mention} Lost 💀"
            else:
                content = f"**It's a tie! Between {self.user.mention} & {self.ctx.author.mention}**"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self, ctx, user):
        self.ctx = ctx
        self.user = user
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y, self.ctx, self.user))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


class TTTCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = "tictactoe",
        aliases=["ttt", "tic-tac-toe"],
        description = "Play Tic-Tac-Toe with friends",
        usage = "[Opponent User]",
        help ="• **Vote locked** command.")

    async def ttt(self, ctx, user: discord.Member = None):
        if not user:

            embed = await Embed.missingrequiredargument(self, ctx)
            await ctx.respond(embed = embed, )
            return

        elif user == self.bot.user:
            embed = discord.Embed(
                title=f"<:mecool:885766779496972298> You Noob",
                colour=discord.Color.red(),
                description=f"You can't fight with me, I'm too cool. Challenge someone else. "
                f"\n\nCorrect Usage: `/tictactoe [user]`\nWhere `user` is your oppopnent. Just challenge him!",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)
            return

        elif user == ctx.author:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> You Noob",
                colour=discord.Color.red(),
                description=f"You can't challenge yourself. Challenge someone else. "
                f"\n\nCorrect Usage: `/tictactoe [user]`\nWhere `user` is your oppopnent. Just challenge him!",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)
            return

        elif user.bot:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> You Noob",
                colour=discord.Color.red(),
                description=f"You can't challenge a bot, they're too cool. Challenge someone else. "
                f"\n\nCorrect Usage: `/tictactoe [user]`\nWhere `user` is your oppopnent. Just challenge him!",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)
            return

        else:
            one = discord.Embed(
                title="Tic-Tac-Toe!",
                color=ctx.author.top_role.color,
                description=f"**{ctx.author.mention} ⚔️ {user.mention}!**",
            )

            msg = await ctx.respond(embed=one)
            await sleep(2)
            await msg.edit(content=f"First goes {ctx.author.mention}", view=TicTacToe(ctx, user))


def setup(bot):
    bot.add_cog(TTTCmd(bot))
