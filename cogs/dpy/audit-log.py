@client.listen()
async def on_message_delete(message):
    log_channel = get(message.guild.channels, name='log')
    try:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34))
        embed.add_field(name='Content:', value=message.content)
        embed.add_field(name='Channel:', value=message.channel.mention)
        embed.set_footer(text=f'Deleted message author: {message.author.name}', icon_url=message.author.avatar_url)
    except:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Unable to recover')

    await log_channel.send(embed=embed)
