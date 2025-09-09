import discord
from discord import app_commands
from discord.ext import commands


class ExampleCog(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # mypy is happy
    @commands.command()
    async def my_text_cmd(self, ctx: commands.Context[commands.Bot]) -> None:
        # these react to text messages in discord chat
        await ctx.send("Text command says: Hello world")
        return None

    # mypy is happy
    @app_commands.command()
    # app commands use a different signature
    async def my_app_cmd(self, interaction: discord.Interaction[commands.Bot]) -> None:
        # these are slash commands
        await interaction.response.send_message("App command says: Hello world.")
        return None

    # mypy is not happy
    @commands.hybrid_command()
    async def my_hybrid_cmd(self, ctx: commands.Context[commands.Bot]) -> None:
        # these are _both_ text and slash commands, facilitated by discord.py
        await ctx.send("Hybrid command says: Hello world.")
        return None


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))
