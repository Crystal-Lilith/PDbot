@client.listen()
async def on_message_delete(message):
    log_channel = get(message.guild.channels, name='log')
    if message.content:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34))
        embed.add_field(name='Content:', value=message.content)
        embed.add_field(name='Channel:', value=message.channel.mention)
        embed.set_footer(text=f'Deleted by: {message.author}', icon_url=message.author.avatar_url)
    else:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Unable to recover')

    await log_channel.send(embed=embed)
