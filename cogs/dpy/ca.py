@client.command(description='Creates announcement')
@commands.has_role('Owner')
async def ca(ctx, option, title, *, message):
    if option == 'general' or option == 'add' or option == 'remove' or option == 'modify':
        if option == 'general':
            embed = discord.Embed(title={title}, color=discord.Color.from_rgb(0, 191, 255), description=message)
        if option == 'add':
            embed = discord.Embed(title=f'**+**[{title}]', color=discord.Color.from_rgb(0, 255, 0), description=message)
        if option == 'remove':
            embed = discord.Embed(title=f'**-**[{title}]', color=discord.Color.from_rgb(178, 34, 34), description=message)
        if option == 'modify':
            embed = discord.Embed(title=f'**/**[{title}]', color=discord.Color.from_rgb(255, 255, 51), description=message)
        announce = get(ctx.guild.channels, name='📢server-announcements')
        embed.set_footer(text=f'Author: {ctx.message.author}')
        await announce.send(embed=embed)
        await ctx.channel.send('Announcement posted!')
    else:
        await ctx.channel.send('Invalid option!')
