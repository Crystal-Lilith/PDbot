@client.listen()
async def on_command_error(ctx, error):
    message = await ctx.channel.fetch_message(ctx.message.id)
    user_cmd = message.content.split()[0].split('$')[1]
    json_files = os.listdir("cmds")
    cmds = []
    for cmd in json_files:
        with open(f'cmds/{cmd}') as f:
            data = json.load(f)
        for i in data:
            cmds.append(i)
    if user_cmd not in cmds:
        embed = discord.Embed(title='Unknown Command! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Command not found! Do `$help` for a list of commands!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
