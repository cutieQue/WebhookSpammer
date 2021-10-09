import time
from time import sleep
import sys
import os
import requests
import colorama
from colorama import Fore, init
os.system('cls' if os.name == 'nt' else 'clear')
init(convert=True)
colorama.init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝")
sleep(0.2)
print(f"{Fore.LIGHTYELLOW_EX}Version = 1.1\nDev: cutieQue")
sleep(1)
print(f'\n           [{Fore.LIGHTBLUE_EX}1{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Spammer{Fore.RESET}     [{Fore.LIGHTBLUE_EX}2{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Deleter\n')
print(f'{Fore.LIGHTRED_EX}[>] {Fore.RESET}', end='')
choice = int(input(''))

if choice not in [1, 2]:
    print(f'{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.MAGENTA}Option{Fore.RESET} = {Fore.RED}Error{Fore.RESET} : Invalid Choice!')
    time.sleep(1)
    print(f"{Fore.RED}Exiting...")
    time.sleep(3)

if choice == 1:
    print(f"{Fore.RED}Press CTRL+C to Exit when finished with the Spammer!")
    sleep(1.3)
    print(f"{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET} [{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"{Fore.MAGENTA}Message")
    message = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f'[{Fore.LIGHTRED_EX}WEBHOOK SPAMMER LOG{Fore.RESET}] Sent a new message!')

if choice == 2:
  print(f"{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
  webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
  requests.delete(webhook)
  print(f"{Fore.LIGHTGREEN_EX}Done! {Fore.RED}\nExiting now...")
  sleep(1)
  exit()
