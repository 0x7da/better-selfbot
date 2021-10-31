import discord
import time
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'LOL', help_command = None)

colorama.init()
token = 'GOES YOUR TOKEN HERE'
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.RED}                      By Shockwave             
{Fore.RED}                      [1] Mass Dm                                                 
''')
 fuck = input(f"{Fore.GREEN}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send?>>")
  counter = 0
  for guild in client.guilds:
    for user in guild.members:
      time.sleep (1)
      counter = counter +1
      try: 
        await user.send(f"{input2}")
        print(f"{Fore.GREEN}[+] Sent{Fore.YELLOW} {input2} To {user}")
      except Exception as  e:
        print (e)
      if counter == 100:
        counter = 0
        time.sleep (1)

client.run(token, bot = False)
