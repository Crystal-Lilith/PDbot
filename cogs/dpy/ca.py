@client.command(description='Creates announcement')
@commands.has_role('Owner')
async def ca(ctx, option, title, *, message):
    announce = get(ctx.guild.channels, name='📢server-announcements')
    await ctx.announce.embed(title=f'**+**[{title}]', color=discord.Color.from_rgb(0, 191, 255), description=message)
    await ctx.channel.send('Announcement posted!')
