@client.command()
async def slap(ctx):
  await ctx.channel.send(f'*Slapped* {ctx.author.mention}')