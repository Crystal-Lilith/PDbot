@client.listen()
async def on_message_delete(message):
    log_channel = get(message.guild.channels, name='log')
    if message.content:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description=message.content)
        embed.set_footer(text=f'Deleted by: {message.author}', icon_url=message.author.avatar_url)
        await log_channel.send(embed=embed, files=message.attachments)
    else:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Unable to recover')
        embed.set_footer(text=f'Deleted by: {message.author}', icon_url=message.author.avatar_url)
        await log_channel.send(embed=embed)
