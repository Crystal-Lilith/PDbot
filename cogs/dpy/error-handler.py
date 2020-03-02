@client.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(error)
        await ctx.channel.send(error)
