import discord
from discord.ext import commands
import random
from datetime import datetime, timedelta
from config import TOKEN



intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

user_join_times = {}

time_log_file = "voice_time_log.txt"

def format_duration(duration):
   # """Muotoilee keston tunneiksi, minuuteiksi ja sekunneiksi."""
    parts = []
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        parts.append(f"{int(hours)} {'tunti' if hours == 1 else 'tuntia'}")
    if minutes:
        parts.append(f"{int(minutes)} {'minuutti' if minutes == 1 else 'minuuttia'}")
    if seconds or not parts:
        # Näytä sekunnit, jos ei tunteja eikä minuutteja, tai aika on alle minuutin
        parts.append(f"{int(seconds)} {'sekunti' if seconds == 1 else 'sekuntia'}")
    return " ja ".join(parts)

def read_time_log():
    try:
        with open(time_log_file, "r") as file:
            return {int(line.split(",")[0]): float(line.split(",")[1]) for line in file if line}
    except FileNotFoundError:
        return {}

def write_time_log(user_id, time_spent):
    time_log = read_time_log()
    time_log[user_id] = time_log.get(user_id, 0) + time_spent
    with open(time_log_file, "w") as file:
        for user_id, total_time in time_log.items():
            file.write(f"{user_id},{total_time}\n")


@bot.event
async def on_ready():
    print(f'Olen valmis! Kirjautunut nimellä {bot.user}')
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            for member in channel.members:
                # Tarkistaa, että jäsen ei ole botti
                if not member.bot:
                    user_join_times[member.id] = datetime.now()
                    print(f"{member.name} on jo kanavalla {channel.name}, aloitetaan ajan seuranta.")


    
@bot.command()
async def hei(ctx):
    # Vastaa käyttäjälle "Hei" ja lisää käyttäjän nimi
    await ctx.send(f'Hei {ctx.author.name}!')


@bot.command()
async def kysy(ctx):
    vastaukset = []
    # Lue vastaukset tiedostosta
    with open('kysy.txt', 'r', encoding='utf-8') as f:
        vastaukset = f.readlines()
    
    # Valitse satunnainen vastaus
    valittu_vastaus = random.choice(vastaukset).strip()
    await ctx.send(valittu_vastaus)

@bot.event
async def on_voice_state_update(member, before, after):
    current_time = datetime.now()
    print(f"{member.name} tila muuttui")

    if before.channel is None and after.channel is not None:
        user_join_times[member.id] = current_time
        print(f"{member.name} liittyi kanavalle {after.channel.name}")
    elif before.channel is not None and (after.channel is None or before.channel != after.channel):
        join_time = user_join_times.pop(member.id, None)
        if join_time:
            time_spent = (current_time - join_time).total_seconds()
            write_time_log(member.id, time_spent)
            time_spent_td = timedelta(seconds=int(time_spent))
            time_formatted = str(time_spent_td)
            time_formatted = format_duration(time_spent)
            print(f"{member.name} vietti {time_formatted} kanavalla {before.channel.name if before.channel else 'N/A'}")

@bot.command()
async def aika(ctx):

    current_time = datetime.now()

    member = ctx.author

    join_time = user_join_times.get(member.id, None)
    if join_time:
        time_spent = (current_time - join_time).total_seconds()
        time_formatted = format_duration(time_spent)
        await ctx.send(f"{member.name} on ollut kanavalla {time_formatted}.")
    else:
        await ctx.send(f"{member.name} ei ole tällä hetkellä puhekanavalla.")

@bot.command()
async def kokonaisaika(ctx):

    member = ctx.author

    join_time = user_join_times.get(member.id, None)
    if join_time:
        current_time = datetime.now()
        time_spent = (current_time - join_time).total_seconds()
        write_time_log(member.id, time_spent)

    time_log = read_time_log()
    total_time_seconds = time_log.get(member.id, 0)
    time_formatted = format_duration(total_time_seconds)
    await ctx.send(f"{member.name} on viettänyt yhteensä {time_formatted} puhekanavilla.")



bot.run(TOKEN)