from discord.ext.commands import Cog, command


class CogsController(Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await ctx.bot.is_owner(ctx.author):
            await ctx.send("You don't have permission.")
            return False
        return True

    @command(name="load")
    async def _cog_load(self, ctx, cog):
        self.bot.load_extension("cogs." + cog)
        await ctx.send(f"Loaded Extension: {cog}.py")

    @command(name="unload")
    async def _cog_unload(self, ctx, cog):
        self.bot.unload_extension("cogs." + cog)
        await ctx.send(f"Unloaded Extension: {cog}.py")

    @command(name="reload")
    async def _cog_reload(self, ctx, cog):
        self.bot.reload_extension("cogs." + cog)
        await ctx.send(f"Reloaded Extension: {cog}.py")


def setup(bot):
    bot.add_cog(CogsController(bot))
