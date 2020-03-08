@client.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='Unknown Command! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Command not found! Do `$help` for a list of commands!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    # else:
    #     print(error)
    #     await ctx.channel.send(error)
