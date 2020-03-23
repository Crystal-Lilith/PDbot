@client.listen()
async def on_message_delete(message):
    log_channel = get(message.guild.channels, name='log')
    try:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34))
        embed.add_field(name='Content:', value=message.content)
        embed.add_field(name='Channel:', value=message.channel.mention)
        embed.set_footer(text=f'Deleted message author: {message.author}', icon_url=message.author.avatar_url)
    except:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Unable to recover')

    await log_channel.send(embed=embed)

@client.listen()
async def on_message_edit(old_message, new_message):
    log_channel = get(message.guild.channels, name='log')
    try:
        embed = discord.Embed(title='Message Updated ♻️', color=discord.Color.from_rgb(178, 34, 34))
        embed.add_field(name='Old:', value=old_message.content)
        embed.add_field(name='New:', value=new_message.content)
        embed.add_field(name='Channel:', value=old_message.channel.mention)
        embed.set_footer(text=f'Message updated by: {old_message.author}', icon_url=message.author.avatar_url)
    except:
        embed = discord.Embed(title='Message Updated ♻️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Failed to display contents')

    await log_channel.send(embed=embed)
