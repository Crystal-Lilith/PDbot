@client.command()
@commands.has_roles(673405620527038478,682105898642047233)
async def dm(ctx, user: discord.User, msg):
  await user.send(msg)
  ctx.channel.send('Message Sent')
