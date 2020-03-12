@Client.command()
async def dm(ctx, channel_name, *, msg):
  msg_channel = get(ctx.guild.channel, name=channel_name)
  await msg_channel.send(msg)
