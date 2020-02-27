# @client.command(description='Shows you all files in the specified directory')
# @commands.has_any_role('PDBot Mod', 'PDBot Dev')
# async def ls(ctx, *, directory):
#     for x in directory.lower().split('/'):
#         if x == '.env' or if x == 'start.sh':
#             return
#     f = []
#     for (dirpath, dirnames, filenames) in walk(directory):
#         f.extend(filenames)
#         break
#     for i in os.listdir(directory):
#         x = f"{x}{i}\n"
#     files = os.listdir('.')[:-1]
#     embed = discord.Embed(title=f'List of files in {directory}', color=discord.Color.from_rgb(0, 191, 255), description=f'```{}```')
#     await ctx.channel.send(embed=embed)
