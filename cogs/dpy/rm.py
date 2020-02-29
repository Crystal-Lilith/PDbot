@client.command(description='Deletes messages in a channel||<amount>')
@commands.has_role('Owner')
async def rm(ctx, amount):
    try:
        amount = int(amount)
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description=f'Deleted {amount} messages!')
        embed.set_footer(text=f'Messages deleted by: {ctx.message.author}')
        await ctx.channel.purge(limit=(amount + 1))
        await ctx.channel.send(embed=embed, delete_after=10)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51), description='Amount must be an integer!')
        embed.set_footer(text=f'Attempted By: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
