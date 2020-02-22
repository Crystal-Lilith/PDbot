@client.command(description='Creates announcement')
@clinet.has_role('Owner')
async def ac(ctx, option, title, *, message):
    announce = get(ctx.guild.channels, name='📢server-announcements')
    await ctx.announce.embed(title=f'**+**[{title}]', color=discord.Color.from_rgb(0, 191, 255), description=message)
    await ctx.channel.send('Announcement posted!')