@commands.has_role("#") #<---YOUR ROLE NAME HERE   
@bot.command() 
async def speak(ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")