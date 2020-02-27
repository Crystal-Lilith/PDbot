@client.command(description='Creates a vote')
@commands.has_role('Owner')
async def cv(ctx, timer, *, desc):
    embed = discord.Embed(title=f'Vote [Timer: {timer}]', color=discord.Color.from_rgb(0, 255, 0), description=message)
    embed.set_footer(text=f'Author: {ctx.message.author}')
    vote = await ctx.channel.send(embed=embed)
    for i in ['✅', '⛔']:
        await vote.add_reaction(i)
