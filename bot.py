import discord
from discord.ext.commands import Bot
from datetime import datetime

bot = Bot(command_prefix = None)

@bot.event
async def on_message(message):
    time_now = datetime.now()
    time_now = time_now.strftime('%d.%m.%Y %H:%M')
    if (message.author.id != 707149650192367708):
        log_channel = bot.get_channel(707151946015834174)
        embed = discord.Embed(type = 'rich',
                    description = f'Автор сообщения - <@{message.author.id}>\n({message.channel.mention})',
                    title = message.jump_url)
        value = ''
        if (len(message.content) <= 950):
            value = message.content + '\n'
        else:
            value = message.content[:950] + '...' + '\n'
        if (message.embeds != []):
            value += 'Содержит вложение.'
            value += '\n'
        if (message.attachments != []):
            value += 'Содержит файл/картинку.'
            value += '\n'

        embed.add_field(name = 'Содержание:', value = value)
        embed.set_footer(text = time_now, icon_url = message.author.avatar_url if (message.author.avatar_url) else Embed.Empty)
        await log_channel.send(embed = embed)

with open('config.txt', 'r') as f:
    TOKEN = f.read()
bot.run(TOKEN)
