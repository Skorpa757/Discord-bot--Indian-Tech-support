import discord
from discord.ext import commands
import typing
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["Sweep", "sweep", "Ban", "banhammer", "Banhammer"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, reason: typing.Optional[str]=None):
        try:    
            await ctx.send("I am calling the almighty Banhammer...")
            await asyncio.sleep(2)
            await member.ban(reason=reason)
            await ctx.send(f"I have succesfully banned {member.name}!! Everyone thank the BanHammer God!")
        except Exception as e:
            await ctx.send(e)
    
    @commands.command(aliases=["Reverse", "reverse", "Unban"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int, reason: typing.Optional[str]=None):
        try:
            await ctx.send("I am reversing the Banhammer...")
            user = self.bot.get_user(id)
            await ctx.guild.unban(user, reason=reason)
            await ctx.send("I reversed the Banhammer... I am sorry BanHammer God.")
        except Exception as e:
            await ctx.send(e)
    
    @commands.command(aliases=["Kick"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, reason: typing.Optional[str]=None):
        try:
            await ctx.send("I am preparing myself...")
            await member.kick(reason=reason)
            await ctx.send(f"I kicked {member.name}")
        except Exception as e:
            await ctx.send(e)

        

    



















def setup(bot):
    bot.add_cog(Moderation(bot))