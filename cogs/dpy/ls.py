@client.command(description='Shows you all files in the specified directory')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def ls(ctx, directory):
    for x in directory.lower().split('/'):
        if i in ['.env', 'start.sh']:
            return
    x=''
    for i in listdir(directory):
        x = f"{x}{i}\n"
    embed = discord.Embed(title=f'List of files in {directory}', color=discord.Color.from_rgb(0, 191, 255), description=f'```{x[:-1]}```')
    await ctx.channel.send(embed=embed)
    del(x, i, embed)
