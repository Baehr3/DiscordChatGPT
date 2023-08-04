import nextcord
import openai
from nextcord.ext import commands

bot = commands.Bot(intents=nextcord.Intents.all(), command_prefix="@")
openai.api_key = "API KEY HERE"


@bot.event
async def on_message(message):
    if bot.user != message.author:
        if message.content[((message.content.lower()).find("im")+2)] == " ":
            s=""
            for _ in list(message.content[((message.content.lower()).find("im")+3):]):
                if _!=" ":
                    s=s+_
                else: break

            await message.channel.send("Hi {}, I'm bot".format(s))
        else:
            await bot.process_commands(message)
    else:
        await bot.process_commands(message)


@bot.command()
async def ask(ctx, *, message):
    comp = openai.Completion.create(model="gpt-3.5-turbo", prompt=message, max_tokens=4000)
    await ctx.reply(comp.choices[0].messages)

@bot.command()
async def gen(ctx, *, message):
    generate = openai.Image.create(prompt=(message), n=1, size="256x256")
    await ctx.reply(generate.choices[0].url)

bot.run("DISCORD BOT KEY HERE")



