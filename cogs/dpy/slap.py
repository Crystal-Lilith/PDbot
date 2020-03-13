@client.command(description='Slaps the mentioned user||<username>')
async def slap(ctx, user=None):
    try:
        user=discord.User(user)
    except:
        pass
    if user==None:
        user=ctx.author.mention
    await ctx.send("*Slapped* "+user+"")
