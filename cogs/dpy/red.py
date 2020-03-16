@client.command()
async def red(ctx):
    embed = discord.Embed(title='this is a red color', color=discord.Color.from_rgb(255, 0, 0), description='<= This is a red color')
    await ctx.channel.send(embed=embed)