@client.command(description='Updates the PDBot||None')
async def update(ctx):
    embed = discord.Embed(title='Bot Update', color=discord.Color.from_rgb(0, 191, 255), description='```Updating bot...```')
    embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)
    # try:
    await bot.close()
    await os.system('./stop.sh')
    await sys.exit()
    # except:
    #     embed = discord.Embed(color=discord.Color.from_rgb(0, 191, 255), description='```Failed to update the bot!```')
    #     embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
    #     await ctx.channel.send(embed=embed)
