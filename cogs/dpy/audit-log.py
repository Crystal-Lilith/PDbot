@client.listen()
async def on_message_delete(message):
    log_channel = get(ctx.guild.channels, name='log')
    embed = discord.Embed(title='Message Deleted 🗑️', color=discord.Color.from_rgb(178, 34, 34),
                                description=message.content)
    embed.set_footer(text=f'Deleted by: {message.author}', icon_url=message.author.avatar_url)
    await ctx.channel.send(embed=embed, files=message.attachments)
