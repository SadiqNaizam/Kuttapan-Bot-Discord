import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="kuttapa ")



@client.event
async def on_ready():
    print("bot online")
    await client.get_channel(746045604597334126).send("njan ethi")

@client.event
async def on_member_join(member):
 await client.get_channel(746045604597334126).send(f'{member} ethi')

@client.command()
async def play(ctx,url):
    channel = ctx.author.voice.channel
    await channel.connect()
    guild = ctx.message.guild
    voice_client = client.voice_clients(guild)
    player = await voice_client.create_ytdl_player(url)
    player.start()


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = client.voice_clients(guild)
    await voice_client.disconnect()

@client.command()
async def jokes(ctx):

    jokes = ["How does a rabbi make coffee? Hebrews it!",
     "Rest in peace boiling water. You will be mist!",
     "How do you throw a space party? You planet!",
     "Want to hear a construction joke? Oh never mind, I'm still working on that one.",
     "Why don't scientists trust atoms? Because they make up everything!",
     "I hate Russian dolls… they're so full of themselves!",
     "Talk is cheap? Have you ever talked to a lawyer?",
     "Why did the gym close down? It just didn't work out!",
     "Two artists had an art contest. It ended in a draw!",
     "A plateau is the highest form of flattery.",
     "I have a fear of speed bumps. But I am slowly getting over it.",
     "You can only get spoiled milk from a pampered cow.",
     "What do you call a boomerang that doesn't come back? A stick!",
     "You know what I saw today? Everything I looked at.",
     "What are shark's two most favorite words? Man overboard!",
     "If we shouldn't eat at night, why do they put a light in the fridge?",
     "Have you ever tried eating a clock? It's really time-consuming, especially if you go for seconds.",
     "Why are ghosts such bad liars? Because they are easy to see through.",
     "It's cleaning day so naturally, I've already polished off a whole chocolate bar.",
     "What did the buffalo say when his son left for college? Bison!",
     "Here, I bought you a calendar. Your days are numbered now.",
     "Where do fish sleep? In the riverbed.",
     "What did one plate say to his friend? Tonight, dinner's on me!",
     "Where are average things manufactured? The satisfactory.",
     "I tried to sure the airport for misplacing my luggage. I lost my case."]
    await ctx.send(f'{random.choice(jokes)}')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

client.run('tokrm:NzQ2NDAwNjM1OTA5NDM5NTgw.Xz_xww.KwuuquTCL2AQ1rcBtkY5Yns5aos')