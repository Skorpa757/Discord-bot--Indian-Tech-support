import discord
from discord.ext import commands


class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def please(self, ctx):
        await ctx.send("No No No No NO NO NO Drugs are bad mmmkay")
    
    @commands.command(aliases=["fuckyeah!"])
    async def fuckyeah(self, ctx):
        ctx.send("I FUCKING DID IT")
    
    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("You did it")

def setup(bot):
    bot.add_cog(MembersCog(bot))