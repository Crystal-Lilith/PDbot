@client.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(error)
        embed = discord.Embed(title='Error!', color=discord.Color.from_rgb(255, 255, 51),
                                description=error)
        await ctx.channel.send(embed=embed)
