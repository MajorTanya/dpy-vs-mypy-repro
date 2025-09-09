from discord.ext import commands


class ExampleCog(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command()
    async def my_cmd(self, ctx: commands.Context[commands.Bot]) -> None:
        await ctx.send("Hello world")
        return None


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))
