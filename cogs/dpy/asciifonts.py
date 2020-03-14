@client.command(description='Displays ascii fonts||None')
async def asciifonts(ctx):
    try:
        page = requests.get('http://www.figlet.org/fontdb.cgi')
        soup = BeautifulSoup(page.content, 'html.parser')
        fonts = soup.find_all('td')
        font = ''

        for i in fonts[1::3]:
            text = i.get_text().strip()
            if text != 'Font Name' and text != 'Contact us at info@figlet.org':
                font = f'{font}{text}\n'

        embed = discord.Embed(title='Fonts', color=discord.Color.from_rgb(0, 191, 255), 
                                description=font)
        embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Failed to get fonts')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@asciifonts.error
async def asciifonts_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
