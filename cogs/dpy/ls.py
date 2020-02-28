@client.command(description='Shows you all files in the specified directory')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def ls(ctx, *, directory='.'):
    try:
        x = ''
        for i in os.listdir(directory):
            if x.lower() not in [".env", "start.sh"]:
                x = f"{x}{i}\n"
            else:
                embed = discord.Embed(title='Warning! ❗', color=discord.Color.from_rgb(178, 34, 34),
                                description='You may not ls this directory!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author}')
                return
        embed = discord.Embed(title=f'List of files and folders in `{directory}`', color=discord.Color.from_rgb(0, 191, 255), description=f'```css\n{x}```')
        embed.set_footer(text=f'Requested by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Directory doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
