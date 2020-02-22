@client.command(description='Creates announcement')
@commands.has_role('Owner')
async def ca(ctx, option, title, *, message):
    announce = get(ctx.guild.channels, name='📢server-announcements')
    embed = discord.Embed(title=f'**+**[{title}]', color=discord.Color.from_rgb(0, 191, 255), description=message)
    embed.set_author(ctx.message.author)
    await announce.send(embed=embed)
    await ctx.channel.send('Announcement posted!')
