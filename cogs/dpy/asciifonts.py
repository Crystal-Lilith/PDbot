@client.command(description='Creates ascii art||None')
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
                                description=text)
        embed.set_footer(text=f'Requested by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Failed to get fonts')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
