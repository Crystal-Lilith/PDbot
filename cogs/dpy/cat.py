from os import listdir

@client.command(description="Shows you all files in the specified directory")
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cat(ctx, dir):
    x=""
    for i in listdir(dir):
        x = f"{x}{i}\n"
    embed = discord.Embed(title=f'List of files in {dir}', color=discord.Color.from_rgb(0, 191, 255), description=f'```{x[:-1]}```')

