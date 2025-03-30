import os
import asyncio
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv, dotenv_values

load_dotenv()
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
verified_role = os.getenv("verified_role_id")  #Insert ID in .env
role1 = os.getenv("role1")  #Insert ID in .env
role2 = os.getenv("role2")  #Insert ID in .env
unverified_role = os.getenv("unverified_role")  #Insert ID in .env

GUILD_ID = os.getenv("guild_id")  #Insert ID in .env
current_set = set()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_update(after):
    guild = bot.get_guild(os.getenv("guild_id"))
    member = after
    if member.guild.id != GUILD_ID:
        return
    
    if member.id in current_set:
        return
    
    if any(role.id == role1 for role in member.roles) and any(role.id == role2 for role in member.roles):
        current_set.add(member.id)
        await member.add_roles(guild.get_role(verified_role))
        await member.remove_roles(guild.get_role(unverified_role))
        await member.remove_roles(guild.get_role(role1))
        await member.remove_roles(guild.get_role(role2))
        await member.send("Welcome to my palace hun!. Grab your roles and introduce yourself")
        print(f'{member} has been verified')
        
        await asyncio.sleep(15)
        current_set.discard(member.id)

bot.run(os.getenv("discord_bot_token")) #Insert token in .env