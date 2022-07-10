import os
from os import system
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    import discord_webhook
except:
    os.system('pip install discord_webhook')
    import discord_webhook

import queue
try:
    import colorama
    from colorama import Fore, init
except:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore, init
from queue import Queue
urls = queue.Queue()
try:
    import threading
    from threading import Thread
except:
    os.system('pip install threading')
    import threading
    from threading import Thread
try:
    import dhooks
    from dhooks import Webhook
except:
    os.system('pip install dhooks')
    import dhooks
    from dhooks import Webhook

init()
P = []
import random

userslist = input(f'[{Fore.GREEN}?{Fore.WHITE}{Fore.RESET}{Fore.BLUE}] Userlist : ')
p_file = input(f'[{Fore.GREEN}?{Fore.WHITE}{Fore.RESET}{Fore.BLUE}] Proxy File : ')
for i in open(p_file, 'r').read().splitlines():
	        P.append(i)
for line in open(userslist, 'r'):
            urls.put(line.strip())
from discord_webhook import DiscordEmbed, DiscordWebhook
u = input('Enter webhook: ')
hook = Webhook(u)
def req():
    while True:
        url = urls.get()
        Proxy = random.choice(P)
        Proxy.strip()
        prox = {
						'http': f'http://{Proxy}',
						'https': f'http://{Proxy}'
					}
        
        r = requests.head(f"https://discordapp.com/api/invites/{url}", proxies=prox).status_code
        if r == 404:

                            hook.send(f"discord.gg/{url} is available")
        elif r == 200:
            pass
        else:
            print(f'{r}')
threading.Thread(target=req).start()
threading.Thread(target=req).start()
threading.Thread(target=req).start()
threading.Thread(target=req).start()
