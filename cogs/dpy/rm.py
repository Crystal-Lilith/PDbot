@client.command(description='Deletes messages in a channel||<amount>')
async def rm(ctx, amount):
    if not ctx.author.permissions_in(ctx.channel).manage_messages:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51), description='You do not have the correct permissions (manage messages) to use this command!')
        embed.set_footer(text=f'Attempted By: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
        return
    try:
        amount = int(amount)
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description=f'Deleted {amount} messages!')
        embed.set_footer(text=f'Messages deleted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.purge(limit=(amount + 1))
        await ctx.channel.send(embed=embed, delete_after=10)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51), description='Amount must be an integer!')
        embed.set_footer(text=f'Attempted By: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@rm.error
async def rm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
