import discord
from discord.ext import commands
import PIL
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.group(invoke_without_command=True)
    async def m(self, ctx):
        await ctx.send("Make memes and do other fun stuff!")
    
    @m.command()
    async def make(self, ctx):

        def check(message):
            return message.author == ctx.author
        
        await ctx.send("What is the toptext?")
        top = await self.bot.wait_for('message', timeout=30.0, check=check)
        await ctx.send("Great, what is the bottomtext?")
        bottom = await self.bot.wait_for('message', timeout=30.0, check=check)
        await ctx.send("Okay great, making the meme now. This can take a few seconds...")
        basis = Image.open("Doge.jpg")
        width, height = basis.size
        width += int(width * -0.21)
        toptext = top.content
        bottomtext = bottom.content
        fnt = ImageFont.truetype('impact.ttf', 45)
        img = Image.new('RGBA', basis.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(basis)
        d.text((width / 2, 10), toptext, font=fnt, fill=(255, 255, 255, 255))
        d.text((width / 2, height - 60), bottomtext, font=fnt, fill=(255, 255, 255, 255))
        basis.save('CoolMeme.png')
        await ctx.send("Hey", file=discord.File('CoolMeme.png'))


        





def setup(bot):
    bot.add_cog(Fun(bot))