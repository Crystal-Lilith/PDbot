@client.command(description='Creates new project||<project-name>')
async def cp(ctx, *, projectname):
    projectname = projectname.lower()
    if not get(ctx.guild.roles, name=f'{projectname} Founder'):
        channels = ['sources', 'to-do-list', 'suggestions', 'known-bugs', 'general', 'bot-commands']
        color = discord.Color.from_rgb(randint(0,255), randint(0,255), randint(0,255))

        await ctx.guild.create_role(name=f'{projectname} Founder', mentionable=True, color=color)
        await ctx.guild.create_role(name=f'{projectname} Dev', mentionable=True, color=color)
        await asyncio.sleep(4)
        founder = get(ctx.guild.roles, name=f'{projectname} Founder')
        dev = get(ctx.guild.roles, name=f'{projectname} Dev')
        manager = get(ctx.guild.roles, name='Manager')
        mod = get(ctx.guild.roles, name='Moderator')
        await ctx.message.author.add_roles(founder)

        bot = get(ctx.guild.roles, name='PDBot')

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            founder: discord.PermissionOverwrite(manage_channels = True,
                                            read_messages = True,
                                            view_channel = True,
                                            send_messages = True,
                                            send_tts_messages = True,
                                            manage_messages = True,
                                            embed_links = True,
                                            attach_files = True,
                                            read_message_history = True,
                                            manage_roles = False,
                                            manage_permissions = True,
                                            manage_webhooks = True),
            dev: discord.PermissionOverwrite(manage_channels = False,
                                            read_messages = True,
                                            view_channel = True,
                                            send_messages = True,
                                            send_tts_messages = True,
                                            manage_messages = True,
                                            embed_links = True,
                                            attach_files = True,
                                            read_message_history = True,
                                            manage_roles = False,
                                            manage_permissions = False,
                                            manage_webhooks = True),
            manager: discord.PermissionOverwrite(manage_channels = True,
                                            read_messages = True,
                                            view_channel = True,
                                            send_messages = True,
                                            send_tts_messages = True,
                                            manage_messages = True,
                                            embed_links = True,
                                            attach_files = True,
                                            read_message_history = True,
                                            manage_roles = True,
                                            manage_permissions = True,
                                            manage_webhooks = True),
            mod: discord.PermissionOverwrite(manage_channels = True,
                                            read_messages = True,
                                            view_channel = True,
                                            send_messages = True,
                                            send_tts_messages = True,
                                            manage_messages = True,
                                            embed_links = True,
                                            attach_files = True,
                                            read_message_history = True,
                                            manage_roles = True,
                                            manage_permissions = True,
                                            manage_webhooks = True),
            bot: discord.PermissionOverwrite(manage_channels = True,
                                            read_messages = True,
                                            view_channel = True,
                                            send_messages = True,
                                            send_tts_messages = True,
                                            manage_messages = True,
                                            embed_links = True,
                                            attach_files = True,
                                            read_message_history = True,
                                            manage_roles = True,
                                            manage_permissions = True,
                                            manage_webhooks = True
                                            )
        }

        await ctx.guild.create_category(f'{projectname} Dev', overwrites=overwrites)
        category = get(ctx.guild.categories, name=f'{projectname} Dev')


        for i in channels:
            await ctx.guild.create_text_channel(i, category=category)
        await ctx.guild.create_voice_channel('chat', category=category)
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description=f'Category **{projectname}** created!')
        embed.set_footer(text=f'Project created by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='That project already exists!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@cp.error
async def cp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
