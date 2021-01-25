import random, string, requests, time
from colorama import Fore
from discord_webhook import DiscordWebhook
import os
os.system("cls" or "clear")
print(Fore.RED+"""

Discord Server :  https://discord.gg/eJeHG7D6pm
   _____ _               _                       __ 
  / ____| |             | |                     /_ |
 | |    | |__   ___  ___| | _____ _ __     __   _| |
 | |    | '_ \ / _ \/ __| |/ / _ \ '__|    \ \ / / |
 | |____| | | |  __/ (__|   <  __/ |        \ V /| |
  \_____|_| |_|\___|\___|_|\_\___|_|         \_/ |_|
                                                    
                                                    
    Made By : K4Sp3r
     Insta : @K4S 
      Snap : Fuun
"""+Fore.WHITE)
time.sleep(.5)
hmletters = int(input('how many letters you want to check : '))
print("")
websit = input('what is the website you want to check : ')
print("")
web = list(websit)
webs = web[:-1]
webss = ''.join(webs)
wbhook = str(input("Webhook : "))
print("")
time.sleep(.3)
print(" ")
while True:
    usernames = ('').join(random.choices(string.ascii_lowercase + string.digits, k=hmletters))
    webhook = DiscordWebhook(url=wbhook, content=f'`{usernames}` | Might be Available or Banned on => ||`{webss}`|| |')
    r = requests.get(f'https://{websit}{usernames}')
    if r.status_code == 200:
        print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
    else:
        print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {usernames}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
        f = open("availables.txt", "a", encoding='utf-8')
        f.write(f"{usernames} | Might be Available or Banned on => {webss} |\n")
        webhook.execute()
