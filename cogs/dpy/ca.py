@client.command(description='Creates announcement||<general/add/remove/modify> <title> <desc>')
@commands.has_role('Owner')
async def ca(ctx, option, title, *, message):
    if option == 'general' or option == 'add' or option == 'remove' or option == 'modify':
        if option == 'general':
            embed = discord.Embed(title=f'{title} :tada:', color=discord.Color.from_rgb(0, 191, 255), description=message)
        if option == 'add':
            embed = discord.Embed(title=f'**+**[{title}] :tada:', color=discord.Color.from_rgb(0, 255, 0), description=message)
        if option == 'remove':
            embed = discord.Embed(title=f'**-**[{title}] :tada:', color=discord.Color.from_rgb(178, 34, 34), description=message)
        if option == 'modify':
            embed = discord.Embed(title=f'**/**[{title}] :tada:', color=discord.Color.from_rgb(255, 255, 51), description=message)
        announce = get(ctx.guild.channels, name='📢server-announcements')
        embed.set_footer(text=f'Author: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await announce.send(embed=embed)
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description='Announcement posted!')
        embed.set_footer(text=f'Announcement posted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51), description='Invalid option!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
