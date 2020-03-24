import discord
from discord.ext import commands
import PIL
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import asyncio
import io
from io import BytesIO
import requests

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
        fnt = ImageFont.truetype('impact.ttf', 20)
        img = Image.new('RGBA', basis.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(basis)
        d.text((width / 2, 10), toptext, font=fnt, fill=(255, 255, 255, 255))
        d.text((width / 2, height - 60), bottomtext, font=fnt, fill=(255, 255, 255, 255))
        basis.save('CoolMeme.png')
        await ctx.send("Hey", file=discord.File('CoolMeme.png'))

    @commands.command()
    async def ecard(self, ctx):

        def check(message):
            return message.author == ctx.author
        
        download = requests.get(ctx.author.avatar_url, stream=True)
        av = Image.open(io.BytesIO(download.content))
        print('mhm')
        base = Image.open("base.jpg")
        await ctx.send("What is your company name?")
        comp = await self.bot.wait_for('message', timeout=60.0, check=check)
        await ctx.send("Great, what is the content?")
        ct = await self.bot.wait_for('message', timeout=60.0, check=check)
        width, height = base.size
        width += int(width * -0.21)
        print('mm')
        btmfnt = ImageFont.truetype('Helvetica.ttf', 20)
        d = ImageDraw.Draw(base)
        d.text((760, 1000), f"--------------- {ctx.author.name} - Call now! 06-1337420!---------------", font=btmfnt, fill=(107, 107, 107, 107))
        print('Lucky')
        base.paste(av, (0,0))
        print('cbt')
        mainfnt = ImageFont.truetype('Helvetica.ttf', 69)
        slfnt = ImageFont.truetype('Helvetica.ttf', 44)
        d.text((210, 0), comp.content, font=mainfnt, fill=(12, 12, 12, 12))
        d.text((215, 215), ct.content, font=slfnt, fill=(28, 28, 28, 28))
        base.save('Ecard.jpg')
        print("Dayum")
        await ctx.send("Hey", file=discord.File('Ecard.jpg'))




        





def setup(bot):
    bot.add_cog(Fun(bot))