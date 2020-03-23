@client.command(description='Updates the PDBot||None')
async def update(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(0, 191, 255), description='```Updating bot...```')
    embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)
    try:
        await os.system('./stop.sh')
        await bot.close()
        await sys.exit()
    except:
        embed = discord.Embed(color=discord.Color.from_rgb(0, 191, 255), description='```Failed to update the bot!```')
        embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
