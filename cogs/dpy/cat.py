@client.command(description='Outputs file content')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cat(ctx, *, directory):
    try:
        with open(directory, 'r') as f:
            embed = discord.Embed(title=f'List of files and folders in `{directory}`', color=discord.Color.from_rgb(0, 191, 255), description=f'```css\n{f.read()}```')
            embed.set_footer(text=f'Attempted by: {ctx.message.author}')
            await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='File doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
