#████████╗██████╗░░█████╗░░██████╗██╗░░██╗  ██████╗░██████╗░░██████╗░
#╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░██║  ██╔══██╗██╔══██╗██╔════╝░
#░░░██║░░░██████╔╝███████║╚█████╗░███████║  ██████╔╝██████╔╝██║░░██╗░
#░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██╔══██║  ██╔══██╗██╔═══╝░██║░░╚██╗
#░░░██║░░░██║░░██║██║░░██║██████╔╝██║░░██║  ██║░░██║██║░░░░░╚██████╔╝
#░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░

# Bu bot sadece trash rpg değil, aynı zamanda basit bir AFK komutu ile beraber gelir. İyi eğlenceler!+--

import discord
from discord.ext import commands


afk = "AFK Değil"

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def on_ready(self):
        print(f"Giriş yapıldı: {self.user}")

bot = MyBot()

@bot.command()
async def afk(ctx):
    global afk
    afk = "AFK"
    await ctx.send("Kullanıcı: <@{}> AFK moduna geçti.".format(ctx.author.id))

    
    if afk == "AFK":
        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return
            global afk
            if message.author == ctx.author and afk == "AFK":
                afk = "AFK Değil"
                await message.channel.send("Kullanıcı: <@{}> AFK modundan çıktı.".format(message.author.id))

            if message.mention_everyone or bot.user in message.mentions:
                await message.channel.send("Kullanıcı: <@{}> şu anda AFK modunda.".format(message.author.id))

            await bot.process_commands(message)

            
@bot.command()
async def afkcheck(ctx, member: discord.Member = None):
    global afk
    if member is None:
        await ctx.send("Lütfen bir kullanıcı etiketleyin, örnek: `!afkcheck @Kullanıcı`")
        return
    await ctx.send(f"Kullanıcı: {member.mention} AFK durumu: {afk}")

#  Aşağıdaki sistem'in kullanılabilmesi için 2 yöntem vardır;
#  1. bot.run(token) yerindeki token'i botunuzun tokeni ile değiştirebilirsiniz.
#  2. token.txt'e koyup, kodu daha da güvenli yapabilirsiniz. (Önerilir.)

with open("token.txt", "r") as f:
    token = f.read().strip()

bot.run(token)

