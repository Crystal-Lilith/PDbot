@client.command()
async def dp(ctx, projectname):    
    if get(ctx.author.roles, name=f"{projectname} Founder"):
        #channels = ['sources', 'to-do-list', 'suggestions', 'known-bugs', 'general', 'bot-commands']
        founder = get(ctx.guild.roles, name=f"{projectname} Founder")
        dev = get(ctx.guild.roles, name=f"{projectname} Dev")
        category = get(ctx.guild.categories, name=f"{projectname} Dev")

        channels = []
        # for server in Client.servers:
        #     for channel in server.channels:
        for channel in get(category.channels):
            channels.append(channel)
        # await founder.delete()
        # await dev.delete()
        for channel in channels:
            await ctx.channel.delete()

        # for i in channels:
        #     channel = get(ctx.guild.text_channels, name=i, category=category)
        #     await channel.delete()

        # await get(ctx.guild.voice_channels, name='chat', category=category).delete()
        
        # await category.delete()

        # await ctx.channel.send(f"Category **{projectname}** deleted!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to delete it!')
