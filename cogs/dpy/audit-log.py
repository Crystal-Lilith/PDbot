@client.listen()
async def on_raw_message_delete(message):
    # message_guild = await client.fetch_guild(message.guild_id)
    message_channel = await client.fetch_channel(message.channel_id)
    deleted_message = await message_channel.fetch_message(message.message_id) 
    log_channel = get(message_guild.channels, name='log')
    # embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
    #                             description=message.content)
    # embed.set_footer(text=f'Deleted by: {message.author}', icon_url=message.author.avatar_url)
    # await log_channel.send(embed=embed, files=message.attachments)
    print(deleted_message.content)
