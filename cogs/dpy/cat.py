@client.command(description='Outputs file content||<file>')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cat(ctx, *, directory):
    if directory.startswith("./"):
        pass
    else:
        directory = f'./{directory}'
    try:
        split_directory = directory.split('/')
        for i in ['..', '.env', 'start.sh']:
            if i in split_directory:
                embed = discord.Embed(title='Warning ❗', color=discord.Color.from_rgb(178, 34, 34),
                                description='You may not cat this file!')
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
                return
        lang = ''
        if split_directory[-1].split('.')[-1] == 'py':
            lang = 'python'
        elif split_directory[-1].split('.')[-1] == 'rb':
            lang = 'ruby'
        elif split_directory[-1].split('.')[-1] == 'json':
            lang = 'json'
        else:
            pass
        with open(directory, 'r') as f:
            contents = f.read()
        if len(contents) < 2000:
            embed = discord.Embed(title=f'Contents in `{directory}` ✅', color=discord.Color.from_rgb(0, 191, 255),
                                    description=f'```{lang}\n{contents}```')
            embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            with open('output.txt', 'w') as fp:
                fp.write(contents)
            embed = discord.Embed(title=f'Contents in `{directory}` was too long ❗', color=discord.Color.from_rgb(0, 191, 255),
                                    description='File contents was over 2000 characters! Sent as output.txt')
            embed.set_footer(text=f'Requested by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed, file=discord.File('output.txt'))
            os.remove('output.txt')
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='File doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
