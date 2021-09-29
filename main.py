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
print(f"{Fore.LIGHTYELLOW_EX}Dev: cutieQue")
sleep(1)
print(f'{Fore.LIGHTBLUE_EX}\n           [1] Webhook Spammer     [2] Webhook Deleter\n')
print(f'{Fore.LIGHTRED_EX}[>] {Fore.RESET}', end='')
choice = int(input(''))

if choice not in [1, 2]:
    print(f'---\n{Fore.MAGENTA}Option{Fore.RESET} = {Fore.RED}Error{Fore.RESET} : Invalid Choice!')
    time.sleep(1)
    print(f"{Fore.RED}Exiting...")
    time.sleep(3)

if choice == 1:
    print(f"{Fore.RED}Press CTRL+C to Exit when finished with the Spammer!")
    sleep(3)
    print(f"---\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}[>] "))
    print(f"{Fore.MAGENTA}Message{Fore.RESET}")
    message = str(input(f"{Fore.LIGHTRED_EX}[>] "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f'{Fore.LIGHTRED_EX}[WEBHOOK SPAMMER LOG] Sent a new message!')

if choice == 2:
  print(f"\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
  webhook = str(input(f"{Fore.LIGHTRED_EX}[>] "))
  requests.delete(webhook)
  print(f"{Fore.LIGHTGREEN_EX}Done! {Fore.RED}\nExiting now...")
  sleep(1)
  exit()