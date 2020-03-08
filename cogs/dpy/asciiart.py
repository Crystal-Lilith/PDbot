@client.command(description='Creates ascii art||<font> <message>')
async def asciiart(ctx, font, *, message):
    try:
        embed = discord.Embed(color=discord.Color.from_rgb(0, 191, 255),
                                description=f'```{pyfiglet.figlet_format(message, font=font)}```')
        embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Font doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
