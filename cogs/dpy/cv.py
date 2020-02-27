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
    vote_channel = get(ctx.guild.channels, name='✅vote')
    if 'vote_amount' in globals():
        pass
    else:
        vote_amount = 0
    embed = discord.Embed(title=f'#{vote_amount+1} Vote [{timer}min]', color=discord.Color.from_rgb(0, 255, 0), description=f'{desc}\n✅: Yes\n🚫: No')
    embed.set_footer(text=f'Vote started by: {ctx.message.author}')
    vote = await vote_channel.send(embed=embed)

    vote_amount += 1

    for i in ['✅', '🚫']:
        await vote.add_reaction(i)
    await asyncio.sleep(float(timer) * 60)
    
    vote = await vote_channel.fetch_message(vote.id)
    for i in vote.reactions:
        if i.emoji == '✅':
            yes = get(vote.reactions, emoji=i.emoji).count
        elif i.emoji == '🚫':
            no = get(vote.reactions, emoji=i.emoji).count
        else:
            pass
    embed = discord.Embed(title=f'Vote #{vote_amount}', color=discord.Color.from_rgb(0, 255, 0), description=f'Vote ended!\n✅: {yes}\n🚫: {no}')
    embed.set_footer(text=f'Ended the vote made by: {ctx.message.author}')
    await vote_channel.send(embed=embed)
