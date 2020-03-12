@client.command()
async def slap(ctx, user=None):
    if user==None:
        user=ctx.author.mention
    await ctx.send("*Slapped "+user+"*")