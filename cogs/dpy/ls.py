@client.command(description='Shows you all files in the specified directory')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def ls(ctx, *, directory='.'):
    x = ''
    for i in os.listdir(directory):
        if x.lower() not in [".env", "start.sh"]:
            x = f"{x}{i}\n"
    embed = discord.Embed(title=f'List of files and folders in `{directory}`', color=discord.Color.from_rgb(0, 191, 255), description=f'```css\n{x}```')
    await ctx.channel.send(embed=embed)
