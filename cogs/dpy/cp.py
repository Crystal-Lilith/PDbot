@client.command()
async def cp(ctx, projectname):
    await ctx.channel.purge(limit=1)
    channels = ['test'] # 'sources', 'to-do-list', 'suggestions', 'known-bugs', 'general'

    await ctx.guild.create_role(name=f"{projectname} Dev", mentionable=True)
    role = get(ctx.guild.roles, name=f"{projectname} Dev")
    await ctx.message.author.add_roles(role)


    await ctx.guild.create_category(f"{projectname} Dev")
    category = get(ctx.guild.categories, name=f"{projectname} Dev")
    # await category.set_permissions(role, read_message_history=True, send_messages=True)


    for i in channels:
        await ctx.guild.create_text_channel(i, category=category)
    await ctx.guild.create_voice_channel('chat', category=category)
    await ctx.channel.send(f"Category {projectname} created!")
