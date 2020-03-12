@Client.command()
@commands.has_any_role('PDBot Dev', 'PDBot Mod')
async def dm(ctx, category, channel_name, *, msg):
  category = get(ctx.guild.categories, name=f"{projectname} Dev")
  msg_channel = get(ctx.guild.channel, category=category, name=channel_name)
  await msg_channel.send(msg)
