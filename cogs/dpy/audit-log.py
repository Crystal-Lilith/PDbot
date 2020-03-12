@client.listen()
async def on_message_delete(message):
    log_channel = get(message.guild.channels, name='log')
    if message.content:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description=message.content)        
    else:
        embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description='Unable to recover')

    embed.add_field(name='channel', value=f'#{message.channel}')
    embed.set_footer(text=f'Deleted by: {message.author} | In #{message.channel}', icon_url=message.author.avatar_url)
    await log_channel.send(embed=embed)
