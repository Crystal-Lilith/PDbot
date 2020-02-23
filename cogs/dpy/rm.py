@client.command(description='Deletes messages in a channel')
@commands.has_role('Owner')
async def rm(ctx, amount):
    try:
        amount = int(amount)
        embed = discord.Embed(title=f'Deleted [{amount}]', color=discord.Color.from_rgb(0, 255, 0),
                                description=f'Deleted {amount} messages!')
        await ctx.channel.purge(limit=(amount + 1))
        await ctx.channel.send(embed=embed, delete_after=10)
    except:
        embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(178, 34, 34), description='Amount must be an integer!')
        await ctx.channel.send(embed=embed)
