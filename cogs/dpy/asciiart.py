@client.command(description='Creates ascii art||<message>')
async def asciiart(ctx, *, font, message):
    try:
        embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34),
                                description=pyfiglet.figlet_format(message, font=font))
        embed.set_footer(text=f'Requested by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Failed!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
