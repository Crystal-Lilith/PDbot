@client.listen()
async def on_command_error(ctx, error):
    if isinstance(error, discord.commands.CommandNotFound):
        pass
    elif isinstance(error, discord.commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0]
        desc = user_cmd.description.split('||')[0]
        syntax = user_cmd.description.split('||')[0]
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'{desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        print(error)
        await ctx.channel.send(error)
