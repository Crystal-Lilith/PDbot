@client.command(description='Gives a would you rather question||None')
async def wyr(ctx):
    try:
        page = requests.get('https://conversationstartersworld.com/would-you-rather-questions/')
        soup = BeautifulSoup(page.content, 'html.parser')
        questions = soup.find(class_='post-456 page type-page status-publish has-post-thumbnail entry').find_all('h3')
        question = random.choice(questions).get_text()[4:]

        embed = discord.Embed(title='Would you rather? 🤔', color=discord.Color.from_rgb(0, 191, 255), 
                                description=question)
        embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Failed to get questions')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@wyr.error
async def wyr_error(ctx, error):
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
