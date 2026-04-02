import discord
from discord.ext import commands
from discord import app_commands, message

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

token ='MTQ4ODkzMTE2OTE2Nzg2ODExNg.GH8X-A.UQ4OmC3NWEx-XUjjAODIwEUd4dQsXuWU0d7Xq8'

@bot.event
async def on_ready():
    print("Bot Online")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")



# แจ้งคนเข้าออก
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1488971680750633142)
    text = f"สวัสดีจ้า {member.mention}!"

    emmbed = discord.Embed(title = 'เฮ้ย' ,
                           description = text,
                           colour = 0xD8A7B1)

    await channel.send(text)
    await channel.send(embed = emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1488971680750633142)
    text = f"ลาก่อนมะพร้าว {member.mention}!"
    await channel.send(text)


#ส่งข้อความ
@bot.event
async def on_message(message):
    mes = message.content
    if mes == "แฮมสเตอร์":
        await message.channel.send("ครับผม")
    elif mes == 'mr.Johnny':
        await message.channel.send("ครับผม" + str(message.author.name))

        await bot.process_commands(message)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# /
@bot.tree.command(name='ยอดเงิน', description='ดูยอดเงิน')
async def Money(interaction):
    await interaction.response.send_message("ยอดเงินรวมทั้งชีวิตคือ 0 ")
#คำถาม
@bot.tree.command(name='name')
@app_commands.describe(name= "What's your name?")
async def namecommand(interaction, name : str ):
    await interaction.response.send_message(f"Welcome to {name}")

bot.run (token)