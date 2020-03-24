import discord
from discord.ext import commands
import random
import asyncio
import string
import datetime
import aiohttp
from discord.ext import tasks
import json


initial_extensions = ['cogs.member', 'cogs.moderation', 'cogs.fun']
with open("values.json") as f:
    data = json.load(f)
    t = data["Token"]
    
token = t
prefix = ";"
description = "Mhm Yes it seems you have gotten to me, the bot. It looks like we are going to have a fun time! Commands are being added so don't cry"
bot = commands.Bot(command_prefix=prefix, description=description)


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
        print(f"Loaded {extension}")

def load_values():
    with open('tag.json', 'r') as json_file:
        return json.load(json_file)


def save_values():
    with open('tag', 'w') as json_file:
        json.dump(values, json_file)



@bot.event
async def on_ready():
    print("----------")
    print("I am ready")
    print(f"Version {discord.__version__}")
    print(f"Logged in as {bot.user}")
    print(f"My ID is {bot.user.id}")
    print("----------")


@bot.command()
async def hi(ctx):
    channel = bot.get_channel(681254950033948674)
    await channel.send("Hi")





@bot.command()
async def verify(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Member // Verified")
    member = ctx.author
    
    if role not in member.roles:
        user = ctx.author
        verify = "".join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for x in range(5))
        embed1=discord.Embed(title="Hey!", description=f"Type this: `{verify}`, if you do it correctly you get acces to the rest of the server. Goodluck!")
        await user.send(embed=embed1)
        message = await bot.wait_for('message', timeout=60)
        if message.content == verify:
            embed2=discord.Embed(title="I'm proud", description="You did it! You now have full acces to the server")
            await user.send(embed=embed2)
            await member.add_roles(role)
    
        elif message.content != verify:
            embed3=discord.Embed(title="Sad man", description="Sorry, this is not correct, try again by doing `L!verify`.")
            await user.send(embed=embed3)
    elif role in member.roles:
        await ctx.send("You're already verified!")







@bot.command()
@commands.is_owner()
async def reload(ctx):
    try:
        for extension in initial_extensions:
            bot.unload_extension(extension)
            await asyncio.sleep(0.5)
            bot.load_extension(extension)
            await ctx.send(f"Reloaded {extension}")
    except Exception as e:
        await ctx.send(e)





@bot.group(invoke_without_command=True)
async def tag(ctx, query):
    try:
        with open("tag.json") as f:
            data = json.load(f)

            tags = data["Tags"] #A list of dicts
            for tag in tags:
                if query in tag["Names"]:
                    content = tag["Content"]
                    await ctx.send(content)
    except Exception as e:
        print(e)


@tag.command(aliases=["make", "Make", "Create"])
async def create(ctx):
    
    def check(message):
        return message.author == ctx.author
    
    await ctx.send("What is the name of the tag?")
    name = await bot.wait_for('message', timeout=30.0, check=check)

    await ctx.send("Okay what is the content? \n Note: If you want images make them a link, not going to store alot of images :)")
    ct = await bot.wait_for('message', timeout=90.0, check=check)
    await ctx.send("Great, making the tag now, I'll notify you when its done!")
    with open("tag.json") as file:
        data = json.load(file)
        temp = data["Tags"]
        y = {
            "Names" : name.content,
            "Content" : ct.content,
            "Author" : ctx.author.id
        }
    
        def write_json(data, filename='tag.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4)
            
        temp.append(y)
    write_json(data)
    await ctx.send("Done!")

@tag.command()
async def info(ctx, t):
    with open("tag.json") as file:
        data = json.load(file)
        tags = data["Tags"]
        for tag in tags:
            if t in tag["Names"]:
                content = tag["Content"]
                author = tag["Author"]
                names = tag["Names"]
                creator = bot.get_user(author)
                einfo=discord.Embed(title="", description=f"**Author:** {creator.mention}\n**Content:** {content}", timestamp=datetime.datetime.now())
                einfo.set_author(name=f"Showing info for tag: {names}", icon_url=creator.avatar_url, url=einfo.Empty)
                await ctx.send(embed=einfo)


@tag.error
async def tag_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        etag=discord.Embed(title="", description="Tag commands will be displayed here...")
        await ctx.send(embed=etag)

@bot.command()
async def foo(ctx):
    await ctx.send("SAY IT")
    mystring = await bot.wait_for('message', timeout=200.0, check=None)
    data = mystring.content.split("", 60)
    data1 = data.split("\n", 120)
    data2 = data1.split("\n", 180)
    data3 = data2.split("\n", 240)
    data4 = data3.split("\n", 300)
    data5 = data4.split("\n", 360)
    data6 = data5.split("\n", 420)
    data7 = data6.split("\n", 480)
    data8 = data7.split("\n", 540)
    data9 = data7.split("\n", 600)
    for final in data9:
        await ctx.send(final)



bot.run(token)