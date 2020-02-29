@client.command(description='Gives a would you rather question||$wr')
async def wyr(ctx):
    # try:
    page = requests.get('https://www.signupgenius.com/groups/would-you-rather.cfm')
    soup = BeautifulSoup(page.content, 'html.parser')
    questions = soup.find('ol').find_all('li')
    #question = questions.get_text() # random.choice(questions).

    embed = discord.Embed(title='Would you rather?', color=discord.Color.from_rgb(0, 191, 255), 
                            description=questions)
    embed.set_footer(text=f'Requested by: {ctx.message.author}')
    await ctx.channel.send(embed=embed)
    # except:
        # embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
        #                         description='Failed to get questions')
        # embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        # await ctx.channel.send(embed=embed)
