@client.listen()
async def on_command_error(ctx, error):
    message = await ctx.channel.fetch_message(ctx.message.id)
    user_cmd = message.content.split()[0].split('$')[1]
    if user_cmd == 'update':
        pass
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='Unknown Command! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Command not found! Do `$help` for a list of commands!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    # else:
    #     print(error)
    #     await ctx.channel.send(error)
