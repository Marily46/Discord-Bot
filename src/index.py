import discord
from discord.ext import commands
import datetime
from urllib import parse, request 
import re


bot = commands.Bot(command_prefix='>', description= "This is a helper bot" )

@bot.command()
async def ping(ctx):
    await ctx.send('QUE VIVA EL TECHNOO!!!')

@bot.command()
async def sum(ctx,numOne: int, numTwo: int):
     await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",description="Hola Gente de la nueva Era",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="Server Created at", value =f"{ctx.guild.created_at}")
    embed.add_field(name="server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID",value=f"{ctx.guild.id}")  
    await ctx.send(embed=embed)
    
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0] )

@bot.command()
async def play(ctx,url:str):
    voiceChannel= discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    await voiceChannel.connect()
    
@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("El bot no esta conectado al voice")
        
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No se està reproduciendo audio")
        
@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("El audio no esta en pausa")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    voice.stop()


#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="ChatBot", url="http://www.twitch.tv/accountname"))
    print('My Bot is Ready')

bot.run('OTI4MTMyNTMyMDA2OTc3NTg3.YdUUxw.Uylfm-TJTyfhVE3X5Jhh_ZZU4ws')
    