import os
from colorama import Fore, Style, init
import requests
import flask
import threading
from concurrent.futures import ThreadPoolExecutor
import time
from turtle import Turtle, Screen
init(autoreset=True)  # هذا يخلي اللون يرجع عادي بعد الطباعة
owis = (Fore.CYAN + "Owis")


def boot():
    print("started")
    os.system("clear")
    print("started")
    print(Fore.LIGHTBLUE_EX + "AUTHOUR:", owis)
    
boot()

while True:
    name = input(
        "just for using this tool you agree that is for educational purposes only "
        "if you agree press enter, else Ctrl+Z"
    )
    if name == "":
        break  # ضغط Enter فقط
    else:
        print("\033[91mPlease press Enter only!\033[0m")  # رسالة باللون الأحمر

RED = "\033[91m"
RESET = "\033[0m"
print(Fore.YELLOW + "warning")
print(RED + " you agreed using tool for educational purposes only " + RESET, name)

host = input("target host or url: ")

if not host.startswith(("http://", "https://")):
    host = "https://" + host
    
if not host:
    print(Fore.RED + "you should enter target host or url")
    host = input("target full url: ")
    time.sleep(3)
if not host:
    print(Fore.RED + "you should enter url")
    host = input("target full url: ")
    
if not host:
     print(Fore.RED+ "you should enter url")
     host = input("target full url: ")
     
r = requests.get(host)
print("status ",r.status_code)

password = input("wordlist file: ")
if not password:
    print(Fore.RED + "You should enter an paths file")
    password = input("wordlist file: ") 

base = host.rstrip("/") + "/"
print("trying with "+ host ,password)
def check(p):
    r = requests.get(base + p.strip(), timeout=3)
    if r.status_code == 200:
        print(f"{Fore.GREEN}{base+p.strip()} {r.status_code}{Fore.RESET}")
with ThreadPoolExecutor(max_workers=46) as ex:
    f = open(password, errors="ignore")
    ex.map(check, f)
