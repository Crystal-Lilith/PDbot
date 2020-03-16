@client.command(description='Creates a vote||<timer(days)> <desc>')
@commands.has_role('Owner')
async def cv(ctx, timer, *, desc):
    try:
        float(timer)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Timer must be a int or float!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
        return

    global vote_amount
    vote_channel = get(ctx.guild.channels, name='✅vote')
    if 'vote_amount' in globals():
        pass
    else:
        vote_amount = 0
    current_vote_count = vote_amount + 1
    embed = discord.Embed(title=f'Vote #{current_vote_count} [{timer} days]', color=discord.Color.from_rgb(0, 255, 0),
                            description=f'{desc}\n\n```✅: Yes\n🚫: No```')
    embed.set_footer(text=f'Vote started by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
    vote = await vote_channel.send(embed=embed)

    vote_amount += 1

    for i in ['✅', '🚫']:
        await vote.add_reaction(i)
    await asyncio.sleep(float(timer) * 60 * 60 * 24)

    vote = await vote_channel.fetch_message(vote.id)
    for i in vote.reactions:
        if i.emoji == '✅':
            yes = get(vote.reactions, emoji=i.emoji).count
        elif i.emoji == '🚫':
            no = get(vote.reactions, emoji=i.emoji).count
        else:
            pass
    if yes > no:
        embed = discord.Embed(title=f'Vote #{current_vote_count} ✅', color=discord.Color.from_rgb(0, 255, 0),
                                description=f'Approved!\n\n`✅ had {yes - no} more vote(s)!`\n\n```✅: {yes}\n🚫: {no}```')
    elif no > yes:
        embed = discord.Embed(title=f'Vote #{current_vote_count} 🚫', color=discord.Color.from_rgb(178, 34, 34),
                                description=f'Denied!\n\n`🚫 had {no - yes} more vote(s)!`\n\n```✅: {yes}\n🚫: {no}```')
    else:
        embed = discord.Embed(title=f'Vote #{current_vote_count} ❗', color=discord.Color.from_rgb(0, 191, 255),
                                description=f'Tied!\n\n`Vote tied!`\n\n```✅: {yes}\n🚫: {no}```')

    embed.set_footer(text=f'Ended the vote made by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
    await vote_channel.send(embed=embed)
    vote_amount -= 1

@cv.error
async def cv_error(ctx, error):
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
