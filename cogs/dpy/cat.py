@client.command(description='Outputs file content')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cat(ctx, *, directory):
    try:
        directory = directory.split('/')
        for i in directory:
            if i.lower() in [".env", "start.sh"]:
                embed = discord.Embed(title='Warning ❗', color=discord.Color.from_rgb(178, 34, 34),
                                description='You may not cat this file!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author}')
                await ctx.channel.send(embed=embed)
            elif i == directory[-1]:
                with open(directory, 'r') as f:
                    i = i.lower().split('.')
                    lang = ''
                    if i[-1] == 'py':
                        lang = 'python'
                    elif i[-1] == 'rb':
                        lang = 'ruby'
                    else:
                        pass
                    embed = discord.Embed(title=f'List of files and folders in `{directory}`', color=discord.Color.from_rgb(0, 191, 255), description=f'```{lang}\n{f.read()}```')
                    embed.set_footer(text=f'Requested by: {ctx.message.author}')
                    await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='File doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
