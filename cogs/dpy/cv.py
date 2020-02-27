@client.command(description='Creates a vote')
@commands.has_role('Owner')
async def cv(ctx, timer, *, desc):
    try:
        float(timer)
    except:
        embed = discord.Embed(title='Error!', color=discord.Color.from_rgb(255, 255, 51),
                                description='Timer must be a int or float!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
        return

    global vote_amount
    if 'vote_amount' in globals():
        pass
    else:
        vote_amount = 0
    embed = discord.Embed(title=f'#{vote_amount+1} Vote [{timer}min]', color=discord.Color.from_rgb(0, 255, 0), description=desc)
    embed.set_footer(text=f'Vote started by: {ctx.message.author}')
    vote = await ctx.channel.send(embed=embed)

    vote_amount += 1

    for i in ['✅', '🚫']:
        await vote.add_reaction(i)
    vote = await ctx.channel.fetch_message(vote.id)
    await asyncio.sleep(float(timer) * 60)

    for i in vote.reactions:
        if i.emoji == '✅':
            yes = vote.reactions.count(i)
        elif i.emoji == '🚫':
            no = vote.reactions.count(i)
        else:
            await ctx.channel.send('not working')
    embed = discord.Embed(title=f'Vote #{vote_amount}', color=discord.Color.from_rgb(0, 255, 0), description=f'Vote ended!\n✅: {yes}\n🚫: {no}')
    embed.set_footer(text=f'Ended the vote made by: {ctx.message.author}')
    await ctx.channel.send(embed=embed)
