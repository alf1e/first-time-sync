import tomlkit

import discord
from discord.ext import commands
import aiocron
import aiohttp

import breadcord


class FTS(breadcord.module.ModuleCog):
    @commands.is_owner()
    @commands.command()
    async def fts(self, ctx: commands.Context):
        self.bot.tree.copy_global_to(guild=ctx.guild)
        await self.bot.tree.sync(guild=ctx.guild)
        await ctx.send(
            embed=discord.Embed(
                title="Commands synchronised!",
                description="Commands synchronised! Disabling this module...",
                color=discord.Color.green()
            )
        )
        setting = self.bot.settings.get("modules")
        setting.value.remove("fts")
        await self.module.unload()


async def setup(bot: breadcord.Bot):
    await bot.add_cog(FTS("fts"))
