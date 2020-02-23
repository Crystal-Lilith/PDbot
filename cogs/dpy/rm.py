@client.command(description='Deletes messages in a channel')
@commands.has_role('Owner')
async def rm(ctx, amount):
    try:
        amount = int(amount) + 1
        await ctx.channel.purge(amount)
        await ctx.channel.send(f'Deleted {amount} messages!', delete_after=10)
    except:
        await ctx.channel.send('Amount must be an integer!')
