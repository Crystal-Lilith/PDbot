@client.command()
@commands.has_any_role(673405620527038478, 682105898642047233)
async def dm(ctx, user: discord.User, *, msg):
  await user.send(msg)
  await ctx.channel.send(f'Message `{msg}` sent')
