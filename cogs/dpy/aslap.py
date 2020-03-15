@client.command(description='Slaps the mentioned user anonymously||<username>')
async def aslap(ctx, user: discord.User):
  await ctx.channel.purge(limit=1)
  await ctx.channel.send(f'*Slapped* {user.mention}')
