from hata import enter_executor

@commands.has_role('PDBot Dev')
@client.command()
async def dexec(ctx, *code):
    output=exec(code)
    if len(output) > 2000:
        async with enter_executor():
            with open('output.txt') as f:
                f.write(output)
        await ctx.send(content='Output was too long, here is the output in a file', file='output.txt')
    else:
        await ctx.send(output)
